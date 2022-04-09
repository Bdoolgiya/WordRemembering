import os


def open_file():  # 파일
    name_list = []  # 현재 존재하는 단어장 리스트 형식으로 생성
    for filename in os.listdir("C:/word/"):
        ext = filename.split(".")[-1]
        name_head = filename.split(".")[0]
        if ext == "txt":
            name_list.append(name_head)

    return name_list

