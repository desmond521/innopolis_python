# innopolis_python

## Python Assignment 1

> Run **main.py** to inspect tasks and receive output.

All source files (*.py) are located in '_src/_' directory.

1. **main.py**
    
    * file to run.
    * contains test functions.
    * applies decorators (implemented in tasks 1-4) on test functions.
    * shows test results.
    
2. **task1.py**
    
    Contains function decorator that prints information about decorated functions:
    
    * function name.
    * number of function calls.
    * function execution time.
    
3. **task2.py**
    
    Contains function decorator that prints information about decorated functions:
    
    * output from the 1st task.
    * function name.
    * function object.
    * function signature.
    * function arguments.
        * positional.
        * key-worded.
    * function docstring.
    * function source code.
    * function output.
    * function return value.
    
4. **task3.py**
    
    Contains class decorators with the same behaviour as ones from tasks 1 and 2.
    
    Also implemented class decorator that rank decorated functions by the execution time.
    
5. **task4.py**
    
    Extends decorators behaviour while protecting decorated functions from exceptions, using **Try & Except** statement.
    
    In case of raised exception, redirects stderr to logfile including timestamp.
