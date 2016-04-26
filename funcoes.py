# o comando def é usado para se declarar uma função
def sum(a,b):
    return a+b
    
c = sum(1,3)
print(c)    

#valore padronizados de argumentos
def desconto(valor, desc=12):
    return valor - desc
    
print(desconto(25))    

#parametros nomeados
print(desconto(25,desc=11))

#numero arbitrario de argumentos packing e unpacking

from datetime import date
d = (2016,4,25)
print(date(*d))

def new_user (active = False, admin = False):
    print(active)
    print(admin)
    
config = {"active":False,      #dicionaario
          "admin":True}    
          
new_user(**config)          


#unpacking é usado dentro das funções
#*args ou **kwargs

def unpacking_experiment(*args):
    arg1 = args[0]
    arg2 = args[1]
    others = args[2:]
    print(arg1)
    print(arg2)
    print(others)
    
    
#a função recebeu um numero qualquer de parametros
print(unpacking_experiment(1,2,5,5,5,6,7,8,8))  

def unpack(**kwargs):
    print(kwargs)
    
print(unpack(named="Teste",other="Other"))    

