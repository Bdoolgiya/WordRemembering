import tkinter as tk
from tkinter.ttk import *
from functions import *
import os


class window_main:

    def __init__(self, master):

        self.name = None
        self.label_showlist_info = None
        self.text_findlist_info = None
        self.btn_findlist_info = None
        self.toplevel1 = None
        self.add_title = ""
        self.add_word = ""
        self.add_mean = ""
        self.master = master

        self.name_list = open_file()
        self.info_img = tk.PhotoImage(file="info_btn_image30x30.png")

        self.notebook = Notebook(master, width=800, height=600, takefocus=True)
        self.notebook.pack()

        self.is_opened_window = False

        # ---------------- "단어 추가" 프레임 ------------------

        self.frame_add_word = tk.Frame(master)
        self.frame_add_word.pack()
        self.notebook.add(self.frame_add_word, text="단어 추가")

        self.label_title_addword = tk.Label(self.frame_add_word)
        self.label_title_addword.configure(text="단어장 추가하기", font=("굴림", 40))
        self.label_title_addword.place(relx=0.26, rely=0.05)

        self.label_tuto_addword = tk.Label(self.frame_add_word)
        self.label_tuto_addword.configure(text='입력 단어가 추가될 "단어장" 제목 쓰기\n\n\n\n\n\n'
                                               '"단어" 항목에 추가하고 싶은 단어 쓰기\n\n\n\n\n\n'
                                               '"의미" 항목에 추가한 단어의 의미 쓰기',
                                          font=("굴림", 15))
        self.label_tuto_addword.place(relx=0.05, rely=0.25)

        self.text_title_addword = tk.Text(self.frame_add_word)
        self.text_title_addword.configure(width=30, height=1, font=("굴림", 18))
        self.text_title_addword.place(relx=0.05, rely=0.32)

        self.text_word_addword = tk.Text(self.frame_add_word)
        self.text_word_addword.configure(width=30, height=1, font=("굴림", 18))
        self.text_word_addword.place(relx=0.05, rely=0.53)

        self.text_mean_addword = tk.Text(self.frame_add_word)
        self.text_mean_addword.configure(width=30, height=1, font=("굴림", 18))
        self.text_mean_addword.place(relx=0.05, rely=0.74)

        self.btn_showinfo_addword = tk.Button(self.frame_add_word)
        self.btn_showinfo_addword.place(relx=0.95, rely=0.93)
        self.btn_showinfo_addword.configure(image=self.info_img, width=30, height=30, command=self.cmd_make_infowin)

        self.label_tuto2_addword = tk.Label(self.frame_add_word, text="모두 입력 후\n아래 버튼을 클릭", font=("굴림", 20))
        self.label_tuto2_addword.place(relx=0.65, rely=0.35)

        self.btn_addword_addword = tk.Button(self.frame_add_word, padx=5, pady=3, text="추가", command=self.cmd_add_word,
                                             width=12, height=5, font=("굴림", 20))
        self.btn_addword_addword.place(relx=0.65, rely=0.48)

        self.label_showstate_addword = tk.Label(self.frame_add_word, font=("굴림", 20), relief="solid", bd=3,
                                                anchor="w", justify="left", bg="white", width=42, height=2, fg="black")
        self.label_showstate_addword.place(relx=0.05, rely=0.85)

        # ---------------- "단어장 편집" 프레임 ------------------

        self.frame_edit_word = tk.Frame(master)
        self.frame_edit_word.pack()
        self.notebook.add(self.frame_edit_word, text="단어장 편집")

        self.label_title_editword = tk.Label(self.frame_edit_word)
        self.label_title_editword.configure(text="단어장 편집하기", font=("굴림", 40))
        self.label_title_editword.place(relx=0.26, rely=0.05)

        self.btn_dellist_editword = tk.Button(self.frame_edit_word)
        self.btn_dellist_editword.configure(text="단어장 삭제하기", font=("굴림", 15), padx=3, width=20, height=3)
        self.btn_dellist_editword.place(relx=0.02, rely=0.2)

        self.btn_editword_editword = tk.Button(self.frame_edit_word)
        self.btn_editword_editword.configure(text="단어 편집하기", font=("굴림", 15), padx=3, width=20, height=3)
        self.btn_editword_editword.place(relx=0.35, rely=0.2)

        self.btn_editlist_editword = tk.Button(self.frame_edit_word)
        self.btn_editlist_editword.configure(text="단어장 바꾸기", font=("굴림", 15), padx=3, width=20, height=3)
        self.btn_editlist_editword.place(relx=0.68, rely=0.2)

        self.label_divarea_editword = tk.Label(self.frame_edit_word)
        self.label_divarea_editword.configure(text="__________________________________________________________________"
                                                   "__________________________________________________________________"
                                                   "_______________________")
        self.label_divarea_editword.place(relx=0.01, rely=0.33)

    def cmd_make_infowin(self):
        self.toplevel1 = tk.Toplevel(self.master)
        self.toplevel1.geometry("300x200")

        self.btn_findlist_info = tk.Button(self.toplevel1)
        self.btn_findlist_info.configure(text="단어장 존재여부 확인하기", padx=3, pady=2, font=("굴림", 15),
                                         command=self.cmd_find_list)
        self.btn_findlist_info.place(relx=0.01, rely=0.05)

        self.text_findlist_info = tk.Text(self.toplevel1)
        self.text_findlist_info.configure(font=("굴림", 12), width=34, height=1)
        self.text_findlist_info.place(relx=0.01, rely=0.35)

        self.label_showlist_info = tk.Label(self.toplevel1)
        self.label_showlist_info.configure(text="", font=("굴림", 12), width=30, height=2, anchor="w",
                                           justify="left", bg="white", fg="black", relief="solid")
        self.label_showlist_info.place(relx=0.01, rely=0.6)

    def cmd_add_word(self):
        self.add_word = self.text_word_addword.get('1.0', tk.END).strip().replace("  ", " ")
        self.add_mean = self.text_mean_addword.get('1.0', tk.END).strip().replace("  ", " ")
        self.add_title = self.text_title_addword.get('1.0', tk.END).strip()

        if (self.add_mean or self.add_title or self.add_word) == "":
            self.label_showstate_addword.configure(text="값이 입력되지 않은 항목이 있습니다\n모든 항목을 입력해 주세요",
                                                   fg="red")

        elif "," in (self.add_mean or self.add_title or self.add_word):
            self.label_showstate_addword.configure(text='항목에 들어가면 안되는 문자(,)가 포함되어 있습니다\n'
                                                        '해당 문자를 제외하고 다시 입력해 주세요')

        else:
            if not os.path.exists("C:/word"):
                os.makedirs("C:/word")
            if os.path.exists(f"C:/word/{self.add_title}.txt"):
                self.label_showstate_addword.configure(text=f'존재하던 "{self.add_title}" 파일에\n'
                                                            f'"{self.add_word}"을 "{self.add_mean}"의 뜻으로 저장했습니다',
                                                       fg="black")
            else:
                self.label_showstate_addword.configure(text=f'"{self.add_title}" 파일을 생성하여\n'
                                                            f'"{self.add_word}"을 "{self.add_mean}"의 뜻으로 저장했습니다',
                                                       fg="black")

            with open("C:/word/{}.txt".format(self.add_title), "+a") as f:
                f.write(f'{self.add_word},{self.add_mean}\n')

        self.name_list = open_file()

    def cmd_find_list(self):
        self.name = self.text_findlist_info.get("1.0", tk.END)
        if self.name in self.name_list:
            self.label_showlist_info.configure(text=f'"{self.name}" 단어장은 존재합니다')
        else:
            self.label_showlist_info.configure(text=f'"{self.name}" 단어장은 존재하지 않습니다')

    def cmd_open_info(self):
        pass

    def button_click(self):
        pass
        # If button is clicked, run this method and open window 2


class window_memorize:
    def __init__(self, master):
        self.master = master
        # create buttons,entries,etc

    def button_method(self):
        # run this when button click to close window
        self.master.destroy()


class window_info:
    def __init__(self, master):
        self.master = master
        self.files_list = open_file()

        self.fr_info = tk.Frame(self.master)

        self.btn_check_exist = tk.Button(self.fr_info).configure(text="확인하기", font=("굴림", 20), width=13, height=3)
        self.btn_check_exist.place(relx=0.04, rely=0.05)

        self.btn_syn = tk.Button(self.fr_info).configure(text="동기화하기", font=("굴림", 20), width=13, height=3)
        self.btn_syn.place(relx=0.52, rely=0.05)

    def cmd_check_exist(self):
        pass


def main():  # run
    root = tk.Tk()
    app = window_main(root)
    root.geometry("800x600")
    root.resizable(False, False)
    root.title("단어 외우기")
    root.mainloop()


if __name__ == '__main__':
    main()
