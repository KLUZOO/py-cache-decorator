from typing import Callable


def cache(func: Callable) -> Callable:
    data = {}

    def inner(*args, **kwargs) -> int:
        if args in data:
            print("Getting from cache")
            return data[args]
        else:
            print("Calculating new result")
            res = func(*args, **kwargs)
            data[args] = res
            return res

    return inner
