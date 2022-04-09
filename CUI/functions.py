import os


def generate_word():  # 단어 파일을 생성하고 도중에 "C:/word" 디렉토리가 존재하지 않을 경우 생성
    word_list = []
    word_dictionary = {}
    n = int(input("입력받을 영단어의 갯수를 입력해주세요 : "))  # 입력받고 싶은 영단어의 갯수 입력

    for order_word in range(n):  # 앞서 입력받은 수만큼 영단어 입력
        word = input("{}번째 영단어를 입력해주세요 : ".format(order_word + 1))
        word_list.append(word)
        word_dictionary[word] = ""

    for order_mean in word_list:  # 앞서 입력받은 영단어들의 뜻 입력
        mean = input('"{}"의 뜻을 입력해주세요(뜻이 한 번에 여러개 입력될 때에는 ,로 구분해 주세요) : '.format(order_mean))
        mean = mean.replace(",", "/")
        word_dictionary[order_mean] = mean

    name = input("해당 단어장의 이름를 입력해주세요(.은 포함되면 안됩니다) : ")  # 단어장 이름 입력
    while "." in name:  # .이 이름 내에 포함되었을 경우 다시 입력
        name = input("해당 단어장의 이름에서 .을 제외하고 다시 이름을 입력하여 주세요 : ")

    try:  # 단어장을 만듦
        if not os.path.exists("C:/word"):
            os.makedirs("C:/word")
        with open("C:/word/{}.txt".format(name), "x") as f:
            for order_write in word_list:
                f.write("{},{}\n".format(order_write, word_dictionary[order_write]))

    except FileExistsError:  # 이미 같은 이름의 단어장이 있을 경우 확인을 받고 단어장을 덮어씌움
        bool_create = input("이미 존재하는 단어장입니다. 해당 단어장을 덮어씌우겠습니까?(y/n) : ")
        if bool_create == "y" or "Y":
            with open("C:/word/{}.txt".format(name), "w") as f:
                for order_write in word_list:
                    f.write("{},{}\n".format(order_write, word_dictionary[order_write]))


