import time


class service_method(object):
    def __init__(self, logging=True):
        self.logging = logging

    def __call__(self, method):
        def wrapped(obj, *args, **kwargs):
            if self.logging:
                obj.logger.info(
                    "{}.{} called".format(obj.__class__.__name__, method.__name__)
                )
            s_time = time.time() * 1000

            result = method(obj, *args, **kwargs)

            t_time = time.time() * 1000 - s_time
            if self.logging:
                obj.logger.debug(
                    "Execution time for {}.{}: {}ms".format(
                        obj.__class__.__name__, method.__name__, t_time
                    )
                )
            return result

        return wrapped
