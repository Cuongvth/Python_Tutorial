basket = {"apple", "orange", "apple", "pear", "orange", "banana"}

print(basket)
# {"orange", "banana", "pear", "apple"}

print(
    "orange" in basket
)  # In ra giá trị đúng hoặc sai biểu diễn cho sự tồn tại của đối tượng chỉ định
# True

print(
    "crabgrass" in basket
)  # In ra giá trị đúng hoặc sai biểu diễn cho sự tồn tại của đối tượng chỉ định
# False

a = set(
    "abracadabra"
)  # Tạo đối tượng a với các phần tử là các kí tự có trong chuỗi chỉ định không có các kí tự lặp lại

b = set(
    "alacazam"
)  # Tạo đối tượng b với các phần tử là các kí tự có trong chuỗi chỉ định không có các kí tự lặp lại

print(a)
# {"a", "r", "b", "c", "d"}

print(a - b)  # Phần tử tồn tại trong a nhưng không tồn tại trong b
# {"r", "d", "b"}

print(a | b)  # Phàn tử tồn tại trong a hoặc trong b
# {"a", "c", "r", "d", "b", "m", "z", "l"}

print(a & b)  # Phần tử tồn tại ở trong cả a và b
# {"a", "c"}

print(
    a ^ b
)  # Phần tử tồn tại ở trong a hoặc b nhưng không tồn tại trong đối tượng còn lại
# {"r", "d", "b", "m", "z", "l"}
