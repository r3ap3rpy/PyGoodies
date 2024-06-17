try:
    from flask import Flask, request, abort, Response
except:
    raise SystemExit("Please: pip install flask")
import sys

sys.path.append("..\\")
from FileDict import FileDict

my_dict = FileDict(dirname='flaskdict')

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def index():
    global my_dict
    return dict(my_dict)

@app.route("/set", methods = ['POST'])
def setitem():
    global my_dict
    my_key = request.args.get("key",0)
    my_value = request.args.get("value",0)
    if my_key and my_value:
        my_dict[my_key] = my_value
        return dict({my_key : my_value})
    else:
        abort(400, "/set?key=name&value=value")

@app.route("/get", methods = ["GET"])
def getitem():
    global my_dict
    if my_dict.get(request.args.get('key')):
        return dict({request.args.get('key') : my_dict[request.args.get('key')]})
    else:
        return dict({request.args.get('key') : 'N.A.'})
    
@app.route("/del", methods = ["POST"])
def delitem():
    global my_dict
    if my_dict.get(request.args.get('key')):
        del my_dict[request.args.get('key')]
        return f"Key: {request.args.get('key')} deleted..."
    else:
        return f"Key: {request.args.get('key')} not found..."
    
if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 8000, debug = True)