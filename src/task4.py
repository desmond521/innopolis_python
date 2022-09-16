import contextlib
import datetime
import functools
import io
import sys
import traceback
from inspect import currentframe, getargvalues, getdoc, getsource, signature
from time import time
from typing import Any, Callable

from task3 import ranks

padding = 16


# Function call counter using class decorator
# Execution time of a function using class decorator
# Exception free
class class_decorator_time_count_exception:
    def __init__(self, function: Callable[[Any], Any]) -> None:
        self.count = 0
        self.function = function
        self.function_name = function.__name__

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        self.count += 1

        start_time = time()

        # Exception free
        with open("log.txt", "a") as log_file:
            try:
                result = self.function(*args, **kwds)
            except:
                log_file.write(
                    f"{datetime.datetime.now()}\n{traceback.format_exc()}\n\n"
                )

        print(
            f"'{self.function_name}' call #{self.count} executed in {(time() - start_time):.4f} sec."
        )

        return result


# Original source code dump using class decorator
# Exception free
class class_decorator_dump_exception:
    def __init__(self, function: Callable[[Any], Any]) -> None:
        self.function = function

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        # Results container preparation and output reading
        # Rerouting output stream
        old_stdout = sys.stdout
        new_std_out = io.StringIO()
        sys.stdout = new_std_out

        # Result evaluation
        # Exception free
        with open("log.txt", "a") as log_file:
            try:
                result = self.function(*args, **kwds)
                output = new_std_out.getvalue().split("\n")
            except:
                log_file.write(
                    f"{datetime.datetime.now()}\n{traceback.format_exc()}\n\n"
                )

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
# Exception free
class class_decorator_rank_exception:
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


# Function call counter using function decorator
# Execution time of a function using function decorator
# Exception free
def function_decorator_time_count(function: Callable[[Any], Any]) -> Any:
    @functools.wraps(function)
    def wrapper(*args: Any, **kwds: Any) -> Any:
        wrapper.count += 1

        start_time = time()

        with open("log.txt", "a") as log_file:
            try:
                result = function(*args, **kwds)
            except:
                log_file.write(
                    f"{datetime.datetime.now()}\n{traceback.format_exc()}\n\n"
                )

        print(
            f"'{wrapper.function_name}' call #{wrapper.count} executed in {(time() - start_time):.4f} sec."
        )

        return result

    wrapper.count = 0
    wrapper.function_name = function.__name__

    return wrapper


# Original source code dump using function decorator
# Exception free
def function_decorator_dump_exception(function: Callable[[Any], Any]) -> Any:
    @functools.wraps(function)
    def wrapper(*args: Any, **kwds: Any) -> Any:
        # Results container preparation and output reading
        # Rerouting output stream
        old_stdout = sys.stdout
        new_std_out = io.StringIO()
        sys.stdout = new_std_out

        # Result evaluation
        # Exception free
        with open("log.txt", "a") as log_file:
            try:
                result = function(*args, **kwds)
                output = new_std_out.getvalue().split("\n")
            except:
                log_file.write(
                    f"{datetime.datetime.now()}\n{traceback.format_exc()}\n\n"
                )

        # Resetting output stream
        sys.stdout = old_stdout

        frame = currentframe()
        documentation = getdoc(function).split("\n") if getdoc(function) else None
        source = getsource(function).split("\n")

        # Function dump results including basic formatting
        print("Name:".ljust(padding), function.__name__)

        print("Type:".ljust(padding), function.__class__)

        print("Signature:".ljust(padding), signature(function))

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

    return wrapper
