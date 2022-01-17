import random
import threading
from tkinter import *
from tkinter.ttk import *

def generate_sequence(difficulty):
    generated_list = []
    for i_generated in range(int(difficulty)):
        generated_list.append (random.randrange(1, 101))
    return generated_list

def get_list_from_user(difficulty):
    memorized_list = [0] * difficulty
    memorized_list = input('Insert your memorized numbers ').split()
    for i_list in range(0,len(memorized_list) - 1):
        if memorized_list[i_list].isnumeric == False:
            memorized_list.clear()
            return memorized_list
    return memorized_list

def is_list_equal(difficulty):
    generated_list = generate_sequence(difficulty)
    show_list(difficulty,generated_list)

    memorized_list = get_list_from_user(difficulty)
    is_the_same = True
    for i_list in range(difficulty):
        if len(generated_list) == len(memorized_list) and \
            int(generated_list[i_list]) == int(memorized_list[i_list]):
                continue
        else:
            is_the_same = False
            break
    return is_the_same

def show_list(difficulty,generated_list):
    root = Tk()
    root.geometry("450x300")
    root.title("Memory Game")
    label = Label(root, text="Memory Game").pack()
    user_name = Label(root, text="The number to remember are" + str(generated_list)).place(x = 40,y = 60)
    root.attributes('-topmost', True)
    root.update()
    event = threading.Event()
    event.wait(0.7*difficulty)
    root.destroy()
    root.mainloop()
    return

def play(difficulty):
    return is_list_equal(difficulty)



# print (generate_sequence(5))
# print(get_list_from_user(5))
# print (play(3))