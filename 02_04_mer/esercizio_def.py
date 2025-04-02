def  quadrato ():
    numero=int (input(" dammi un numero?: "))
    n=numero*numero
    
    
    
    
    print("in quadrato del numero è ", n)





def somma_lista(lista):
    somma=0
    for numero in lista :
        somma+=numero
    print(somma)

        
        
while True:   
    
    quadrato()
    
    scelta=input("Vuoi continuare?")
    if scelta== "no":
        break
    
while True:   
    lista=[]
    while True:
         numero=int (input(" dammi un numero?: "))
         lista.append(numero)
         if len(lista)> 2:
             break
    somma_lista(lista)
    
    scelta=input("Vuoi continuare?")
    if scelta== "no":
        break  
