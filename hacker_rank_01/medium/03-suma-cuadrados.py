n = int(input())


def square_sum(x) -> int:
    if x <= 0:
        raise RuntimeError("x must be a entire number greater than 0")

    result: int = 0
    for i in range(1, x + 1):
        result += i**2
    return result


print(f'{square_sum(n)}')
