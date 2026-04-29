from read_from_file import read_data
from fight import calculate_hit


villain = read_data(r"week_8\villains.txt")
hero = read_data(r"week_8\heroes.txt")

hero_weapon = read_data(r"week_8\weapons.txt")
villain_weapon = read_data(r"week_8\weapons.txt")

#print(villain)
#print(hero)


hero_hit = calculate_hit(hero, hero_weapon)
villain_hit = calculate_hit(villain, villain_weapon)

print(f"{hero} uses {hero_weapon} and hits {villain} for {hero_hit} damage!")
print(f"{villain} uses {villain_weapon} and hits {hero} for {villain_hit} damage!")


if hero_hit > villain_hit:
    print(f"{hero} saves Viljandi!")
elif villain_hit > hero_hit:
    print(f"{villain} nukes Viljandi!")
else:
    print("It's a tie! Viljandi is safe... for now.")