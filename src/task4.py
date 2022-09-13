import contextlib
import datetime
import traceback
from time import time
from typing import Any, Callable

ranks = dict()
padding = 16

# Functions rank evalualor exception free decorator
class class_decorator_3:
    def __init__(self, function: Callable[[Any], Any]) -> None:
        self.function = function
        self.function_name = function.__name__

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        result = None
        start_time = time()

        with open("output.txt", "a") as output_file, open("log.txt", "a") as log_file:
            with contextlib.redirect_stdout(output_file):
                # , contextlib.redirect_stderr(log_file):
                try:
                    result = self.function(*args, **kwds)
                    ranks[self.function_name] = time() - start_time
                except:
                    log_file.write(
                        f"{datetime.datetime.now()}\n{traceback.format_exc()}\n\n"
                    )

        return result
