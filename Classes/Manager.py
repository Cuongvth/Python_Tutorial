from Employee import Employee


class Manager(Employee):
    def __init__(
        self,
        ten=None,
        tuoi=None,
        luong=None,
        thoiGianLamViec=None,
        lstNhanVien=None,
        thuong=None,
    ):
        super().__init__(ten, tuoi, luong, thoiGianLamViec)

        if lstNhanVien is None:
            self.lstNhanVien = []
            try:
                for i in range(int(input("Số lượng nhân viên: "))):
                    print("----------------")
                    print("Nhập nhân viên thứ", i + 1)
                    self.lstNhanVien.append(Employee())
                    print("----------------")
            except:
                pass
        else:
            self.lstNhanVien = lstNhanVien

        if thuong is None:
            try:
                self.thuong = int(input("Thưởng quản lí: "))
            except:
                self.thuong = 0
        else:
            self.thuong = thuong

    def Show(self):
        print("--------------------------------")
        print("Tên:", self.ten)
        print("Tuổi:", self.tuoi)
        print("Lương:", self.luong)
        print("Thời gian làm việc:", self.thoiGianLamViec)
        print("Thưởng:", self.thuong)
        print("Tổng lương:", self.tinhTongLuong())
        print("--------------------------------")

    def tinhTongLuong(self):
        return self.thoiGianLamViec * self.luong + self.thuong

    def toJson(self):
        return {
            "ten": self.ten,
            "tuoi": self.tuoi,
            "luong": self.luong,
            "thoiGianLamViec": self.thoiGianLamViec,
            "lstNhanVien": [i.toJson() for i in self.lstNhanVien],
            "thuong": self.thuong,
        }

    @classmethod
    def jsonToObject(cls, data):
        return Manager(
            data["ten"],
            data["tuoi"],
            data["luong"],
            data["thoiGianLamViec"],
            [Employee.jsonToObject(i) for i in data["lstNhanVien"]],
            data["thuong"],
        )
