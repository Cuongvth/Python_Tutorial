import os
import sys

sys.path.append(
    os.path.dirname(os.path.abspath(__file__)).split("Python_Tutorial")[0]
    + "Python_Tutorial"
)

from B import B
from C import C
from D import D
from Config.Config import path

while True:  # Lặp lại liên tục
    try:
        x = int(
            input("Please enter a number: ")
        )  # Khỏi tạo x lấy giá trị được nhập và ép kiểu về int
        break  # Sau khi lấy được giá trị cho x thì dừng vòng lặp
    except ValueError:  # Nếu xảy ra lỗi ValueError
        print("Oops!  That was no valid number.  Try again...")  # In ra thông báo lỗi

for cls in [B, C, D]:  # Lặp qua mảng [B, C, D]
    try:
        raise cls()  # Ném ra ngoại lệ được lặp qua
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")

try:
    raise Exception("spam", "eggs")  # Ném ra ngoại lệ với các đối số là "spam", "eggs"
except Exception as inst:  # Lấy ra ngoại lệ dưới đối tượng inst
    print(type(inst))
    print(inst.args)  # Các đối số của Exception được lưu trữ trong thuộc tính args
    print(inst)
    x, y = inst.args
    print("x =", x)
    print("y =", y)


try:
    f = open(path + "Errors_and_Exceptions\Handling_Exceptions\myfile.txt")
    s = f.readline()
    i = int(s.strip())
    print(i)
except OSError as err:
    print("OS error:", err)
except ValueError:
    print("Could not convert data to an integer.")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise

# Mở chế độ tương tác và chạy file với đối số là myfile.txt
# Output:
# myfile.txt has 1 lines
for arg in sys.argv[1:]:
    try:
        f = open(arg, "r")
    except OSError:
        print("cannot open", arg)
    else:
        print(arg, "has", len(f.readlines()), "lines")
        f.close()
