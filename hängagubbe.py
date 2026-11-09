import random
#orlista med 10 ord
ord_lista = ["komplicerad", "homogen", "grönsak", "fontanell", "periskop", "ortoped", "hyperakusi",  "python", "gerundium", "fortnite"]
#programmet väljer ett slumpmässigt ord ur listan
botval = random.choice(ord_lista)
antal_felgissningar = len(botval) + 1
while True:
    print(f"du ska gissa ett ord, bokstav för bokstav, {len(botval)} bokstäver)")
    val = input("Ange en gissning -> ")
    val = val.isalnum
    if len(str(val)) > 1:
        print("Du får bara gissa en bokstav, gissa igen")
    if val is not botval:
        antal_gissningar += -1
    print(f"Du har nu f{antal_felgissningar}.st felgissningar kvar")
        
    
