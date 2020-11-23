num = []
cont=0
print ('Informe os 5 numeros')
for i in range(5):
    num.append(int(input('Numero '+ str(i+1) + ':\n')))
    if num[i] == 0:
        cont+=1
print(num)
print("Quantidade de Zeros: ", cont)
