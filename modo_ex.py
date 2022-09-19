#!/usr/bin/env python
# coding: utf-8

# In[ ]:

#VAR

listEmpty = []
listFull = [1, 2, 3, 4, 5]

setEmpty = set ()
setFull = {1, 'dois', 3, 'quatro', 5, 'seis', 7}

tupleEmpty = ()
tupleFull = (1, 2, 3, 4, 5, 6, 7)

dicEmpty = {}
dicFull = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}


#FUNC LIST----------------------------------------------
def add_list():
    m1=0
    while m1 != '3':
        print('''
        --- ADD LIST ---
        1: Lista Vazia
        2: Lista Cheia
        3: Voltar
        ''')

        m1 = str(input("Escolha a sua opção: "))

        if m1 == '1':
            mx = 0
            while mx < 2:
                mx = valida_max()
            add_list_empty(mx)

        elif m1 == '2':
            mx = 0
            while mx < 2:
                mx = valida_max()
            add_list_full(mx)
        elif m1 == '3':
            break
        else:
            print("ERRO!Inroduza alguma opção!")


def add_list_empty(x):
    for i in range (x):
        v1 = input("Introduza valor: ")
        listEmpty.append(v1)
    print(listEmpty)

def add_list_full(x):
    for i in range(x):
        v1 = input("Introduza valor: ")
        listFull.append(v1)
    print(listFull)

#FUNC SET-----------------------------------------------
def add_set():
    m1 = 0
    while m1 != 3:
        print('''
        --- ADD SET ---
        1: Set Vazio
        2: Set Cheio
        3: Voltar
        ''')

        m1 = str(input("Escolha a sua opção: "))

        if m1 == '1':
            mx = 0
            while mx < 2:
                mx = valida_max()
            add_set_empty(mx)
        elif m1 == '2':
            mx = 0
            while mx < 2:
                mx = valida_max()
            add_set_full(mx)
        elif m1 == '3':
            break
        else:
            print("ERRO!Inroduza alguma opção!")

def add_set_empty(x):
    for i in range(x):
        v1 = input("Introduza valor")
        setEmpty.add(v1)
    print(setEmpty)

def add_set_full(x):
    for i in range(x):
        v1 = input("Introduza valor")
        setFull.add(v1)
    print(setFull)

#FUNC TUPLE--------------------------------------------------
def add_tuple():
    m1 = 0
    while m1 != 3:
        print('''
        --- ADD Tuple ---
        1: Tuple Vazio
        2: Tuple Cheio
        3: Voltar
        ''')

        m1 = str(input("Escolha a sua opção: "))

        if m1 == '1':
            mx = 0
            while mx < 2:
                mx = valida_max()
            add_tuple_empty(mx)
        elif m1 == '2':
            mx = 0
            while mx < 2:
                mx = valida_max()
            add_tuple_full(mx)
        elif m1 == '3':
            break
        else:
            print("ERRO!Inroduza alguma opção!")

def add_tuple_empty(x):
    global tupleEmpty
    for i in range(x):
        v1 = input("Introduza valor")
        tupleEmpty += tuple([v1])
    print(tupleEmpty)

def add_tuple_full(x):
    global tupleFull
    for i in range(x):
        v1 = input("Introduza valor")
        tupleFull += tuple([v1])
    print(tupleFull)

#FUNC DIC--------------------------------------------------
def add_dic():
    m1 = 0
    while m1 != 3:
        print('''
        --- ADD DIC ---
        1: Dic Vazio
        2: Dic Cheio
        3: Voltar
        ''')

        m1 = str(input("Escolha a sua opção: "))

        if m1 == '1':
            mx = 0
            while mx < 2:
                mx = valida_max()
            add_dic_empty(mx)
        elif m1 == '2':
            mx = 0
            while mx < 2:
                mx = valida_max()
            add_dic_full(mx)
        elif m1 == '3':
            break
        else:
            print("ERRO!Inroduza alguma opção!")

def add_dic_empty(x):
    for i in range(x):
        v1 = input("Introduza Chave: ")
        v2 = input("Introduza Valor: ")
        dicEmpty[v1] = v2
    print(dicEmpty)

def add_dic_full(x):
    for i in range(x):
        v1 = input("Introduza Chave: ")
        v2 = input("Introduza Valor: ")
        dicFull[v1] = v2
    print(dicFull)

#FUNC PRINT--------------------------------------------
def printAll():
    m1 = 0
    while m1 != '5':
        print('''
        --- PRINT ---
        1: Listas
        2: Set's
        3: Tuples
        4: Dicinários
        5: Voltar
        ''')

        m1 = str(input("Escolha a sua opção: "))

        if m1 == '1':
            print(listEmpty)
            print(listFull)
        elif m1 == '2':
            print(setEmpty)
            print(setFull)
        elif m1 == '3':
            print(tupleEmpty)
            print(tupleFull)
        elif m1 == '4':
            print(dicEmpty)
            print(dicFull)
        elif m1 == '5':
            break
        else:
            print("ERRO! Inroduza alguma opção!")
            
