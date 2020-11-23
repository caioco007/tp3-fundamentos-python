lista = []
for i in range (100):
    print('\n1. Mostrar lista')
    print('2. Incluir elemento')
    print('3. Remover elemento')
    print('4. Apagar todos os elementos da lista.')

    alternativa= int(input('\nDigite uma alternativa: '))

    if 1 == alternativa:
        print('\n1. Mostrar lista')
        print(lista)
    elif 2 == alternativa:
        print('\n2. Incluir elemento')
        elemento = str(input('Digite um elemento: '))
        lista.append(elemento)
        print(lista)
    elif 3 == alternativa:
        print('\n3. Remover elemento')
        print(lista)
        del_elem = str(input('Qual elemento deseja remover: '))
        lista.remove(del_elem)
        print(lista)
    elif 4 == alternativa:
        print('\n4. Apagar todos os elementos da lista.')
        lista.clear()

    else:
        print('\nValor inválido')