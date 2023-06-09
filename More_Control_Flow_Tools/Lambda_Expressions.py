def make_incrementor(n):
    return lambda x: x + n


def Demo():
    try:
        n = int(input("n: "))
        x = int(input("x: "))
        f = make_incrementor(n)
        print(f"{x} + {n} = {f(x)}")
    except Exception as ex:
        print(ex)
