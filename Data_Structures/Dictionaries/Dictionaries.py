tel = {"jack": 4098, "sape": 4139}

tel["guido"] = 4127  # Thêm phần tử có key là "guido" và giá trị là 4127
print(tel)
# {'jack': 4098, 'sape': 4139, 'guido': 4127}

print(tel["jack"])  # In ra phần tử có key là "jack"
# 4098

del tel["sape"]  # Xóa phần tử có key là "sape"
tel["irv"] = 4127  # Thêm phần tử có key là "irv" và giá trị là 4127
print(tel)
# {"jack": 4098, "guido": 4127, "irv": 4127}

print(list(tel))  # In tất cả các key có trong đối tượng
# ["jack", "guido", "irv"]

print(sorted(tel))  # In tất cả các key có trong đối tượng sau khi được sắp xếp
# ["guido", "irv", "jack"]

print(
    "guido" in tel
)  # In ra giá trị đúng hoặc sai biểu diễn cho sự tồn tại của đối tượng có key là "guido"
# True

print(
    "jack" not in tel
)  # In ra giá trị đúng hoặc sai biểu diễn cho sự tồn tại của đối tượng có key là "jack"
# False