def open_file(name=""):  # 미리 만들어진 단어 파일에서 단어를 추출해내 딕셔너리 형식으로 반환
    word_dic = {}
    word_list = []

    name_list = []  # 현재 존재하는 단어장 리스트 형식으로 생성
    for filename in os.listdir("C:/word/"):
        ext = filename.split(".")[-1]
        name_head = filename.split(".")[0]
        if ext == "txt":
            name_list.append(name_head)

    if (name == "") or (name not in name_list):  # 열 파일 이름을 모르거나 존재하지 않는 파일 이름일 경우 이름 입력
        print("현재 단어장 : ", end="")
        for head in name_list:
            print(head, end="    ")
        print()
        name = input("열 단어장의 이름을 입력해주세요 : ")
        while name not in name_list:
            print("현재 단어장 : ", end="")
            for head in name_list:
                print(head, end="    ")
            print()
            name = input("존재하지 않는 단어장입니다. 현재 단어장 중 다시 입력해주세요 : ")

    with open("C:/word/{}.txt".format(name), 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            line = list(line.split(","))
            word_list.append(line[0])
            word_dic[line[0]] = line[1].replace("/", ",")

    return word_dic, word_list


def delete_file(name=""):  # 만들어져 있는 단어장 파일 삭제
    name_list = []  # 현재 존재하는 단어장 리스트 형식으로 생성
    for filename in os.listdir("C:/word/"):
        ext = filename.split(".")[-1]
        name_head = filename.split(".")[0]
        if ext == "txt":
            name_list.append(name_head)

    if (name == "") or (name not in name_list):  # 삭제할 파일 이름을 모르거나 존재하지 않는 파일 이름일 경우 이름 입력
        print("현재 단어장 : ", end="")
        for head in name_list:
            print(head, end="    ")
        print()
        name = input("삭제할 단어장의 이름을 입력해주세요 : ")
        while name not in name_list:
            print("현재 단어장 : ", end="")
            for head in name_list:
                print(head, end="    ")
            print()
            name = input("존재하지 않는 단어장입니다. 현재 단어장 중 다시 입력해주세요 : ")

    bool_judge = input("정말로 해당 단어장을 삭제하시겠습니까?(삭제할 단어장 : {})(y/n) : ".format(name))
    if bool_judge == ("y" or "Y"):  # 단어장 삭제
        os.remove("C:/word/{}.txt".format(name))

        name_list = []  # 현재 존재하는 단어장 리스트 형식으로 재생성
        for filename in os.listdir("C:/word/"):
            ext = filename.split(".")[-1]
            name_head = filename.split(".")[0]
            if ext == "txt":
                name_list.append(name_head)

        if name not in os.listdir("C:/word/"):  # 삭제 성공 확인
            print("단어장이 성공적으로 삭제되었습니다")
        else:
            print("단어장의 삭제에 실패하였습니다")


def modify_file(name=""):
    name_list = []  # 현재 존재하는 단어장 리스트 형식으로 생성
    for filename in os.listdir("C:/word/"):
        ext = filename.split(".")[-1]
        name_head = filename.split(".")[0]
        if ext == "txt":
            name_list.append(name_head)

    while (name == "") or (name not in name_list):  # 수정할 파일 이름을 모르거나 존재하지 않는 파일 이름일 경우 이름 입력
        print("현재 단어장 : ", end="")
        for head in name_list:
            print(head, end="    ")
        print()
        name = input("수정할 단어장의 이름을 입력해주세요 : ")
        while name not in name_list:
            print("현재 단어장 : ", end="")
            for head in name_list:
                print(head, end="    ")
            print()
            name = input("존재하지 않는 단어장입니다. 현재 단어장 중 다시 입력해주세요 : ")

    bool_modify = input("변경하고 싶은 것을 고르세요(스펠링/뜻/단어추가/단어삭제/단어장삭제) : ")  # 수행할 종류 선택
    while bool_modify != ("스펠링" or "뜻" or "단어추가" or "단어삭제" or "단어장삭제"):  # 잘못 골랐을 경우 계속 반복
        bool_modify = input("다음 보기 안에서 골라 다시 선택해주세요(스펠링/뜻/단어추가/단어삭제) : ")

    bool_continue = input("정말 다음 작업을 실행하겠습니까?({})(y/n) : ".format(bool_modify))
    if bool_continue == ("y" or "Y"):
        word_dic, word_list = open_file(name)

        if bool_modify == "스펠링":

            bool_change_1 = False

            while not bool_change_1:
                edited_lines = []

                print("현재 단어장 내에 있는 단어 : ", end="")
                for word in word_list:
                    print(word, end="   ")
                print()

                target_word = input("스펠링이 틀린 단어를 입력해주세요 : ")
                while target_word not in word_list:
                    target_word = input("존재하지 않는 단어입니다. 다시 입력해주세요 : ")
                modify_word = input("어떤 단어로 바꿀지 입력해주세요 : ")

                with open("C:/word/{}.txt".format(name), "r+") as f:

                    lines = f.readlines()
                    for line in lines:
                        if target_word == line.split(".")[0]:
                            edited_lines.append(modify_word + "," + line.split(",")[-1])
                            bool_change_1 = True
                        else:
                            edited_lines.append(line)

                if bool_change_1:
                    with open("C:/word/{}.txt".format(name), "w") as f:
                        f.writelines(edited_lines)

                bool_dec = input("작업이 종료되었습니다. 계속 해당 작업을 수행하시겠습니까?(y/n) : ")
                if bool_dec == ("y" or "Y"):
                    bool_change_1 = False

        if bool_modify == "뜻":

            bool_change_2 = False

            while not bool_change_2:
                edited_lines = []
                mean_list = []

                print("현재 단어장 내에 있는 뜻 : ", end="")
                for word in word_list:
                    print("{0}({1})".format(word_dic[word], word), end="    ")
                    mean_list.append(word_dic[word])

                target_mean = input("수정하고 싶은 뜻을 입력해주세요(뜻이 여러 개일 경우 위에 나타난 보기대로 전부 입력해주세요) : ")
                while target_mean not in mean_list:
                    target_mean = input("해당 뜻(들)은 단어장에 존재하지 않습니다. 다시 입력해주세요 : ")
                modify_mean = input("어떤 뜻으로 바꿀지 입력해주세요(여러 개일 경우 ,로 구분해주세요) : ")
                modify_mean = modify_mean.replace("/", ",")

                with open("C:/word/{}.txt".format(name), "r+") as f:
                    lines = f.readlines()
                    for line in lines:
                        if target_mean == line.split(".")[-1]:
                            edited_lines.append(line.split(".")[0] + "," + modify_mean)
                            bool_change_2 = True
                        else:
                            edited_lines.append(line)

                if bool_change_2:
                    with open("C:/word/{}.txt".format(name), "w") as f:
                        f.writelines(edited_lines)

                bool_dec = input("작업이 종료되었습니다. 계속 해당 작업을 수행하시겠습니까?(y/n) : ")

                if bool_dec == ("y" or "Y"):
                    bool_change_2 = False

        if bool_modify == "단어추가":

            bool_change_3 = False

            while not bool_change_3:

                word_add = input("추가하고 싶은 단어를 입력해주세요 : ")
                while word_add == "" or word_add in word_list:
                    word_add = input("공백으로 입력하였거나 이미 존재하는 단어입니다. 다시 입력해주세요 : ")
                mean_add = input("추가할 단어의 뜻을 입력해주세요(여러 개일 경우 ,로 구분해주세요) : ")
                while mean_add == "":
                    mean_add = input("공백으로 입력하였습니다. 다시 입력해주세요 : ")



