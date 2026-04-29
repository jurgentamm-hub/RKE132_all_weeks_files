from colorama import Fore, Style
"küsib lemmikvärvi ja siis väljastab teksti"

color = input("Sisesta enda lemmikvärv? ").lower()

"""if color == "punane":
    print("Sina oled energiline inimene!")
elif color == "roosa":
    print("Sina oled romantik!")
elif color == "roheline":
    print("Sina oled rahulik inimene!")
elif color == "sinine":
    print("Sina oled keskendudnud inimene!")
else:
    print("Sina oled imeline ükssarvik!")"""

match color:
    case "punane":
            print(Fore.RED + "Sina oled energiline inimene!")
    case "roosa":
            print(Fore.PINK + "Sina oled romantik!")
    case "roheline":
            print(Fore.GREEN + "Sina oled rahulik inimene!")
    case "sinine":
            print("Sina oled keskendudnud inimene!")
    case _:
            print("Sina oled imeline ükssarvik!")