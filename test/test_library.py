import time

def test_search(func):
    def wrapper():
        print("Test: "+func.__name__+"\n------")
        start_time = time.perf_counter()
        func()
        end_time = time.perf_counter()
        print(func.__name__ + " runtime: %d seconds." %(end_time - start_time))
        print("------")
    return wrapper
