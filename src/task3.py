import datetime
from contextlib import redirect_stdout
from inspect import getsource, signature
from textwrap import indent
from time import time
from typing import Any, Callable

from task2 import trim
from task4 import class_decorator_exception

ranks = dict()
padding = 16

# Function call counter using class decorator
# Execution time of a function using class decorator
class class_decorator_time_count:
    def __init__(self, function: Callable[[Any], Any]) -> None:
        self.count = 0
        self.function = function

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        self.count += 1

        start = time()
        output, result, exc_flag = class_decorator_exception(self.function)(*args, **kwds)
        with open("output.txt", "a") as output_file:
            with redirect_stdout(output_file):
                print(
                    f"{datetime.datetime.now()}\n'{self.function.__name__}' call #{self.count} executed in {(time() - start):.4f} sec. {'with an exception' if exc_flag else ''}\n"
                )

        return output, result, exc_flag


# Original source code dump using class decorator
class class_decorator_dump:
    def __init__(self, function: Callable[[Any], Any]) -> None:
        self.function = function

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        # Function dump container preparation and output/return reading
        output, result, exc_flag = class_decorator_time_count(self.function)(*args, **kwds)
        documentation = indent(trim(self.function.__doc__), padding * " ")[padding:]
        source = indent(getsource(self.function), padding * " ")[padding:]
        output = indent(output.getvalue(), padding * " ")[padding:]

        # Function dump results including basic formatting
        with open("output.txt", "a") as output_file:
            with redirect_stdout(output_file):
                print(f"{datetime.datetime.now()}\n")
                print("Name:".ljust(padding), self.function.__name__, sep="")
                print("Type:".ljust(padding), self.function.__class__, sep="")
                print("Signature:".ljust(padding), signature(self.function), sep="")
                print(
                    "Arguments:".ljust(padding),
                    "positional:".ljust(padding),
                    args,
                    sep="",
                )
                print(
                    "".ljust(padding),
                    "key-worded:".ljust(padding),
                    kwds,
                    sep="",
                    end="\n\n",
                )
                print(
                    "Documentation:".ljust(padding), documentation, sep="", end="\n\n"
                )
                print("Source Code:".ljust(padding), source, sep="")
                print("Output:".ljust(padding), output, sep="")
                print("Returns:".ljust(padding), result, sep="", end="\n\n")

        return result


# Functions rank collector using class decorator
class class_decorator_rank:
    def __init__(self, function: Callable[[Any], Any]) -> None:
        self.function = function

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        start_time = time()
        output, result, exc_flag = class_decorator_exception(self.function)(*args, **kwds)
        end = time() - start_time
        ranks[self.function.__name__] = end

        return result
