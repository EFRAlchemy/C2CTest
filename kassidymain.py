import random

name = input("What is your name? \n>")

print(f'\nWelcome to the Elitebot {name}!\n')

age = input(f'So {name}, how old are you?? \n>')

print(f'\nLord!! {age}!? That is so cool!!\n')


def display_menu():
  print(f' Anyways, it seems like you need help {name}.\n')
  print("1. Sign in/Log in")
  print("2. Create Savings Account")
  print("3. Create Checking Account")
  print("4. Transfer Money")
  print("5. Deposit Money")
  print("6. Exit")

display_menu()
  
def selection():
  choice = int(input('''
  Enter your choice so I can properly assist. \n>'''))
  if choice == 1:
    print("Okay hold on,\n")
    #Make sure you ask user 'sign in or log in?' in choice1 def
    choice_1()
  elif choice == 2:
    print("Let's get you started.\n")
    choice_2()
  elif choice == 3:
    print("1. Tranfer 2. Desposit 3. Withdraw")
    choice_3()
  elif choice == 4:
    print("Oh, you exited. Bye Bye.")
    choice_4()

selection()

def choice_1():
  print("Hey! I can't actually show you a video, but I can say a joke!!")
choice_1()

def choice_2():
  print("Why cant a statistic answer an algebraic question correct? Because it will PROBABLY get it wrong, hahahaha!!")
choice_2()

def choice_3():
  print("Sure! 2x + 8, find the value of x. X is = to 4!")
choice_3()

def choice_4():
  print(f"Aw shucks. See you next time then {name}!")
choice_4()
  
selection()

#My Exit message works and still displays, yet it's an error
#I'll work on that as this course progresses.