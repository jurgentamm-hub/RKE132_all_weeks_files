import datetime

from hello import say_hello

hour = datetime.datetime.now().hour
name = input("Enter first name!!!!!: ")
        
say_hello(hour, name)