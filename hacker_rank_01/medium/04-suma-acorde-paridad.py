n = int(input())


def parity_sum(x) -> int:
    if x < 0:
        raise RuntimeError("x must be a entire number greater than or equals to 0")

    if x % 2 == 0:
        return even_numbers_sum(x)
    if x % 2 != 0:
        return odd_numbers_sum(x)

    return 0


def even_numbers_sum(x) -> int:
    result: int = 0
    for i in range(1, x + 1):
        if i % 2 == 0:
            result += i
    return result


def odd_numbers_sum(x) -> int:
    result: int = 0
    for i in range(1, x + 1):
        if i % 2 != 0:
            result += i
    return result


print(f'{parity_sum(n)}')
