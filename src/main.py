from math import sqrt
from random import randint
from typing import List, Tuple

from task1 import function_decorator_time_count
from task2 import function_decorator_dump
from task3 import (
    class_decorator_time_count,
    class_decorator_dump,
    class_decorator_rank,
    ranks,
)
from task4 import (
    class_decorator_time_count_exception,
    class_decorator_dump_exception,
    class_decorator_rank_exception,
    function_decorator_time_count,
    function_decorator_dump_exception,
)

why_1 = lambda x, y: x**y
why_2 = lambda x: lambda y: x**y


def quadratic_equation_solver(a: float, b: float, c: float) -> Tuple[float, float]:
    """
    My quadratic equation solver funciton.

    Parameters
    ----------
    a : float
        coefficient a
    b : float
        coefficient b
    c : float
        coefficient c

    Returns
    -------
    Tuple[float, float]
        a tuple of x_1 and x_2

    Raises
    ------
    ValueError
        when the discriminant is less than zero
    """
    discriminant = b**2 - 4 * a * c

    if discriminant < 0:
        raise ValueError

    x_1 = (-b + sqrt(discriminant)) / (2 * a)
    x_2 = (-b - sqrt(discriminant)) / (2 * a)

    print(f"'x_1' = {x_1}, 'x_2' = {x_2}.")
    return (x_1, x_2)


def pascal_triangle_printer(n: int = 1000) -> List[List[int]]:
    """
    My Pascal triangle printer function.

    Parameters
    ----------
    n : int, optional
        number of rows

    Returns
    -------
    List[List[int]]
        a list of n-rows of the Pascal Triangle

    Raises
    ------
    ValueError
        when the parameter n is less than or equals zero
    """
    if n <= 0:
        raise ValueError

    length = 0
    rows = [[1]]

    while len(rows) != n:
        rows.append(
            [a + b for a, b in zip([0] + rows[length - 1], rows[length - 1] + [0])]
        )
        length = len(rows)

    print(rows)
    return rows


def func() -> None:
    """
    A simple function.

    Returns
    -------
    None
    """
    print("I'm ready to start...")
    result = 0
    n = randint(10, 751)
    for i in range(n):
        result += i**2


def funx(n: int = 2, m: int = 10) -> None:
    """
    A simple function.

    Parameters
    ----------
    n : int, optional
        power
    m : int, optional
        range

    Returns
    -------
    None
    """
    print("I'm ready to do some serious stuff...")
    max_val = float("-inf")
    n = randint(10, 751)
    result = [why_1(i, n) for i in range(m)]
    for i in result:
        if i > max_val:
            max_val = i


def funh(bar1, bar2=""):
    """
    This function does something useful.

    Parameters
    ----------
    bar1 : Any
        bar1 description
    bar2 : Any, optional
        bar2 description

    Returns
    -------
    None
    """
    print("some\nmultiline\noutput")


def show_ranks() -> None:
    """
    This function shows the ranking table of the decorated functions.

    Returns
    -------
    None
    """
    global ranks
    padding = 26

    ranks = dict(sorted(ranks.items(), key=lambda item: item[1]))

    print("FUNCTION".ljust(padding), "RANK".ljust(padding // 4), "TIME ELAPSED (SEC.)")
    for index, (key, value) in enumerate(ranks.items()):
        print(
            str(key).ljust(padding),
            str(index + 1).ljust(padding // 4),
            f"{value:.6f}",
        )


if __name__ == "__main__":
    # 1
    # func_time_count = function_decorator_time_count(func)
    # func_time_count()

    # funx_time_count = function_decorator_time_count(funx)
    # funx_time_count()

    # func_time_count()

    # funx_time_count()

    # func_time_count()

    # pascal_triangle_printer_time_count = function_decorator_time_count(
    #     pascal_triangle_printer
    # )
    # pascal_triangle_printer_time_count(20)

    # 2
    # class_decorator_time_count(funh)(None, bar2="")

    # function_decorator_dump(funh)(None, bar2="")
    # class_decorator_dump(funh)(None, None)
    # class_decorator_dump(pascal_triangle_printer)(10)
    # class_decorator_dump(quadratic_equation_solver)(-2, 2, 1)

    # 3
    class_decorator_rank(func)()
    class_decorator_rank(funx)()
    class_decorator_rank(funh)(None, bar2="")
    class_decorator_rank(why_1)(4, 6)
    class_decorator_rank(why_2)(4)(6)

    # 4
    # Exception
    # class_decorator_rank_exception(quadratic_equation_solver)(1, 1, 1)
    # class_decorator_rank_exception(quadratic_equation_solver)(-2, 2, 1)
    # class_decorator_rank_exception(pascal_triangle_printer)(10)

    show_ranks()
