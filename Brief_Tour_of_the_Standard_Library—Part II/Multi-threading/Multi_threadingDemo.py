import AsyncZip


def Demo():
    background = AsyncZip.AsyncZip(
        input("Đường dẫn file muốn thêm: "),
        "W:\Git\Python_Tutorial\Brief_Tour_of_the_Standard_Library—Part II\Multi-threading\Photo.rar",
    )
    background.start()
    print("Vẫn tiếp tục chép ảnh dưới nền")
    background.join()
    print("Hoàn thành chép ảnh")
