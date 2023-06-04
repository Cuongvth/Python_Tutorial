from decimal import Decimal


try:
    munber1 = Decimal(input("Nhập số thứ nhất: "))
    munber2 = Decimal(input("Nhập số thứ hai: "))
    print("Tổng: ", munber1 + munber2)
    print("Hiệu: ", munber1 - munber2)
    print("Tích: ", munber1 * munber2)
    print("Thương: ", munber1 / munber2)
except Exception as ex:
    print(ex)
