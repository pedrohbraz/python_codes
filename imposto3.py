while 1:   
    salario = input("salario:")
    imposto = input("imposto:")
    if not imposto:
         print("valor de imposto nao encontrado")
    elif imposto == 's':
        break
    else:
        imposto = float(imposto)
        if imposto < 15 :
            print("furto")  
        else:
            print("assalto")      
           