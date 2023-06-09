def standard_arg(arg):
    print(arg)


def pos_only_arg(arg, /):
    print(arg)


def kwd_only_arg(*, arg):
    print(arg)


def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)


def Demo():
    standard_arg(input("Param: "))
    pos_only_arg(input("Param: "))
    kwd_only_arg(arg=input("Param: "))
    combined_example(
        input("Param1: "), standard=input("Param2: "), kwd_only=input("Param3: ")
    )
