import time, functools

def clockwork(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter() - start
        name = func.__name__
        arg_list = [repr(arg) for arg in args]
        arg_list.extend(f'{key} = {value}' for k, v in kwargs.items())
        arg_string = ', '.join(arg_list)
        print(f"[{end:0.8f}s] {name}({arg_string}) -> {result!r}")
        return result
    return clocked

@functools.lru_cache
@clockwork
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

@clockwork
def factorial(n):
    if n == 1:
        return n
    return factorial(n - 1) * n

print(fibonacci(10))
print(factorial(10))
