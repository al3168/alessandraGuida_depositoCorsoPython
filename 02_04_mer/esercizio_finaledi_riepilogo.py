# inizio= input("inizio del viaggio")
# print=(inizio)

# fase1= input("da cosa abbiamo iniziato?(scegli tu cosa vedere  )(variabili, numeri, stringhe booleani, liste , tuple, cicli, if,for,range,match)?")
    
# print=(fase1)


# match fase1:
#     case "variabili":
#         print=("la variabile sono un fondamento della programmazione in le quali seguono precise regole per essere dichiarate non posso iniziare con _ ,non posso essere maiuscole,non possono avere spazi  ")
        
#     case "numeri":
#         print =("abbiamo diversi tipi di numeri interi e con la virgola float" )
        
#     case "stringhe":
#         print=("le stringhe fanno parte dei tipi di dato basilari formate a loro volta da char e sono particolari perchègià loro sono un insieme di char ma anche perchè possono richiamare dei metodi (vuoi sapere quali: si / no?")
#         while True :
#             if "si" :
#                 print=("len", "append", "upper")
#             else:
#                 "no"
#                 print=(" perfetto allora ti faccio vedere solo un esempio di stringa che va  scritta nei doppi o singoli  apici che sia numero o parola quindi '21','ciao'")
                
#     case "booleani":
#         print=("è un tipo di dato che ci restituisce True o False" )
        
#     case "liste":
#         print=("la lista è una struttura di dato che contiene all'interno diversi tipi di dato delimitate dalle parentesi quadre anch'esse posso richiamre dei metodi (vuoi vedere un esempio: si/no? )")
#         while True:
#             if  "si":
#                 print=("ecco un esmepio di lista [ciao, 1, True,4,5 ] ")
#                 print=("un esempio dei suoi metodi sono append dove vado aggiungere un elemento alla fine della lista insert in una possizione specifica ")
#             else :
#                 "no"
#                 print=("va bene non fa niente ")



inizio = input("Inizio del viaggio: ")
print(inizio)

fase1 = input("Da cosa abbiamo iniziato? (scegli tu cosa vedere: variabili, numeri, stringhe, booleani, liste, tuple, cicli, if, for, range, match): ")

print(fase1)

match fase1:
    case "variabili":
        print("Le variabili sono un fondamento della programmazione e seguono precise regole per essere dichiarate: non possono iniziare con _, non possono essere maiuscole e non possono avere spazi.")
        
    case "numeri":
        print("Abbiamo diversi tipi di numeri: interi e con la virgola (float).")
        
    case "stringhe":
        print("Le stringhe fanno parte dei tipi di dato basilari e sono formate a loro volta da char. Sono particolari perché già loro sono un insieme di char, ma anche perché possono richiamare dei metodi. Vuoi sapere quali? (si / no)")
        
        risposta = input().lower()  # A questo punto, prendi la risposta dell'utente
        while True:
            if risposta == "si":
                print("len, append, upper")
               
            elif risposta == "no":
                print("Perfetto, allora ti faccio vedere solo un esempio di stringa che va scritta nei doppi o singoli apici, che sia numero o parola, quindi '21', 'ciao'.")
              
            else:
                print("Risposta non valida. Rispondi con 'si' o 'no'.")
                risposta = input().lower()  # Chiedi di nuovo la risposta

    case "booleani":
        print("È un tipo di dato che ci restituisce True o False.")
        
    case "liste":
        print("La lista è una struttura di dato che contiene all'interno diversi tipi di dato, delimitate dalle parentesi quadre. Anch'esse possono richiamare dei metodi. Vuoi vedere un esempio? (si / no)")
        
        risposta = input().lower() 
while True:
            if risposta == "si":
                print("Ecco un esempio di lista: [ciao, 1, True, 4, 5].")
                print("Un esempio dei suoi metodi è append, dove vado ad aggiungere un elemento alla fine della lista, o insert in una posizione specifica.")
            elif risposta==   "no":
                print("Va bene, non fa niente.")
            
            
##### mirko non l ho termita mi da errore a voce poi ti spiego la mia idea pensavo di riuscire a terminare ma no idealmente sembrava buona come idea ma ho visto che no 

            
        
            