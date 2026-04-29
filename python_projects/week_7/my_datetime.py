import datetime

now = datetime.datetime.now()
"""print(now.year) #aasta
print(now.month) #kuu
print(now.day) #päev    
print(now.hour) #tunnid 
print(now.minute) #minutid
print(now.second) #sekundid"""

weekday = now.strftime("%A")
print(weekday) #nädalapäev  
