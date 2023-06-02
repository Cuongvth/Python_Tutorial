import locale


def Demo():
    print(locale.setlocale(locale.LC_ALL, "English_United States.1252"))
    conv = locale.localeconv()
    print(
        locale.format_string(
            "%s%.*f",
            (
                conv["currency_symbol"],
                conv["frac_digits"],
                float(input("Nhập số tiền: ")),
            ),
            grouping=True,
        )
    )
