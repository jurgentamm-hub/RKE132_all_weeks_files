"""Kirjuta programm, mis küsib kasutajalt tema perekonnanime ja sugu (vali „m“ või „n“).
Programm tervitab kasutajat vastavalt soole:
Kui kasutaja valib „m“, väljasta: „Tere, härra [Perekonnanimi]!“
Kui kasutaja valib „n“, väljasta: „Tere, proua [Perekonnanimi]!“
Kui kasutaja sisestab midagi muud, väljasta: „Tere tulemast, [Perekonnanimi]! (sugu ei olegi tähtis).“"""

perekonnanimi = input("Sisesta oma perekonnanimi: ")
sugu = input("Sisesta oma sugu (m/n): ")
if sugu == "m":
    print("Tere, härra " + perekonnanimi + "!")
elif sugu == "n":
    print(f"Tere proua {perekonnanimi}!")
else:
    print("Tere tulemast, " + perekonnanimi + "! sugu ei olegi tähtis" )