#!/usr/bin/env python
# coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://www.google.com/search?q={}+site%3Aqconcursos.com&client=opera-gx&hs=CMn&sxsrf=AOaemvIBcmNuKRLNV6jMC7oP7KB7tEmSaA%3A1635740820972&ei=lGx_YdDSOvPe1sQP_pmiwAk&oq=Q1837108+s&gs_lcp=Cgdnd3Mtd2l6EAMYADIECCMQJzoKCCMQrgIQsAMQJ0oECEEYAVCcF1jcHWCLKGgBcAB4AIABd4gBzwKSAQMwLjOYAQCgAQHIAQHAAQE&sclient=gws-wiz")

def selenium_search(id,driver):
   
   
    url = "https://www.google.com/search?q={}+site%3Aqconcursos.com&client=opera-gx&hs=CMn&sxsrf=AOaemvIBcmNuKRLNV6jMC7oP7KB7tEmSaA%3A1635740820972&ei=lGx_YdDSOvPe1sQP_pmiwAk&oq=Q1837108+s&gs_lcp=Cgdnd3Mtd2l6EAMYADIECCMQJzoKCCMQrgIQsAMQJ0oECEEYAVCcF1jcHWCLKGgBcAB4AIABd4gBzwKSAQMwLjOYAQCgAQHIAQHAAQE&sclient=gws-wiz".format(id)
    driver.get(url)
    driver.find_element_by_class_name("LC20lb").click()


# In[3]:

