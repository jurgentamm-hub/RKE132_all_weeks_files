import random

shopping_list = ["apple", "bread", "milk", "eggs", "cheese",]

"""
print(f"We have {len(shopping_list)} items in our shopping list.")

shopping_list.extend(["flour", "sugar", "baking powder"])

print(f"We have {len(shopping_list)} items in our shopping list.")

shopping_list.remove("cheese")

for i in shopping_list.copy():
    if item == "cheese":
        shopping_list.remove(item)

print(shopping_list)

for item in shopping_list:
    print(item)
    """

n = shopping_list.count("cheese")


apple_index = shopping_list.index("apple")
print(f"You can find the apple in {apple_index}")


found = "milk" in shopping_list
for item in shopping_list:
    if item == "milk":
        found = True
        break

if found:
    print("Milk is already in the list bro.")
else:
    print("Milk is not in the list.")



#sorting
shopping_list = ["apple", "bread", "milk", "eggs", "cheese",]
shopping_list.sort(reverse=True)
print(shopping_list)

#reverse
shopping_list.reverse()


#random
random_item = random.choice(shopping_list)
print(random_item)