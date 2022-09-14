import shutil


def replace_xlsx():
    shutil.copy("temp_xlsx/鸽宝歌单整理.xlsx", "鸽宝歌单整理.xlsx")


if __name__ == "__main__":
    replace_xlsx()
    print('Success copy')
