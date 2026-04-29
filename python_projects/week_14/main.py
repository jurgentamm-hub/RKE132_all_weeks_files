from file_utils import get_random_from_file
from character import Hero, Villain


hero_name = get_random_from_file(r"week_14\heores.txt")
hero_weapon = get_random_from_file(r"week_14\weapons.txt")

villain_name = get_random_from_file(r"week_14\villains.txt")
villain_weapon = get_random_from_file(r"week_14\weapons.txt")



hero = Hero(hero_name, hero_weapon)
villain = Villain(villain_name, villain_weapon)


print(" x=x=x=x=x VÕITLUS ALAKU!!! x=x=x=x=x ")
print(f"{hero.name} VS {villain.name} \n")
print(f" Hero: {hero.name} - HP : {hero.hp} - Weapon: {hero.weapon} \n")
print(f" Villain: {villain.name} - HP : {villain.hp} - Weapon: {villain.weapon} \n")

round_number = 1

while hero.isalive() and villain.isalive():
    print(f" x=x=x=x=x ROUND {round_number} x=x=x=x=x \n")

    hero.attack(villain)
    
    if not villain.isalive():
        break

    villain.attack(hero)
    
    round_number = round_number + 1

print(" x=x=x=x=x GAME OVER x=x=x=x=x \n")

if hero.isalive():
    print(f"{hero.name} WINS!!!")
else:
    print(f"{villain.name} WINS!")
