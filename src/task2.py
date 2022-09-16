import functools
import io
import sys
from inspect import currentframe, getargvalues, getdoc, getsource, signature
from typing import Any, Callable

padding = 16

# Original source code dump using function decorator
def function_decorator_dump(function: Callable[[Any], Any]) -> Any:
    @functools.wraps(function)
    def wrapper(*args: Any, **kwds: Any) -> Any:
        # Results container preparation and output reading
        # Rerouting output stream
        old_stdout = sys.stdout
        new_std_out = io.StringIO()
        sys.stdout = new_std_out

        # Result evaluation
        result = function(*args, **kwds)
        output = new_std_out.getvalue().split("\n")

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
