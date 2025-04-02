# def decoratore(funzione):
#     def wrapper():#serve a mettere la funzione all'interno di un panino 
#         print(" prima  dell'esecuzione della funzione ")
#         funzione()
#         print("Dopo l'esecuzione della funzione ")
#     return wrapper
    
    
    
    
    
# @decoratore 
# def saluta():
#     print("ciao")
#     #la funzione viene richiamata qui    
# saluta()


# abbiamo modificato la funzione senza toccare la funzione 


# def decoratore_con_argomenti(funzione):
#     def wrapper(*args,**kwargs):
#         print("Prima")
#         risultato=funzione(*args,**kwargs)
#         print("Dopo")
#         return risultato +2
#     return wrapper
    
# @decoratore_con_argomenti
# def somma (a,b):
#     print(a+b)
#     return a+b# funzione decorata

# print("risultato è ",somma(3,5))





def logger(funzione):
    def wrapper(*args, **kwargs):
        print(f"Chiamata a {funzione.__name__} con argomenti: {args} e {kwargs}")
        risultato = funzione(*args, **kwargs)
        print(f"Risultato di {funzione.__name__}: {risultato}")
        return risultato
    return wrapper

@logger
def moltiplica(a, b):
    return a * b

# Chiamata alla funzione decorata
print (moltiplica(3, 4))