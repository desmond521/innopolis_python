import functools
from time import time
from typing import Any, Callable

from task4 import function_decorator_exception


# Function call counter using function decorator
# Function execution time using function decorator
def function_decorator_time_count(
    function: Callable[[Any], Any]
) -> Callable[[Any, Any], Any]:
    @functools.wraps(function)
    def wrapper(*args: Any, **kwds: Any) -> Any:
        wrapper.count += 1

        start = time()
        output, result, flag = function_decorator_exception(function)(*args, **kwds)
        print(
            f"'{function.__name__}' call #{wrapper.count} executed in {(time() - start):.4f} sec. {'with an exception' if flag else ''}"
        )

        return output, result, flag

    wrapper.count = 0

    return wrapper
