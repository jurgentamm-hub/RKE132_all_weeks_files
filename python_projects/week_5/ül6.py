"Kirjutage programm, mis kordab parooli küsimist seni, kuni kasutaja annab õige vastuse."

parool = input("Sisesta parool: ")
õige_parool = "maarmastanpythonit"

while parool != õige_parool:
    print("VALE!!!!!!!!")
    parool = input("Sisesta parool uuesti: ")
print("ÕIGE!!1!11!1!!1111!111!")