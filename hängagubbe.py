import random
#ordlista med 10 ord
ord_lista = ["komplicerad", "homogen", "grönsak", "fontanell", "periskop", "ortoped", "hyperakusi",  "python", "gerundium", "fortnite"]
botval = random.choice(ord_lista)

antal_felgissningar = len(botval)
felgissningar = []
ratt_gissade = []

while antal_felgissningar > 0:

    print(f"Du ska gissa ett ord, bokstav för bokstav, på {len(botval)} bokstäver")

    # Visa ordet med stjärnor och rätt gissade bokstäver
    for bokstav in botval:
        if bokstav in ratt_gissade:
            print(bokstav, end="")
        else:
            print("*", end="")

    print()

    val = input("Ange en gissning -> ").lower()

    if len(val) != 1:
        print("Du får bara gissa en bokstav!")
        continue

    if val in ratt_gissade or val in felgissningar:
        print("Du har redan gissat den bokstaven!")
        continue

    if val in botval:
        ratt_gissade.append(val)
    else:
        antal_felgissningar -= 1
        felgissningar.append(val)

    print(f"Du har nu {antal_felgissningar} st. felgissningar kvar.")
    print("Felgissningar:", ", ".join(felgissningar))

    if all(bokstav in ratt_gissade for bokstav in botval):
        print("Grattis! Du gissade rätt ord:", botval)
        break

    print()

if antal_felgissningar == 0:
    print("Du har inga felgissningar kvar!")
    print("Rätt ord var:", botval)
    
