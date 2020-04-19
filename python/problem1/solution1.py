from functools import reduce


def calculate() -> int:
    result = 0

    for i in range(0, 1000):
        if i % 3 == 0 or i % 5 == 0:
            result += i

    return result


def calculate_functional() -> int:
    return reduce(int.__add__, filter(lambda i: i % 3 == 0 or i % 5 == 0, range(1, 1000)))


def calculate_functional_v2() -> int:
    return sum(filter(lambda i: i % 3 == 0 or i % 5 == 0, range(1, 1000)))


def calculate_functional_pythonic() -> int:
    return sum([i for i in range(1, 1000) if i % 3 == 0 or i % 5 == 0])


def main():
    print(calculate())
    print(calculate_functional())
    print(calculate_functional_v2())
    print(calculate_functional_pythonic())


if __name__ == '__main__':
    main()
