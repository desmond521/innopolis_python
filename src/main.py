from math import sqrt
from random import randint
from typing import List, Tuple

from task1 import decorator_1
from task2 import decorator_2

# from task3 import class_decorator_1, class_decorator_2, class_decorator_3, ranks
from task4 import class_decorator_3, ranks


def quadratic_equation_solver(a: float, b: float, c: float) -> Tuple[float, float]:
    discriminant = b**2 - 4 * a * c

    if discriminant < 0:
        raise ValueError

    x_1 = (-b + sqrt(discriminant)) / (2 * a)
    x_2 = (-b - sqrt(discriminant)) / (2 * a)

    print(f"'x_1' = {x_1}, 'x_2' = {x_2}.")
    return (x_1, x_2)
    # return x_1


def pascal_triangle_printer(n: int = 1000) -> List[List[int]]:
    """Returns n-rows of the Pascal Triangle.

    Parameters:
            n (int): A integer number of rows (default 1000)

    Returns:
            rows (List[List[int]]): the Pascal Triangle rows
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


# @decorator_1
def func() -> None:
    print("I'm ready to start...")
    result = 0
    n = randint(10, 751)
    for i in range(n):
        result += i**2


# @decorator_1
def funx(n: int = 2, m: int = 10) -> None:
    print("I'm ready to do some serious stuff...")
    max_val = float("-inf")
    n = randint(10, 751)
    result = [pow(i, n) for i in range(m)]
    for i in result:
        if i > max_val:
            max_val = i


def funh(bar1, bar2=""):
    """
    This function does something useful
    :param bar1: description
    :param bar2: description
    """
    print("some\nmultiline\noutput")


def show_ranks() -> None:
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
    # func()
    # funx()
    # func()
    # funx()
    # func()
    # pascal_triangle_printer(2500)

    # 2
    # funh_time = decorator_1(funh)
    # funh_time(None, bar2="")

    # funh_dump = decorator_2(funh)
    # funh_dump(None, bar2="")

    # 3, 4
    func_rank = class_decorator_3(func)
    func_rank()

    funx_rank = class_decorator_3(funx)
    funx_rank()

    funh_rank = class_decorator_3(funh)
    funh_rank(None, bar2="")

    # Exception
    quadratic_equation_solver_rank = class_decorator_3(quadratic_equation_solver)
    # quadratic_equation_solver_rank(-2, 2, 1)
    quadratic_equation_solver_rank(1, 1, 1)

    pascal_triangle_printer_rank = class_decorator_3(pascal_triangle_printer)
    pascal_triangle_printer_rank(10)

    show_ranks()
