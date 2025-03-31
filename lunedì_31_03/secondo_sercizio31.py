# while True:
#     print("\n--- MENU ---")
#     print("1) addizione")
#     print("2) sottrazione")
#     print("3) moltiplicazione ")
#     print("4) divisione")
#     print("5) Esci")

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
elif operazione == "/0" :
    print("errore:divisione per 0")
else:
    print("operazione non valida ")

    





