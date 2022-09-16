import contextlib
import io
import sys
from inspect import currentframe, getargvalues, getdoc, getsource, signature
from time import time
from typing import Any, Callable

ranks = dict()
padding = 16

# Function call counter using class decorator
# Execution time of a function using class decorator
class class_decorator_time_count:
    def __init__(self, function: Callable[[Any], Any]) -> None:
        self.count = 0
        self.function = function
        self.function_name = function.__name__

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        self.count += 1

        start_time = time()
        result = self.function(*args, **kwds)
        print(
            f"'{self.function_name}' call #{self.count} executed in {(time() - start_time):.4f} sec."
        )

        return result


# Original source code dump using class decorator
class class_decorator_dump:
    def __init__(self, function: Callable[[Any], Any]) -> None:
        self.function = function

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        # Results container preparation and output reading
        # Rerouting output stream
        old_stdout = sys.stdout
        new_std_out = io.StringIO()
        sys.stdout = new_std_out

        # Result evaluation
        result = self.function(*args, **kwds)
        output = new_std_out.getvalue().split("\n")

        # Resetting output stream
        sys.stdout = old_stdout

        frame = currentframe()
        documentation = (
            getdoc(self.function).split("\n") if getdoc(self.function) else None
        )
        source = getsource(self.function).split("\n")

        # Function dump results including basic formatting
        print("Name:".ljust(padding), self.function.__name__)

        print("Type:".ljust(padding), self.function.__class__)

        print("Signature:".ljust(padding), signature(self.function))

        print(
            "Arguments:".ljust(padding),
            f"positional {getargvalues(frame)[3]['args']}",
            "".ljust(padding // 2),
            f"key-worded {getargvalues(frame)[3]['kwds']}",
        )

        if documentation:
            print("Documentation:".ljust(padding), documentation[0])
            for item in documentation[1:]:
                print("".ljust(padding), item)

        print("Source Code:".ljust(padding), source[0])
        if len(source) > 1:
            for item in source[1:]:
                print("".ljust(padding), item)

        print("Output:".ljust(padding), output[0])
        for item in output[1:]:
            print("".ljust(padding), item)

        print("Returns:".ljust(padding), result)

        del frame

        return result


# Functions rank evalualor using class decorator
class class_decorator_rank:
    def __init__(self, function: Callable[[Any], Any]) -> None:
        self.function = function
        self.function_name = function.__name__

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        start_time = time()

        with open("output.txt", "a") as output_file:
            with contextlib.redirect_stdout(output_file):
                result = self.function(*args, **kwds)

        ranks[self.function_name] = time() - start_time

        return result
