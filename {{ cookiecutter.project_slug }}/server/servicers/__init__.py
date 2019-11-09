import time


def service_method(method):
    def wrapper(self, *args, **kwargs):
        print("{} called".format(method.__name__))
        s_time = time.time()*1000

        result = method(self, *args, **kwargs)

        t_time = time.time()*1000 - s_time
        print("Execution time for {}: {}ms".format(method.__name__, t_time))
        return result
    return wrapper
