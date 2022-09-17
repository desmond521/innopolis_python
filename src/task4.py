import datetime
from contextlib import redirect_stdout
from functools import wraps
from io import StringIO
from traceback import format_exc
from typing import Any, Callable

padding = 16

# Exception free function decorator
def function_decorator_exception(function: Callable[[Any], Any]) -> Any:
    @wraps(function)
    def wrapper(*args: Any, **kwds: Any) -> Any:
        with open("output.txt", "a") as output_file, open("log.txt", "a") as log_file:
            with redirect_stdout(StringIO()) as output:
                try:
                    flag = False
                    result = function(*args, **kwds)
                    output_file.write(
                        f"{datetime.datetime.now()}\n{output.getvalue()}\n"
                    )
                except:
                    flag = True
                    log_file.write(f"{datetime.datetime.now()}\n{format_exc()}\n")
                    return output, None, flag

        return output, result, flag

    return wrapper


# Exception free class decorator
class class_decorator_exception:
    def __init__(self, function: Callable[[Any], Any]) -> None:
        self.function = function

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        with open("output.txt", "a") as output_file, open("log.txt", "a") as log_file:
            with redirect_stdout(StringIO()) as output:
                try:
                    flag = False
                    result = self.function(*args, **kwds)
                    output_file.write(
                        f"{datetime.datetime.now()}\n{output.getvalue()}\n"
                    )
                except:
                    flag = True
                    log_file.write(f"{datetime.datetime.now()}\n{format_exc()}\n")
                    return output, None, flag

        return output, result, flag
