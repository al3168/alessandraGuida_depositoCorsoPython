def  quadrato ():
    numero=int (input(" dammi un numero?: "))
    n=numero*numero
    
    
    
    
    print("in quadrato del numero è ", n)





def somma_lista(lista):
    somma=0
    for numero in lista :
        somma+=numero
    print(somma)

        
     
while True:   #mi rende il cilo infinito   
    
    quadrato()
    
    scelta=input("Vuoi continuare?")
    if scelta== "no":
        break# mi fa uscire dal ciclo
    #creo una lista dinamica i cui valori li chiedo al cliente 
while True:   
    lista=[]
    while True:
         numero=int (input(" dammi un numero?: "))
         lista.append(numero)
         if len(lista)> 2:
             break
    somma_lista(lista)
    
    # booleano semplice che mi da la possibilità di uscire  il programma 
    scelta=input("Vuoi continuare?")
    if scelta== "no":
        break  
    
#  controllori di flusso

contr_flusso= input(" siamo a metà della nostro peercorso dei fondamenti di python sai cosa sono i controllori dei flussi? (si/no)")

