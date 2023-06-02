import struct


def Demo():
    with open(
        input("Đường dẫn file muốn đọc: "),
        "rb",
    ) as f:
        data = f.read(16)  # Đọc 16 bytes từ file
    print(len(data))
    fields = struct.unpack(
        "<IIIHH", data[:16]
    )  # unpack với kiểu <IIIHH cho kiểu 16 bytes
    print(fields)
