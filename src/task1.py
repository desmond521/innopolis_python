import functools
from time import time
from typing import Any, Callable


# Function call counter using function decorator
# Execution time of a function using function decorator
def function_decorator_time_count(function: Callable[[Any], Any]) -> Any:
    @functools.wraps(function)
    def wrapper(*args: Any, **kwds: Any) -> Any:
        wrapper.count += 1

        start_time = time()
        result = function(*args, **kwds)
        print(
            f"'{wrapper.function_name}' call #{wrapper.count} executed in {(time() - start_time):.4f} sec."
        )

        return result

    wrapper.count = 0
    wrapper.function_name = function.__name__

    return wrapper
