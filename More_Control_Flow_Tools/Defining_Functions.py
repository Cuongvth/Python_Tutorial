def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b
    print()


def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


def Demo():
    try:
        fib(int(input("Max number: ")))
        print(fib2(int(input("Max number: "))))
    except Exception as ex:
        print(ex)
