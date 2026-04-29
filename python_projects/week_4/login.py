
username = input("Sisesta kasutajanimi:")
password = input("Sisesta parool:")

"""
if username == "user":
    if password == "1234":
        print("Welcome!")
    else:
        print("Access denied!")
else:
    print("Access denied!")
    """



"""
if username != "user" or password != "1234":
    print("Access denied!")
else:
    print("Access denied!")
    """


if username == "user" and password == "1234":
    print("Welcome!")
else:
    print("Access denied!")