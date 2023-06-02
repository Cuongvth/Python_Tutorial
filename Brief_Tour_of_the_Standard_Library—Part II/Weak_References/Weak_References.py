import weakref, gc
import A


class Weak_References:
    a = A.A("fake")
    d = weakref.WeakValueDictionary()
    d["primary"] = a

    @classmethod
    def Demo(cls):
        cls.a = A.A(input("Nhập giá trị: "))
        cls.d[
            "primary"
        ] = (
            cls.a
        )  # Gán lại a cho d["primary"] bởi vì WeakValueDictionary không nhận ra sự thay đổi và vẫn giữ một tham chiếu yếu đến đối tượng ban đầu

    @classmethod
    def Demo2(cls):
        try:
            del cls.a
        except Exception as ex:
            print(ex.args)

    @classmethod
    def Demo4(cls):
        try:
            print("Giá trị", cls.d["primary"])
        except Exception as ex:
            print(ex.args)


def Demo3():
    gc.collect()
