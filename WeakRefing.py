import  weakref

my_set = {1,2,3,4,5}
my_set_2 = my_set

def garbage_disposed():
    print("I am not feeling too well...")

garbage_disposed = weakref.finalize(my_set, garbage_disposed)

print(garbage_disposed.alive)
del my_set
print("No we remove my_set_2 from reference....")
my_set_2 = "No the original anymore!"
