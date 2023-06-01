a = [-1, 1, 66.25, 333, 333, 1234.5]

del a[0]  # Xóa phần tử thứ 0 trong mảng
print(a)
# [1, 66.25, 333, 333, 1234.5]

del a[2:4]  # Xóa từ các phần tử từ tham số thứ nhất đến tham số thứ hai trong mảng
print(a)
# [1, 66.25, 1234.5]

del a[:]  # Xóa toàn bộ phần tử trong mảng (a[:] là bản sao của mảng a)
print(a)
# []

del a  # Xóa biến
print(a)
