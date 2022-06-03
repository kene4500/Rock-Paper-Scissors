import random

available_choices = ["R", "P", "S"]

def check_validity(user_choice, sys_choice):
    if user_choice in available_choices: #check if the user choice is in the list available_choices
        if user_choice == sys_choice:
            print("Game is TIED please try again") #Differnt things happen depending on user and cpu choice
            get_choices()
        elif user_choice== "S" and sys_choice=="P":
            print("Player(Scissors): CPU(Paper)")
            print("You Win")
            exit()
        elif user_choice== "R" and sys_choice=="S":
            print("Player(Rock): CPU(Scissors)")
            print("You Win")
            exit()
        elif user_choice== "P" and sys_choice=="R":
            print("Player(Paper): CPU(Rock)")
            print("You Win")
            exit()
        elif user_choice== "P" and sys_choice=="S":
            print("Player(Paper): CPU(Scissors)")
            print("You lose try again.")
            get_choices()
        elif user_choice== "S" and sys_choice=="R":
            print("Player(Scissors): CPU(Rock)")
            print("You lose try again.")
            get_choices()
        elif user_choice== "R" and sys_choice=="P":
            print("Player(Rock): CPU(Paper)")
            print("You lose try again.")
            get_choices()


    else:
        while user_choice not in available_choices:
            print("Your choice is invalid please enter R, P or S")
            get_choices()

def get_choices():
    print("This is a game of Rock, Paper, Scissors. You will be playing against the computer.")
    print('If you choose Rock, type "R".\nIf you choose Paper type "P".\nIf you choose Scissors type "S".\n')

    my_choice = input("Type your choice R, P, S here: ")
    comp_choice = random.choice(available_choices)
    my_choice = my_choice.upper()
    check_validity(my_choice, comp_choice)

get_choices()

