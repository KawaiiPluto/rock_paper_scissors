## rock paper scissors
import random



user = input('your name: ')

print(f"welcome  {user}")



isplaying = True
print("system:   welcome to rock paper scissors")

choices = ["rock","scissors","paper"]

while isplaying:





 user_choice= input("enter your choice: ")
 computer_choice = random.choice(choices)

 if user_choice.lower() == computer_choice.lower():
  print(f"user choice: {user_choice.lower()} \n computer choice: {computer_choice.lower()}")
  print("draw")

 elif user_choice.lower()=="rock" and computer_choice.lower()=="scissors":
  print(f"user choice: {user_choice.lower()} \n computer choice: {computer_choice.lower()}")
  print("you win")

 elif user_choice.lower() == "scissors"and computer_choice.lower() == "paper":
  print(f"user choice: {user_choice.lower()} \n computer choice: {computer_choice.lower()}")
  print("you win.")

 elif user_choice.lower() == "paper" and computer_choice.lower() == "rock":
  print(f"user choice: {user_choice.lower()} \n computer choice: {computer_choice.lower()}")
  print("you win")
 elif user_choice.lower() == "scissors" and computer_choice.lower()== "rock":
  print(f"user choice: {user_choice.lower()} \n computer choice: {computer_choice.lower()}")
  print("computer win")

 elif user_choice.lower()=="paper" and computer_choice.lower()== "scissors":
  print(f"user choice: {user_choice.lower()} \n computer choice: {computer_choice.lower()}")
  print("you win")

 elif user_choice.lower()=="rock" and computer_choice.lower()=="paper":
  print(f"user choice: {user_choice.lower()} \n computer choice: {computer_choice.lower()}")
  print("computer win")

 else:
  print("system:   i didnt understand what you said")



 print("say yes or no")

 close_game= input("system:   do you want to play again? \n")


 if close_game.lower() == "yes":
  isplaying
 elif close_game.lower() == "no":
  print('system:   thank you for playing see you soon')
  isplaying = False
  print("========================end game==========================")
 else:
  print("system:   i didnt understand what you said")