from string import Template
import time, os.path
import BatchRename


def Demo():
    t = Template("$HoTen hiện tại $Tuoi tuổi sống tại $DiaChi")
    print(
        t.substitute(
            HoTen=input("Nhập họ tên: "),
            Tuoi=int(input("Nhập tuổi: ")),
            DiaChi=input("Nhập địa chỉ: "),
        )
    )


def DemoOther():
    photofiles = ["img.jpg", "img.jpg", "img.jpg"]
    fmt = input(
        "Nhập format tên sau khi đổi với %d là ngày %n là số thứ tự %f là đuôi file:  "
    )
    t = BatchRename.BatchRename(fmt)
    date = time.strftime("%d%b%y")
    for i, filename in enumerate(photofiles):
        base, ext = os.path.splitext(filename)
        newname = t.substitute(d=date, n=i, f=ext)
        print("{0} --> {1}".format(filename, newname))
