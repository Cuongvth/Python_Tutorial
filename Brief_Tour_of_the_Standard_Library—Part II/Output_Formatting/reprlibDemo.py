import reprlib


def Demo():
    print(
        reprlib.repr(
            set(
                input(
                    "Hãy nhập một vài kí tự tôi sẽ giúp bạn loại bỏ kí tự trùng lặp và rút gọn nó: "
                )
            )
        )
    )
