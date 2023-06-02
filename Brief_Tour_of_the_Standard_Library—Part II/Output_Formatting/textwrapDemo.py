import textwrap


def Demo():
    print(
        textwrap.fill(
            input("Hãy nhập một đoạn văng bản: "),
            width=int(input("Nhập giới hạn kí tự mỗi dòng: ")),
        )
    )
