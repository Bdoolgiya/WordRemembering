from functions import *
import tkinter as tk
from tkinter.ttk import *


class app:

    word_dic, word_list = open_file()

    def __init__(self):
        main_win = tk.Tk()
        main_win.geometry("800x600")
        main_win.resizable(False, False)

        notebook = Notebook(main_win, width=800, height=600, takefocus=True)
        notebook.pack()

        frame_add_word = tk.Frame(main_win)
        notebook.add(frame_add_word, text="단어장 추가")

        frame_edit_word = tk.Frame(main_win)
        notebook.add(frame_edit_word, text="단어장 편집")

        main_win.mainloop()


