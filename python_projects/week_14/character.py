import random


class Character:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

        self.hp = len(name) + 10
    
    def isalive(self):
        return self.hp > 0
    
    def take_damage(self, damage):
        self.hp = self.hp - damage

        if self.hp < 0:
            self.hp = 0


class Hero(Character):
    def __init__(self, name, weapon):
        super().__init__(name, weapon)

    def attack(self,other):
        damage = random.randint(0, len(self.weapon))

        if damage == 0:
            print(f"{self.name} attacks with {self.weapon} but missed. noob hero!")
        
        if damage > other.hp:
            print(f"{self.name} attacks with {self.weapon} and does CRITIKALLL!!! {damage} damage. {other.name} is defeated!")
        else:
            print(f"{self.name} attacks with {self.weapon} and does {damage} damage.")
        

        other.take_damage(damage)
        print(f"{other.name} has {other.hp} health left.")

        heal = random.randint(1, 3)
        if heal > 0:
            self.hp = self.hp + heal
            print(f"{self.name} heals for {heal} hp. {self.name} has {self.hp} health now. \n")
        else: print(f"{self.name} doesnt heal.")


class Villain(Character):
    def __init__(self, name, weapon):
        super().__init__(name, weapon)
    

    def attack(self, other):
        damage = random.randint(0, len(self.weapon) * 2)

        if self.hp <= 5 and damage > 0:
            damage = damage + 2
        
        if damage == 0:
            print(f"{self.name} attacks with {self.weapon} but missed. stupid villain!")
        
        if damage > other.hp:
            print(f"{self.name} attacks with {self.weapon} and does HUGE DAMAGE!!! - {damage} damage. {other.name} is dead!")
        else:
            print(f"{self.name} attacks with {self.weapon} and does {damage} damage.")
        
        other.take_damage(damage)
        print(f"{other.name} has {other.hp} health left. \n")