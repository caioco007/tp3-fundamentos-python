import statistics

nome = []
altura = []
lista = []

for i in range (100):
    nome.append(str(input('Digite seu nome: ')))
    if nome[i] != 'sair':
        altura.append(float(input('Digite sua altura: ')))
        lista.append([nome,altura])
    else:
        nome.remove('sair')
        break
print('EXIT')

media = statistics.mean(lista[0][1])
print('Média de idade: ',media)

def alt_max (valor,tamanho,texto):
    alt=[]
    for i in range(len(tamanho)):
        if tamanho[i] > valor:
            alt.append(texto[i])
            i += 1
    return alt

print(alt_max(media,altura,nome))




