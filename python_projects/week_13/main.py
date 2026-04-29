from animal import Animal, Cat, Dog

my_cat = Cat("Sigmard")
my_dog = Dog("Max")
neighbor_dog = Dog("Jaasna")
random_cat = Cat("Vello")

"""
my_cat.meow()
my_dog.bark()
"""

my_cat.cat_sees(neighbor_dog)
my_cat.cat_sees(random_cat)
"""my_dog.sees(my_cat)"""