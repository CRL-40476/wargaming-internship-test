def isEven(value):
    """
    Плюсы: более выразительный код, более читаемый
    Минусы: в Python деление чисел имеет вычислительную сложность O(x^2),
    в связи с тем, что с увеличением делимого высчитываемое количество групп
    делителя в делимом возрастает с квадратичной скоростью
    """
    return value % 2 == 0


def alt_is_even(value):
    """
    Плюсы: побитовые операции явно будут выполняться быстрее
    Минусы: менее читаемый и и менее выразительный код
    """
    return value & 0x1 == 0

if __name__ == "__main__":
    print(alt_is_even(11))
    print(alt_is_even(12))
    print(alt_is_even(13))
    print(alt_is_even(0))
    print(alt_is_even(1))
    print(alt_is_even(-1))
    print(alt_is_even(-2))
    print(alt_is_even(-3))