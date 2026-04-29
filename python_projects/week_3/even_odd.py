"küsi arvu, vaata kas on paaris või paaritu"
#Moduls

n = int(input("Sisesta mingi arv: "))

"""if n % 2 == 0:
    print("PAARIS ARV")
else:
    print("PAARITU ARV")"""


#   ternary operator
print("Arv on paaris" if n % 2 == 0 else "Arv on paaritu!!!")

match n % 2:
    case 0:
        print("Arv on paaris")
    case 1:
        print("Arv on paaritu")
