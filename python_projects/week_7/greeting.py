

def get_greeting(daytime):
    greeting = ""
    if daytime < 12:
        return "Good morning my friend"
    elif daytime < 18:
        return "Good afternoon kõik toimib funktsiooni sees"
    else:
        return "Good evening, tere õhtust"
