from os import stat
from posixpath import commonpath
from tkinter import *
import pandas as pd
import os
import shutil



#### IPYNB ####




#### IPYNB ####




root = Tk()


def botao_salva (df_resultado,df_falta_catalogar, endereco ):
    colunas_desejadas = df_resultado.columns.values
    linha_desejada = df_falta_catalogar.head(1)
    for coluna in linha_desejada.columns.values:
        if coluna not in colunas_desejadas:
            linha_desejada = linha_desejada.drop(coluna, axis=1)
    linha_desejada['endereco'] = endereco
    return (linha_desejada)

def telaconfirmação (linha_questao):
    endereço =[]
    comando = linha_questao.comando.values[0]
    texto_item = linha_questao['texto item'].values[0]
    endereço.append ( linha_questao.endereco.values[0])
    endereço.append (procura_texto (df_lei,linha_questao.endereco.values[0]))

    return (comando,texto_item,endereço)


def pass_btn_func(id, root):
    pass

def telaconfirmação (linha_questao):
        endereço =[]
        comando = linha_questao.comando.values[0]
        texto_item = linha_questao['texto item'].values[0]
        endereço.append ( linha_questao.endereco.values[0])
        endereço.append (procura_texto (df_lei,linha_questao.endereco.values[0]))

        return (comando,texto_item,endereço)


def salvar_btn_func(end,df_resultado):
    def botao_sim (linha_questao,df_falta_catalogar, df_resultado,end_pasta_resultado,wind,root):
        df_falta_catalogar.drop(df_falta_catalogar.head(1).index, axis=0, inplace= True)
        df_resultado= df_resultado.append(linha_questao)
        df_falta_catalogar.to_csv(end_pasta_resultado+'falta_catalogar.csv',index=False)
        df_resultado.to_csv(end_pasta_resultado+'resultado.csv',index=False)
        wind.destroy() 

        l_id.update()
        l_texto_item.update()
        l_comando.update()


        refresh(root)
        return(df_resultado)

    
    linha_questao = botao_salva (df_resultado,df_falta_catalogar,end)
    
    cmd,txt_it,endereco_confirma = telaconfirmação(linha_questao)


    win = Toplevel()
    win.wm_title("Window")
    win.geometry("950x650")


    l_id = Label(win, text=f"Comando : {cmd}",wraplength=800)
    l_id.grid(row=0, column=0,pady=30)

    l_comando = Label(win, text=f"texto item : {txt_it}",wraplength=800)
    l_comando.grid(row=1, column=0,pady=30)


    l_texto_item = Label(win, text=f"endereco: {endereco_confirma[1]}",wraplength=800)
    l_texto_item.grid(row=2, column=0,pady=30)


    s = Button(win, text="Sim", command= lambda : botao_sim (linha_questao,df_falta_catalogar,df_resultado,endresultado,win,root))

    s.grid(row=5, column=0)

    n = Button(win, text="Não", command=win.destroy)
    n.grid(row=5, column=1)

    win.bind('<Return>', lambda e: botao_sim (linha_questao,df_falta_catalogar,df_resultado,endresultado,win,root))


def resultado_texto():
    return str(var.get())*500


def find_e_btn_func():
    label_result = Label(text=resultado_texto(), wraplength=800)
    label_result.grid(column=0, row=100, columnspan=5)


def sel():
    print(var.get())
    salvar_btn["state"] = ACTIVE

def refresh(self):
    self.destroy()
    os.popen("interface.ipynb")

linha_questao = botao_salva (df_resultado,df_falta_catalogar,'cf88,1,2,,,11,152,,')
cmd,txt_it,endereco_confirma = telaconfirmação(linha_questao)

var = StringVar()

label_id = Label(root, text="Texto item : " + str(txt_it),wraplength=350)

pass_btn = Button(root, text="PASSAR", command=lambda: pass_btn_func(id, root))

salvar_btn = Button(root, text="Salvar", state=DISABLED,
                    command=lambda: salvar_btn_func(var.get(),df_resultado))

e = Entry(root)

find_e_btn = Button(root, text="procurar", command=find_e_btn_func)

master_frame = LabelFrame(root)


master_frame.grid(row =1, column=0, columnspan=10) 

def on_configure(event):
    # update scrollregion after starting 'mainloop'
    # when all widgets are in canvas
    btns_frame.configure(scrollregion=btns_frame.bbox('all'))

btns_frame = Canvas(master_frame,width=1300,height=500)

btns_frame.pack(side=LEFT)


scrollbar = Scrollbar(master_frame, command=btns_frame.yview)
scrollbar.pack(side=LEFT, fill='y')

btns_frame.configure(yscrollcommand = scrollbar.set)

# update scrollregion after starting 'mainloop'
# when all widgets are in canvas
btns_frame.bind('<Configure>', on_configure)

frame = Frame(btns_frame)
btns_frame.create_window((0,0), window=frame, anchor='nw')

label_id.grid(row=0, column=0,columnspan=3)
pass_btn.grid(row=0, column=4,padx=25)
salvar_btn.grid(row=0, column=5,padx=25)
find_e_btn.grid(row=99, column=6,padx=25)
row_frame = 1
set_column = -1

for i in range(len(bot_top10)): 
    set_column += 1
    if i % 4 == 0 and i >= 4:
        row_frame += 1
        set_column = 0
    globals()[f'result{i}'] = LabelFrame(frame, pady=5, padx=5,)

    label_frame = Label(globals()[f'result{i}'], text=bot_top10[i][1], wraplength=300)
    label_frame.pack()

    globals()[f"R{i}"] = Radiobutton(globals()[f'result{i}'],variable=var,
                                        value=bot_top10[i][0], command=sel)
    globals()[f"R{i}"].pack()
    globals()[f'result{i}'].grid(row=row_frame, column=0+set_column)


e.grid(row=99, column=1)

root.geometry("1200x700")

root.mainloop()