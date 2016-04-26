objetos = ['faca','espada','tv','mouse']

for objeto in objetos:   #semelhante ao foreach de outras linguagens
    if objeto.startswith('e'):
        for i in range(10): #como o for classico de outras linguagens
            print (i)       # um objeto retornado por um range é um iterador
        continue
    print(objeto)    