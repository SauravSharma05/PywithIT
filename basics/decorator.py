import time

class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()  
        result = self.func(*args, **kwargs)
        end_time = time.time()  
        print(f"Function '{self.func.__name__}' executed in {end_time - start_time:.4f} seconds")
        return result
    
@Timer
def slow_function(seconds):
    time.sleep(seconds)
    return "Finished sleeping"

result = slow_function(2)
print(result)