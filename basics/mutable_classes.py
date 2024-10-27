# mutalble classes 
class Pointer:
    def __init__(self, value):
        self.value = value

def increment_pointer(ptr):
    ptr.value += 1  

ptr = Pointer(10)
print("Before increment:", ptr.value)  
increment_pointer(ptr)
print("After increment:", ptr.value)  