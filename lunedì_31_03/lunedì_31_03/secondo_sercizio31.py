
#chiedo all'etente cosa sceglie di fare 

x = int(input("scegli un primo numero "))
y = int(input("scegli un secondo numero "))
operazione = (input("scegli quale operazione vuoi fare (+,-,*,/): "))

# esplicito cosa fare secondo le varie operazioni 
if operazione == "+" :
    print(x+y)
elif operazione == "-" :
    print(x-y)
elif operazione == "*" :
    print(x-y)
elif operazione == "/" :
    print(x-y)
    # tentativo di dividere per 0
if  x==0 or y==0 :
    print("errore:divisione per 0")
else:
    print("operazione non valida ")

    





