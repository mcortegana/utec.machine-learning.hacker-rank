x = int(input())


def factorial(n: int) -> int:
    if n < 0:
        raise RuntimeError("Factorial only applies for entire positive numbers")
    result: int = 1
    for i in range(2, n + 1):
        result *= i
    return result


print(f'{factorial(x)}')
