import time
from typing import Callable


def get_timing[T](func: Callable[[], T]) -> tuple[T, float]:
    """Times an arbitrary callable.

    Args:
        func (Callable): The function to time.

    Returns:
        tuple[Any, float]: A tuple containing the result of the callable and the elapsed time in seconds.
    """
    start_time = time.perf_counter()
    result = func()
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    return result, elapsed_time
