# #variabile e stampa della variabile 
inizio_viaggio= input(" ciao questo è l'inizio dello studio di python")
print=(inizio_viaggio)


# #esempio di numeri 

num= input(" dammi un numero (senza virgola )")
print("perfetto questo è un intero", num)

num2=  input(" dammi un numero (con virgola )")
print("perfetto questo è un float", num2)


# #esempio stringa 
prova = int(input("Dimmi quanti anni hai? "))  
prova2 = input("Come ti chiami? ") 


print(f'{prova2},{prova}  complimenti hai scritto e concatenato la tua prima stringa ')

#esempio dei booleani


scelta=input("Vuoi continuare? (si/no?)")
if scelta== "no":
    break  

#esempio liste

while True:
    lista = input("Dammi una serie di dati? ")
    if len(lista) > 0:
    
        print(lista,"aprendo e chiudendo parentesi quadre hai creato una lista ")  
    else :
        print(" non hai creato nessuna lista ")
##### mirko non l ho termita mi da errore a voce poi ti spiego la mia idea pensavo di riuscire a terminare ma no idealmente sembrava buona come idea ma ho visto che no 





