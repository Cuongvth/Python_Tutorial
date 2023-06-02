def divide(x, y):
    try:
        result = x / y  # Cố gắng thực hiện phép chia
    except ZeroDivisionError:
        print("division by zero!")  # Nếu có lỗi chia cho 0 thì in ra thông báo
    else:
        print("result is", result)  # Nếu hoàn thành được phép chia thì in ra kết quả
    finally:
        print("executing finally clause")  # Câu lệnh luôn thực thi vào cuối khối lệnh


divide(2, 1)  # Chia thành công nên in ra kết quả và thực thi câu lệnh luôn chạy
# result is 2.0
# executing finally clause

divide(2, 0)  # Có lỗi chi cho 0 nên in ra thông báo và thực thi câu lệnh luôn chạy
# division by zero!
# executing finally clause

divide(
    "2", "1"
)  # Có lỗi chia hai str chưa được xử lí nên thực thi câu lệnh luôn chạy và ném ra exception
# executing finally clause
# Traceback (most recent call last):
# TypeError: unsupported operand type(s) for /: 'str' and 'str'
