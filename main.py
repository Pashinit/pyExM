import modo_ex

m = 0

while m != '6':
    print('''
            --- Menu ---
    1: Adicionar elemento à Lista
    2: Adicionar elemento ao Set
    3: Adicionar elemento ao Tuple
    4: Adicionar elemento ao Dicionário
    5: Imprimir
    6: Sair
    ''')

    m = str(input("Escolha a sua opção: "))

    if m == '1':
        modo_ex.add_list()
    elif m == '2':
        modo_ex.add_set()
    elif m == '3':
        modo_ex.add_tuple()
    elif m == '4':
        modo_ex.add_dic()
    elif m == '5':
        modo_ex.printAll()
    elif m == '6':
        break
    else:
        print("ERRO!Inroduza alguma opção!")
