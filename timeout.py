from functools import wraps
import signal


class TimeOutError(Exception):
    pass


def timeout():
    def decorator(func):
        def _handle_timeout(signum, frame):
            raise TimeOutError

        def wrapper(*args, **kwargs):
            seconds = args[0].timeout
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result
        return wraps(func)(wrapper)
    return decorator
