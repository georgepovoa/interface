from os import stat
from posixpath import commonpath
from tkinter import *
import time
import pandas as pd




def refresh(self):
    self.destroy()
    self.__init__()
    print(time.now)


root = Tk()


id = 12312


def pass_btn_func(id, root):
    refresh(root)


def salvar_btn_func(id, end):
    def salvar(id, win):
        print("ASD")
        print(id)
        win.destroy()

    win = Toplevel()
    win.wm_title("Window")
    win.geometry("950x650")

    l_id = Label(win, text=f"ID QUESTAO : {id}")
    l_id.grid(row=0, column=0)

    l_comando = Label(win, text=f"Comando : {id}")
    l_comando.grid(row=1, column=0)

    l_texto_item = Label(win, text=f"Texto item : {id}")
    l_texto_item.grid(row=2, column=0)

    l_endereco = Label(win, text=f"Endereço : {id}")
    l_endereco.grid(row=3, column=0)

    l_endereco = Label(win, text="Salvar Questão ? ")
    l_endereco.grid(row=4, column=0)

    s = Button(win, text="Sim", command=win.destroy)
    s.grid(row=5, column=0)

    n = Button(win, text="Não", command=win.destroy)
    n.grid(row=5, column=1)

    win.bind('<Return>', lambda e: salvar(id, win))

    
    


def resultado_texto():
    return str(var.get())*500


def find_e_btn_func():
    label_result = Label(text=resultado_texto(), wraplength=800)
    label_result.grid(column=0, row=100, columnspan=5)


def sel():
    print(var.get())
    salvar_btn["state"] = ACTIVE


var = StringVar()

label_id = Label(root, text="id : " + str(id))

pass_btn = Button(root, text="PASSAR", command=lambda: pass_btn_func(id, root))

salvar_btn = Button(root, text="Salvar", state=DISABLED,
                    command=lambda: salvar_btn_func(id, var.get()))

e = Entry(root)

find_e_btn = Button(root, text="procurar", command=find_e_btn_func)

label_id.grid(row=0, column=0)
pass_btn.grid(row=0, column=1)
salvar_btn.grid(row=0, column=2)
find_e_btn.grid(row=99, column=2)
row_frame = 1
set_column = -1
for i in range(8):
    set_column += 1
    if i % 4 == 0 and i >= 4:
        row_frame += 1
        set_column = 0
    globals()[f'frame{i}'] = LabelFrame(
        root, text="This is my frame " + str(i), pady=5, padx=5)

    label_frame = Label(
        globals()[f'frame{i}'], text="TESTE TESTE "*i*5, wraplength=250)
    label_frame.pack()

    globals()[f"R{i}"] = Radiobutton(globals()[f'frame{i}'],
                                     text=f"{i}", variable=var, value=i, command=sel)
    globals()[f"R{i}"].pack()
    globals()[f'frame{i}'].grid(row=row_frame, column=0+set_column)


e.grid(row=99, column=1)


root.geometry("950x650")


root.mainloop()
