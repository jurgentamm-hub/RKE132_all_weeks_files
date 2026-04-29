"Kirjutage programm, mis prindib sõne tagurpidi (viimasest tähemärgist esimese juurde), nii et iga täht kuvatakse eraldi reale."

sõna = input("Kirjuta oma lemmik sõna: ")

for i in sõna[::-1]:
    print(i)