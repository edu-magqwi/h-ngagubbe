import random
#ordlista med 10 ord
ord_lista = ["KOMPLICERAD", "HOMOGEN", "GRÖNSAK", "FONTANELL", "PERISKOP", "ORTOPED", "HYPERAKUSI", "PYTHON", "GERUNDIUM", "FORTNITE"]
#programmet slumpar
svar = None
while svar != "n":
#Kontrollerar när spelaren vill sluta spela spelet
    botval = random.choice(ord_lista)

    antal_felgissningar = len(botval)
    felgissningar = []
    ratt_gissade = []

    #Det spelas så länge man har gissningar kvar
    while antal_felgissningar > 0:

        print(f"Du ska gissa ett ord, bokstav för bokstav, på {len(botval)} bokstäver\nDu har nu {antal_felgissningar}.st felgissningar kvar\nFelgissningar: {"".join(felgissningar)}")

        # Visa ordet med stjärnor och rätt gissade bokstäver
        for bokstav in botval:
            if bokstav in ratt_gissade:
                print(bokstav, end="")
            else:
                print("*", end="")

        print()
    #Här blir gissningen automatiskt till små bokstäver och den ser till att man bara gissar en bokstav
        val = input("\nAnge en gissning -> ").upper()
        if len(val) != 1:
            print("Du får bara gissa en bokstav!")
            continue
    #Kollar om vi redan har gissat den bokstaven
        if val in ratt_gissade or val in felgissningar:
            print("Du har redan gissat den bokstaven!")
            continue
            #Här kollar vi om gissningen är korrekt eller inte och uppdaterar listorna och antalet felgissningar
        if val in botval:
            ratt_gissade.append(val)
        else:
            antal_felgissningar -= 1
            felgissningar.append(val)

        if len(ratt_gissade) == len(set(botval)):
            print(f"Du överlevde!\nOrdet var: {botval}")
            break
      

    if antal_felgissningar == 0:
        print("Du har inga felgissningar kvar!")
        print("Rätt ord var:", botval)
    svar = input("Vill du spela en till omgång (j/n) ->")
    while svar != "j" and "n":
        print("Ogiltigt svar, svara 'j' eller 'n'")
        svar = input("Vill du spela en till omgång (j/n) ->")
    

