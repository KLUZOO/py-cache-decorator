from typing import Callable


def cache(func: Callable) -> Callable:
    data = {}

    def inner(*args, **kwargs) -> int:
        if args in data and tuple(kwargs.values()) in data:
            print("Getting from cache")
            return data[args]
        else:
            print("Calculating new result")
            res = func(*args, **kwargs)
            data[args] = res
            data[tuple(kwargs.values())] = res
            return res

    return inner
