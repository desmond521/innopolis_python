# innopolis_python

## Python Assignment 1

> Run *main.py* to inspect tasks and receive output.

All source files (*.py) are located in '_src/_' directory.

1. _main.py_
    * file to run.
    * contains test functions.
    * applies decorators (implemented in tasks 1-4) on test functions.
    * shows test results.
2. _task1.py_ 
    * contains function decorator that print information about decorated function:
       * function name.
       * number of function calls.
       * function execution time.
3. _task2.py_
    * contains function decorator that prints information about a decorated function:
    1. output from the 1st task.
    2. function name.
    3. function object.
    4. function signature.
    5. function arguments.
        1. positional.
        2. key-worded.
    6. function docstring.
    7. function source code.
    8. function output.
    9. function return value.
4. _task3.py_
    * contains class decorators with the same behaviour as ones from tasks 1 and 2.
    * also implemented class decorator that rank decorated functions by the execution time.
5. _task4.py_
    * extends decorator_1 behaviour while protecting decorated functions from exceptions, using '_Try and Except_' statement.
    * in case of raised exception, redirects stderr to logfile including timestamp.
