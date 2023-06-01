tel = {"jack": 4098, "sape": 4139}

tel["guido"] = 4127  # Thêm phần tử có khóa là "guido" và giá trị là 4127 vào từ điển
print(tel)
# {'jack': 4098, 'sape': 4139, 'guido': 4127}

print(tel["jack"])  # Lấy ra phần tử có khóa là "jack" trong từ điển
# 4098

del tel["sape"]  # Xóa phần tử có khóa là "sape" trong từ điển
tel["irv"] = 4127  # Thêm phần tử có khóa là "irv" và giá trị là 4127 vào từ điển
print(tel)
# {"jack": 4098, "guido": 4127, "irv": 4127}

print(list(tel))  # Lấy ra tất cả các khóa có trong từ điển
# ["jack", "guido", "irv"]

print(sorted(tel))  # Lấy ra tất cả các khóa có trong từ điển sau khi được sắp xếp
# ["guido", "irv", "jack"]

print(
    "guido" in tel
)  # Lấy ra giá trị đúng hoặc sai biểu diễn cho sự tồn tại của phần tử có khóa là "guido" trong từ điển
# True

print(
    "jack" not in tel
)  # Lấy ra giá trị đúng hoặc sai biểu diễn cho sự tồn tại của phần tử có khóa là "jack" trong từ điển
# False
