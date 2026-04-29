spent = int(input("Kui palju raha sa meie juures kulutasid?"))

"""
if spent >= 5000:
    print("Platinum")
elif spent >= 1000:
    print("Gold")
elif spent >= 500:
    print("Silver")
elif spent >= 100:
    print("Bronze")
else: 
    print("Regular customer")
    """

if spent < 100:
    print("Regular customer")
elif spent >= 100 and spent < 500:
    print("Bronze")
elif spent >= 500 and spent < 1000:
    print("Silver")
elif spent >= 1000 and spent < 5000:
    print("Gold")
else:
    print("Platinum")