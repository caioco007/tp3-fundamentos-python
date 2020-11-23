palavras = []
print ('Informe os 10 palavras')
for i in range(10):
    palavras.append(str(input('Palavra '+ str(i+1) + ':\n')))
palavras.reverse()
print (palavras)