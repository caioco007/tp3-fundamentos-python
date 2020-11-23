frase = []
cont=0
for i in range (100):
    frase.append(str(input('Digite uma frase: ')))
    if frase[i] != 'sair':
        if 'eu' in frase[i]:
            cont+=1
            print('A palavra EU:', cont)
    else:
        frase.remove('sair')
        break
print('EXIT')
print('A palavra EU está em',cont,' frases')