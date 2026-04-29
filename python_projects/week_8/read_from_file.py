from utils import clean_my_list
import random
def read_data(file_path):
    
    ###file_path = "C:\Users\krist\python_projects\week_8\heroes.txt" #absoluutne tee täielik tee failini minu arvutis###
    #file_path = r"week_8\villains.txt" #suhteline tee, kui fail on samas kataloogis, kus skript VALI ÜKS
    with open(file_path, "r", encoding="utf-8") as f:
        data = clean_my_list(f.readlines())
        random_item = random.choice(data)
        return random_item
