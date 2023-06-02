import logging


def Demo():
    type = int(
        input(
            "Nhập kiểu thông báo là 1-5 lần lượt tương ứng với debug, info, warning, error, critical: "
        )
    )
    if type == 1:
        logging.debug(input("Nhập nội dung thông báo: "))
    elif type == 2:
        logging.info(input("Nhập nội dung thông báo: "))
    elif type == 3:
        logging.warning(input("Nhập nội dung thông báo: "))
    elif type == 4:
        logging.error(input("Nhập nội dung thông báo: "))
    elif type == 5:
        logging.critical(input("Nhập nội dung thông báo: "))
    else:
        print("Nhập sai")
