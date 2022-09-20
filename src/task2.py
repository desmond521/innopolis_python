import sys
from functools import wraps
from inspect import getsource, signature
from textwrap import indent
from typing import Any, Callable

from task1 import function_decorator_time_count

padding = 16

# See: https://peps.python.org/pep-0257/
def trim(docstring: str) -> str:
    if not docstring:
        return ""
    # Convert tabs to spaces (following the normal Python rules) and split into a list of lines:
    lines = docstring.expandtabs().splitlines()
    # Determine minimum indentation (first line doesn't count):
    indent = sys.maxsize
    for line in lines[1:]:
        stripped = line.lstrip()
        if stripped:
            indent = min(indent, len(line) - len(stripped))
    # Remove indentation (first line is special):
    trimmed = [lines[0].strip()]
    if indent < sys.maxsize:
        for line in lines[1:]:
            trimmed.append(line[indent:].rstrip())
    # Strip off trailing and leading blank lines:
    while trimmed and not trimmed[-1]:
        trimmed.pop()
    while trimmed and not trimmed[0]:
        trimmed.pop(0)
    # Return a single string:
    return "\n".join(trimmed)


# Original source code dump using function decorator
def function_decorator_dump(
    function: Callable[[Any], Any]
) -> Callable[[Any, Any], Any]:
    @wraps(function)
    def wrapper(*args: Any, **kwds: Any) -> Any:
        # Function dump container preparation and output/return reading
        # Function execution time printer
        output, result, exc_flag = function_decorator_time_count(function)(*args, **kwds)
        documentation = indent(trim(function.__doc__), padding * " ")[padding:]
        source = indent(getsource(function), padding * " ")[padding:]
        output = indent(output.getvalue(), padding * " ")[padding:]

        # Function dump results including basic formatting
        print("Name:".ljust(padding), function.__name__, sep="")
        print("Type:".ljust(padding), function.__class__, sep="")
        print("Signature:".ljust(padding), signature(function), sep="")
        print("Arguments:".ljust(padding), "positional:".ljust(padding), args, sep="")
        print("".ljust(padding), "key-worded:".ljust(padding), kwds, sep="", end="\n\n")
        print("Documentation:".ljust(padding), documentation, sep="", end="\n\n")
        print("Source Code:".ljust(padding), source, sep="")
        print("Output:".ljust(padding), output, sep="")
        print("Returns:".ljust(padding), result, sep="")

        return result

    return wrapper
