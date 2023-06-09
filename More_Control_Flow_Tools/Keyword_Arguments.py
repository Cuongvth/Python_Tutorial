def support(param1, param2=None, param3="Param3"):
    print(f"Parameter 1: {param1}")
    print(f"Parameter 2: {param2}")
    print(f"Parameter 3: {param3}")


def Demo():
    support(input("Param1: "))
    support(input("Param1: "), input("Param2: "), input("Param3: "))
    support(
        param1=input("Param1: "), param2=input("Param2: "), param3=input("Param3: ")
    )
    support(input("Param1: "), param2=input("Param2: "), param3=input("Param3: "))
