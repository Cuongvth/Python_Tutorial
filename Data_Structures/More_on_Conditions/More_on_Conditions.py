string1, string2, string3 = (
    "",
    "Trondheim",
    "Hammer Dance",
)  # Khỏi tạo ba đối tượng string1, string2, string3 với các giá trị tương ứng

non_null = (
    string1 or string2 or string3
)  # Khởi tạo đối tượng non_null co giá trị là phần tử đầu tiên có giá trị trong ba phần tử string1, string2, string3

print(non_null)
