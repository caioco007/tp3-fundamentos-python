lista_1 = []
lista_1.append(1)
lista_1.append(2)
lista_1.append(3)
lista_1.append(4)
lista_1.append(5)
print(lista_1)

lista = [3,6]
if 3 in lista_1:
    lista_1.remove(3)
    print(lista_1)

if 6 not in lista_1:
    print('elemento 6 não encontrado')

else:
    print('elemento não encontrado')

print("Tamanho da lista:",len(lista_1))

lista_1[(len(lista_1)) - 1] = 6
print(lista_1)