#FUNC DEL-------------------------------------------------------
def delet():
    m0 = 0
    while m0 != '6':
        print('''
        --- DELETE ---
        1: EliminarListas
        2: Eliminar Set's
        3: Eliminar Tuples
        4: Eliminar Dicinários
        5: MASTER DELETE
        6: Voltar
        ''')

        m0 = str(input("Escolha a sua opção: "))

        if m0 == '1':
            delet_list()
        elif m0 == '2':
            delet_set()
        elif m0 == '3':
            delet_tuple()
        elif m0 == '4':
            delete_dic()
        elif m0 == '5':
            delet_master()
        elif m0 == '6':
            break
        else:
            print("ERRO! Inroduza alguma opção!")
            
#FUNC DELET LIST------------------------------------------------
def delet_list():
    m1=0
    while m1 != '5':
        print('''
        --- DEL LIST ---
        1: Lista Vazia
        2: Lista Vazia Individual
        3: Lista Cheia
        4: Lista Cheia Individual
        5: Voltar
        ''')

        m1 = str(input("Escolha a sua opção: "))
        
        if m1 == '1':
            if len(listEmpty) != 0:
                listEmpty.clear()
            else:
                print("ERRO! Lista Vazia")
                break    
            print(listEmpty)
        if m1 == '2':
            if len(listEmpty) != 0:
                delet_listEmpty_i()
            else:
                print("ERRO! Lista Vazia")
                break
            
        elif m1 == '3':
            listFull.clear()
            print(listFull)
        if m1 == '4':
            delet_listFull_i()
            print(listFull)
        elif m1 == '5':
            break
        else:
            print("ERRO!Inroduza alguma opção!")
            
def delet_listFull_i():

    for i in range (0,len(listFull)):
        print(i,": ",listFull[i])
    
    x= int(input("Indice do elemento que deseja apagar: "))
    listFull.pop(x)
    print(listFull)
    
def delet_listEmpty_i():
    
    if len(listEmpty) != 0:
        for i in range (0,len(listEmpty)):
            print(i,": ",listEmpty[i])

        x= int(input("Indice do elemento que deseja apagar: "))
        listEmpty.pop(x)
        print(listEmpty) 
    else:
        print("ERRO! Lista Vazia")
        return
                   
#FUNC DELET SET------------------------------------------------
def delet_set():
    m1=0
    while m1 != '3':
        print('''
        --- DEL LIST ---
        1: Set Vazia
        2: Set Cheio
        3: Voltar
        ''')

        m1 = str(input("Escolha a sua opção: "))
        
        if m1 == '1':
            setEmpty.clear()
            print(setEmpty)
        elif m1 == '2':
            setFull.clear()
            print(setFull)
        elif m1 == '3':
            break
        else:
            print("ERRO!Inroduza alguma opção!")
    
#FUNC DELET TUPLE------------------------------------------------
def delet_tuple():
    m1=0
    while m1 != '3':
        print('''
        --- DEL LIST ---
        1: Tuple Vazio
        2: Tuple Cheio
        3: Voltar
        ''')

        m1 = str(input("Escolha a sua opção: "))
        
        if m1 == '1':
            global tupleEmpty
            temp = list(tupleEmpty)
            temp.clear()
            tupleEmpty = tuple(temp)
            print(tupleEmpty)
        elif m1 == '2':
            global tupleFull
            temp = list(tupleFull)
            temp.clear()
            tupleFull = tuple(temp)
            print(tupleFull)
        elif m1 == '3':
            break
        else:
            print("ERRO!Inroduza alguma opção!")
            
    
#FUNC DELET DIC------------------------------------------------
def delet_dic():
    m1=0
    while m1 != '3':
        print('''
        --- DEL LIST ---
        1: Dicionário Vazio
        2: Dicionário Cheio
        3: Voltar
        ''')

        m1 = str(input("Escolha a sua opção: "))
        
        if m1 == '1':
            dicEmpty.clear()
            print(dicEmpty)
        elif m1 == '2':
            dicFull.clear()
            print(dicFull)
        elif m1 == '3':
            break
        else:
            print("ERRO!Inroduza alguma opção!")
               
    
#FUNC DELET MASTER------------------------------------------------
def delet_master():
    listEmpty.clear()
    listFull.clear()
    setEmpty.clear()
    setFull.clear()
    global tupleEmpty
    temp = list(tupleEmpty)
    temp.clear()
    tupleEmpty = tuple(temp)
    global tupleFull
    temp = list(tupleFull)
    temp.clear()
    tupleFull = tuple(temp)
    dicEmpty.clear()
    dicFull.clear()
    
    print(listEmpty,listFull,setEmpty,setFull,tupleEmpty,tupleFull,dicEmpty,dicFull)
    

    
#FUNC VALIDA_MAX------------------------------------------------            
def valida_max():
    valido = False
    while not valido:
        try:
            op = int(input("Quantos valores: "))
            valido = True
            return op
        except ValueError:
            print("Digite um numero inteiro")