while True:
    import os
    import shutil
    import pandas as pd
    import re


    # In[4]:



    source_folder = r"."
    destination_folder = os.getcwd() + '\\'

    # fetch all files
    for file_name in os.listdir(source_folder):
        # construct full file path
        source = source_folder + file_name
        destination = destination_folder + file_name
        # copy only files
        if os.path.isfile(source):
            if os.path.exists (destination):
                print ('não copiou pq já existe', file_name)
            else:
                shutil.copy(source, destination)
                print('copiado', file_name)


    # In[5]:


    df_questoes_similaridade = pd.read_csv ('questao_falta_catalogar_similaridade.csv')
    df_questoes_similaridade


    # In[6]:


    df_questoes_comentario = pd.read_csv ('q_falta_catalogar.csv')


    # In[7]:


    df_questoes_comentario


    # In[8]:


    df_questoes_final = df_questoes_comentario.drop(['Unnamed: 0','QuestãoN','1','Comentario'],axis= 1)


    # In[9]:


    df_questoes_final= df_questoes_final.rename(columns={'referencia_final':'referencia_comentario'})


    # In[10]:


    df_questoes_final


    # In[11]:


    df_questoes_similaridade = df_questoes_similaridade.drop(['Unnamed: 0','questão pesquisada'],axis=1)


    # In[12]:


    df_questoes_similaridade


    # In[13]:


    df_questoes_final = df_questoes_final.join(df_questoes_similaridade)


    # In[14]:


    df_questoes_final


    # In[15]:


    df_questoes_final.columns


    # In[16]:


    df_questoes_final


    # In[17]:


    endresultado = os.getcwd() + '/resultado/'
    print(endresultado)
    if not os.path.exists(endresultado):
        os.makedirs ('resultado')


    if os.path.isfile(endresultado+'resultado.csv'):
        df_resultado = pd.read_csv (endresultado+'resultado.csv')
        print ('df_resultado foi carregado do arquivo já salvo')
    else:
        df_resultado = pd.DataFrame (columns=['IndQconc', 'Assuntos', 'Ano', '5', 'Orgao', 'Cargo', 'Questão', 'Tipo','gabarito', 'comando', 'texto item'])
        df_resultado.to_csv (endresultado+'resultado.csv', index=False)
        print ('criado o df_resultado')


    if os.path.isfile(endresultado+'falta_catalogar.csv'):
        df_falta_catalogar = pd.read_csv (endresultado+'falta_catalogar.csv')
        print ('df_falta_catalogar foi carregado do arquivo já salvo')
    else:
        df_falta_catalogar =pd.read_csv (os.getcwd() + '/'+'falta_catalogar_final.csv')
        df_falta_catalogar.to_csv (endresultado+'falta_catalogar.csv',index=False)
        print ('criado o df_falta_catalogar')

    if os.path.isfile(endresultado+'verificar_depois.csv'):
        df_verificar_depois = pd.read_csv (endresultado+'verificar_depois.csv')
        print ('df_verificar_depois foi carregado do arquivo já salvo')
    else:
        df_verificar_depois = pd.DataFrame (columns=[df_questoes_final.columns])
        df_verificar_depois.to_csv (endresultado+'verificar_depois.csv', index=False)
        df_verificar_depois = pd.read_csv (endresultado+'verificar_depois.csv')
        print ('criado o df_verificar_depois')


    # In[18]:


    df_lei = pd.read_csv ('CFcsvtudolei.csv')


    # In[19]:


    df_lei


    # In[20]:


    def procura_texto (df_lei,endereço):
        resultado = df_lei.Texto.where(df_lei.endereço == endereço)
        resultado = resultado.dropna()
        resultado = resultado.values
        return (resultado[0])


    # In[21]:


    df_falta_catalogar.columns


    # In[22]:


    def botoes_comentario (linha_questao,df_lei):
        listabotoes_coment =[]
        aux_listacoment = eval(linha_questao.referencia_comentario.values[0])
        if aux_listacoment:
            for item in aux_listacoment:
                listabotoes_coment.append([item,procura_texto(df_lei,item)])
        return (listabotoes_coment)

        


    # In[23]:


    def botoes_top10 (linha_questao):
        listabotoes_top10 =[]
        for i in range (1,11):
            listabotoes_top10.append ([linha_questao['endereço'+str(i)][0],linha_questao['resultado'+str(i)][0]])
        return (listabotoes_top10)


    # In[24]:


    def pega_linha1 (df_falta_catalogar):
        primeiralinha = df_falta_catalogar.head(1)
        texto_item =primeiralinha['texto item'][0]
        bot_comentario = botoes_comentario (primeiralinha,df_lei)
        bot_top10 = botoes_top10 (primeiralinha)
        return (texto_item,bot_comentario,bot_top10)


    # In[25]:


    texto_item, bot_comentario,bot_top10 = pega_linha1 (df_falta_catalogar)


    # In[26]:



    # print (texto_item)
    # print ('-'*30)
    # print (bot_comentario)
    # print ('-'*30)
    # print (bot_top10)
    # print ('-'*30)
    # print (bot_top10[1])


    # In[27]:


    def botao_passar (df_falta_catalogar,df_verificar_depois,end_pasta_versao,janela):
        df_falta_catalogar.head(1)
        df_verificar_depois= df_verificar_depois.append(df_falta_catalogar.head(1))
        df_falta_catalogar.drop(df_falta_catalogar.head(1).index,axis=0,inplace= True)
        df_verificar_depois.to_csv(end_pasta_versao+'verificar_depois.csv',index=False)
        df_falta_catalogar.to_csv(end_pasta_versao+'falta_catalogar.csv',index=False)
        refresh(janela)

        return (df_verificar_depois)


    # In[28]:


    # df_verificar_depois = botao_passar (df_falta_catalogar,df_verificar_depois,endresultado)


    # In[29]:


    df_falta_catalogar


    # In[30]:


    df_verificar_depois


    # In[31]:


    df_falta_catalogar


    # Botão Pesquisar

    # In[32]:


    dfart = pd.read_csv (r'CFcsvart.csv')
    dfniv2 = pd.read_csv (r'CFcsvniv2.csv')
    dfniv3 = pd.read_csv (r'CFcsvniv3.csv')
    dfniv4 = pd.read_csv (r'CFcsvniv4.csv')
    df_solei  = pd.read_csv(r'CFcsvtudolei.csv')


    # In[33]:


    artigo = re.compile (r"[a,A]rt.?\s?([0-9]{1,3})\s?-?[A-Z]?", flags= re.IGNORECASE)
    artigopesq = re.compile (r'\bart\.?(?:igo)?\b.*?([0-9]{1,3})',flags= re.IGNORECASE)
    paragrafo1 = re.compile (r'§\s*([0-9][0-9]?|.nico)',flags= re.IGNORECASE)
    paragrafo2 = re.compile (r'p[a.]?(?:r.grafo)?\s*([0-9][0-9]?)',flags= re.IGNORECASE)
    punico = re.compile (r'\bp.?(?:r.grafo)?\s*[u,ú](?:nico)?\b',flags= re.IGNORECASE)
    inciso = re.compile (r"\s?([LVIX]{1,7})")
    alinea1 = re.compile (r'al.nea.*?\b([a-z])\b',flags= re.IGNORECASE)
    alinea2 = re.compile (r"['\"]([a-z])['\"]")


    # In[34]:


    def porvalor (valor,df_tratado_por_indice): #no caso de artigo usar o df com todos os artigos
            valor = str(valor)
            resultado = df_tratado_por_indice.index.where(df_tratado_por_indice.end == valor)
            resultado = resultado.dropna()
            try:
                    indice = resultado[0] #
                    return (int(indice))
            except:
                    return("")
                    
    def verificaproximodf (indice,df_baixo):
        colunas = df_baixo.columns
        colunasdesejadas = 'art','niv2','niv3','niv4'
        for coluna in colunas:
            if coluna not in colunasdesejadas:
                df_baixo= df_baixo.drop ([coluna],axis=1)
        colunaanterior = df_baixo.iloc[:,-1].name
        df_resultado = df_baixo[colunaanterior].where(df_baixo[colunaanterior] == indice)
        df_resultado = df_resultado.dropna()
        df_resultado
        return (df_resultado.size > 0)

    def niv2porindice (indiceart,dfniv2): 
        indiceart = int(indiceart)
        resultado = pd.DataFrame (columns=['Texto'])
        resultado['Texto'] = dfniv2['Texto'].where(dfniv2.art==indiceart)
        resultado['end'] = dfniv2['end'].where(dfniv2.art==indiceart)
        resultado['endereço'] = dfniv2['endereço'].where(dfniv2.art==indiceart)
        resultado = resultado.dropna()
        if resultado.size == 0:
            resultado = ""
        return (resultado)
    def niv3porindice (indiceart,dfniv3):
        indiceart = int(indiceart)
        resultado = pd.DataFrame (columns=['Texto'])
        resultado['Texto'] = dfniv3['Texto'].where(dfniv3.niv2==indiceart)
        resultado['end'] = dfniv3['end'].where(dfniv3.niv2==indiceart)
        resultado['endereço'] = dfniv3['endereço'].where(dfniv3.niv2==indiceart)
        resultado = resultado.dropna()
        if resultado.size == 0:
            resultado = ""
        return (resultado)
    def niv4porindice (indiceart,dfniv4):
        indiceart = int(indiceart)
        resultado = pd.DataFrame (columns=['Texto'])
        resultado['Texto'] = dfniv4['Texto'].where(dfniv4.niv3==indiceart)
        resultado['end'] = dfniv4['end'].where(dfniv4.niv3==indiceart)
        resultado['endereço'] = dfniv4['endereço'].where(dfniv4.niv3==indiceart)
        resultado = resultado.dropna()
        if resultado.size == 0:
            resultado = ""
        return (resultado)
    def achaart (texto):
        trecholei = artigo.search(texto)
        if trecholei is None:
            resultado =""
        else:
            resultado = trecholei.group(1)
        return resultado
    def paragrafocoment (texto):
        resultado = ""
        aux = paragrafo1.search (texto)
        if aux is not None:
            try:
                int (aux.group(1))
                resultado = aux.group(1)
            except:
                resultado = 'Parágrafo Único'
        aux = paragrafo2.search (texto)
        if aux is not None:
            resultado = aux.group(1)
        aux = punico.search (texto)
        if aux is not None:
            resultado = 'Parágrafo Único'
        return (resultado)
    def artcoment (texto):
        resultado = artigopesq.search (texto)
        if resultado is not None:
            resultado = resultado.group(1)
        else:
            resultado =""
        return (resultado)
    def incicoment (texto):
        resultado = inciso.search (texto)
        if resultado is not None:
            resultado = resultado.group(1)
        else:
            resultado =""
        return (resultado)
    def achaalinea (texto):
        aux1 =  alinea1.search(texto)
        aux2 = alinea2.search (texto)
        resultado = ""
        if aux1 is not None:
            resultado = aux1.group(1)
        elif aux2 is not None:
            resultado = aux2.group(1)
        return (resultado)
    def procuradf (textoprocurado, coluna):
        resultado =  coluna.where(coluna == textoprocurado).dropna()
        return (not resultado.empty)


    # In[35]:


    def bot_procurar (texto,dfart,dfniv2,dfniv3,dfniv4):
        resultado=""
        auxart = artcoment(texto)
        if auxart != "" and int(auxart) in dfart.index.values:
                indartigo = porvalor (auxart,dfart) #acha o indice do artigo
                if verificaproximodf (indartigo,dfniv2): #verifica se tem o nivel 2
                    auxniv2=""
                    df_pesq_niv2 = niv2porindice (indartigo,dfniv2) #retorna o nivel 2 do artigo achado
                    auxparagrafo = paragrafocoment (texto)
                    auxniv2 = auxparagrafo
                    if auxparagrafo != "":
                        tiponiv2 = "paragrafo"
                    if not procuradf (auxparagrafo, df_pesq_niv2['end']):
                        auxparagrafo = ""
                        auxniv2 = auxparagrafo
                        tiponiv2 =""
                    if auxparagrafo == "":
                        auxinciso = incicoment (texto)
                        auxniv2 = auxinciso
                        tiponiv2 = 'inciso'
                        if not procuradf (auxinciso, df_pesq_niv2['end']):
                            auxinciso = ""
                            auxniv2 = auxinciso
                            tiponiv2 =""
                    if auxniv2 =="":
                        resultado = dfart.endereço[indartigo]
                    else:
                        indniv2 = porvalor (auxniv2,df_pesq_niv2)
                        df_pesq_niv3 = niv3porindice (indniv2, dfniv3)
                        if verificaproximodf (indniv2,dfniv3):
                            if tiponiv2 == 'paragrafo':
                                auxinciso = incicoment (texto)
                                if  not  procuradf (auxinciso, df_pesq_niv3['end']):
                                    auxinciso =""
                                if auxinciso =="":
                                    resultado = dfniv2.endereço[indniv2]
                                else:
                                    indniv3 = porvalor (auxinciso,df_pesq_niv3)
                                    if verificaproximodf (indniv3,dfniv4):
                                        df_pesq_niv4 = niv4porindice (indniv3,dfniv4)
                                        auxalinea = achaalinea (texto)
                                        if not procuradf (auxalinea, df_pesq_niv4['end']):
                                            auxalinea = ""
                                        if auxalinea == "":
                                            resultado= dfniv3.endereço[indniv3]
                                        else:
                                            indniv4 = porvalor (auxalinea, df_pesq_niv4)
                                            resultado = dfniv4.endereço[indniv4]
                                    else:
                                        resultado = dfniv3.endereço[indniv3]
                            else:
                                df_pesq_niv3 = niv3porindice (indniv2, dfniv3)
                                auxalinea = achaalinea (texto)
                                if not procuradf (auxalinea, df_pesq_niv3['end']):
                                    auxalinea = ""
                                if auxalinea == "":
                                    resultado= dfniv2.endereço[indniv2]
                                else:
                                    indniv3 = porvalor (auxalinea, df_pesq_niv3)
                                    resultado = dfniv3.endereço[indniv3]

                        else:
                            resultado = dfniv2.endereço[indniv2]       
                else:
                    if indartigo !="":
                        resultado = dfart.endereço[indartigo]
        else:
            resultado =  ("")
        return (resultado)


    # In[36]:






    # In[37]:


    def botao_salva (df_resultado,df_falta_catalogar, endereco ):
        colunas_desejadas = df_resultado.columns.values
        linha_desejada = df_falta_catalogar.head(1)
        for coluna in linha_desejada.columns.values:
            if coluna not in colunas_desejadas:
                linha_desejada = linha_desejada.drop(coluna, axis=1)
        linha_desejada['endereco'] = endereco
        return (linha_desejada)


    # In[38]:


    #>>>> ALTERAR <<<<<<
    linha_questao = botao_salva (df_resultado,df_falta_catalogar,'cf88,1,2,,,11,152,,')


    # In[39]:


    linha_questao


    # In[40]:


    def telaconfirmação (linha_questao):
        endereço =[]
        comando = linha_questao.comando.values[0]
        texto_item = linha_questao['texto item'].values[0]
        endereço.append ( linha_questao.endereco.values[0])
        endereço.append (procura_texto (df_lei,linha_questao.endereco.values[0]))

        return (comando,texto_item,endereço)


    # In[41]:


    comando,texto_item,end = telaconfirmação (linha_questao)
    end


    # In[42]:


    def botao_sim (linha_questao,df_falta_catalogar, df_resultado,end_pasta_resultado):
        df_falta_catalogar.drop(df_falta_catalogar.head(1).index, axis=0, inplace= True)
        df_resultado= df_resultado.append(linha_questao)
        df_falta_catalogar.to_csv(end_pasta_resultado+'falta_catalogar.csv',index=False)
        df_resultado.to_csv(end_pasta_resultado+'resultado.csv',index=False)
        return(df_resultado)


    # In[43]:


    ### BOTAO CONFIRMAR ###
    # df_resultado = botao_sim (linha_questao,df_falta_catalogar,df_resultado,endresultado)


    # In[44]:


    df_resultado


    # In[ ]:





    # In[54]:


    from os import stat
    from posixpath import commonpath
    from tkinter import *
    import time
    import pandas as pd

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
        IndQconc = linha_questao['IndQconc'].values[0]
        
        endereço.append ( linha_questao.endereco.values[0])
        endereço.append (procura_texto (df_lei,linha_questao.endereco.values[0]))

        return (comando,texto_item,endereço,IndQconc)

    # def telaconfirmação (linha_questao):
    #         endereço =[]
    #         comando = linha_questao.comando.values[0]
    #         texto_item = linha_questao['texto item'].values[0]
    #         endereço.append ( linha_questao.endereco.values[0])
    #         endereço.append (procura_texto (df_lei,linha_questao.endereco.values[0]))

    #         return (comando,texto_item,endereço)


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
        
        cmd,txt_it,endereco_confirma,IndQconc_intercafe = telaconfirmação(linha_questao)


        win = Toplevel()
        win.wm_title("Window")
        win.geometry("1350x750")


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


    def find_e_btn_func(texte):

        texto_resultado = bot_procurar (e.get(),dfart,dfniv2,dfniv3,dfniv4)
        
        label_result = Label(text=texto_resultado, wraplength=800)
        label_result.grid(column=0, row=100, columnspan=5)

        btn_pesquisa = Button(text = "Salvar",command= salvar_btn_func(texto_resultado,df_resultado))

        btn_pesquisa.grid(column=6, row=100, columnspan=5)

        

        # CRIAR UM BOTÃO PARA ENVIAR END

            


    def sel():
        
        salvar_btn["state"] = ACTIVE

    def refresh(self):
        self.destroy()
        

    linha_questao = botao_salva (df_resultado,df_falta_catalogar,'cf88,1,2,,,11,152,,')
    cmd,txt_it,endereco_confirma,IndQconc_interface = telaconfirmação(linha_questao)

    selenium_search(IndQconc_interface,driver)

    var = StringVar()

    label_id = Label(root, text="Texto item : " + str(txt_it),wraplength=350,background="#3F3F3F",fg="white")

    pass_btn = Button(root, text="PASSAR", command=lambda: botao_passar (df_falta_catalogar,df_verificar_depois,endresultado,root),fg="#fff",bg="#3F3F3F")

    salvar_btn = Button(root, text="Salvar", state=DISABLED,
                        command=lambda: salvar_btn_func(var.get(),df_resultado),fg="#fff",bg="#3F3F3F")

    e = Entry(root)

    find_e_btn = Button(root, text="procurar", command=lambda: find_e_btn_func(var.get()),fg="#fff",bg="#3F3F3F")

    master_frame = LabelFrame(root)


    master_frame.grid(row =1, column=0, columnspan=10) 

    def on_configure(event):
        # update scrollregion after starting 'mainloop'
        # when all widgets are in canvas
        btns_frame.configure(scrollregion=btns_frame.bbox('all'))

    btns_frame = Canvas(master_frame,width=1300,height=500,background="#3F3F3F")

    btns_frame.pack(side=LEFT)


    scrollbar = Scrollbar(master_frame, command=btns_frame.yview)
    scrollbar.pack(side=LEFT, fill='y')

    btns_frame.configure(yscrollcommand = scrollbar.set)

    # update scrollregion after starting 'mainloop'
    # when all widgets are in canvas
    btns_frame.bind('<Configure>', on_configure)

    frame = Frame(btns_frame,background="#3F3F3F")
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
        globals()[f'result{i}'] = LabelFrame(frame, pady=5, padx=5,background="#3F3F3F")

        label_frame = Label(globals()[f'result{i}'], text=bot_top10[i][1], wraplength=300,fg="#fff",background="#3F3F3F")
        label_frame.pack()

        globals()[f"R{i}"] = Radiobutton(globals()[f'result{i}'],variable=var,
                                            value=bot_top10[i][0], command=sel,background="#3F3F3F")
        globals()[f"R{i}"].pack()
        globals()[f'result{i}'].grid(row=row_frame, column=0+set_column)

    for i in range(len(bot_comentario)): 
        if i ==0:
            set_column =-1
        set_column += 1
        if i % 4 == 0 and i >= 4:
            row_frame += 1
            set_column = 0
        globals()[f'result_coment{i}'] = LabelFrame(frame, pady=15, padx=5,background="#3F3F3F",text="Bot_comentario",fg = "white")

        label_frame_comment = Label(globals()[f'result_coment{i}'], text=bot_comentario[i][1], wraplength=300,fg="#fff",background="#3F3F3F")
        label_frame_comment.pack()

        globals()[f"R_coment{i}"] = Radiobutton(globals()[f'result_coment{i}'],variable=var,
                                            value=bot_comentario[i][0], command=sel,background="#3F3F3F")
        globals()[f"R_coment{i}"].pack()
        globals()[f'result_coment{i}'].grid(row=row_frame+4, column=0+set_column)


    e.grid(row=99, column=1)

    root.geometry("1350x750")

    root.configure(background='#3F3F3F')

    root.mainloop()




