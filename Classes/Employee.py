class Employee:
    def __init__(self, ten=None, tuoi=None, luong=None, thoiGianLamViec=None):
        if ten is None:
            self.ten = input("Tên nhân viên: ")
        else:
            self.ten = ten

        if tuoi is None:
            try:
                self.tuoi = int(input("Tuổi nhân viên: "))
            except:
                self.tuoi = 0
        else:
            self.tuoi = tuoi

        if luong is None:
            try:
                self.luong = int(input("Lương nhân viên: "))
            except:
                self.luong = 0
        else:
            self.luong = luong

        if thoiGianLamViec is None:
            try:
                self.thoiGianLamViec = int(input("Thời gian đã làm việc: "))
            except:
                self.thoiGianLamViec = 0
        else:
            self.thoiGianLamViec = thoiGianLamViec

    def Show(self):
        print("--------------------------------")
        print("Tên:", self.ten)
        print("Tuổi:", self.tuoi)
        print("Lương:", self.luong)
        print("Thời gian làm việc:", self.thoiGianLamViec)
        print("Tổng lương:", self.tinhTongLuong())
        print("--------------------------------")

    def tinhTongLuong(self):
        return self.thoiGianLamViec * self.luong

    def toJson(self):
        return {
            "ten": self.ten,
            "tuoi": self.tuoi,
            "luong": self.luong,
            "thoiGianLamViec": self.thoiGianLamViec,
        }

    @classmethod
    def jsonToObject(cls, data):
        return Employee(
            data["ten"], data["tuoi"], data["luong"], data["thoiGianLamViec"]
        )
