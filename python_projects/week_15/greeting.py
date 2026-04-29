import tkinter as tk


root = tk.Tk()
root.title("Greeting")
root.geometry("500x300")
root.grid_columnconfigure(0, weight=1)

def say_hello():
    greeting_label.config(text="Hello, world!")

def greet_user():
    name = name_input.get()

    greeting_label.config(text=f"Hello, {name}!")

greeting_label = tk.Label(root, text="jou jou jou!111!!!")
greeting_label.grid(row=0, column=0)

hello_button = tk.Button(root, text="CLICK ME", command=say_hello)
hello_button.grid(row=1, column=0, pady=10)


#2. osa
name_input = tk.Entry(root, width=20)
name_input.grid(row=2, column=0, pady=10)

greet_button = tk.Button(root, text="tsau!", command=greet_user)
greet_button.grid(row=3, column=0, pady=10)


root.mainloop()