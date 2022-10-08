import random
rock = '''
    _______
---'  (____)
      (___.__)
      (__.___)
      (____)
---.__(___)
'''

paper = '''
    ______
---'   ___)____ )
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    ______
---'   ___)______
          ________)
       ___________)
      (____)
---.__(___)
'''
game_images=[rock,paper,scissors]
print(game_images[0],game_images[1],game_images[2])
user_choice=int(input("What do you choose? type 0 for Rock , 1 for paper or 2 for Scissors. " ))
print(game_images[user_choice])
computer_choice=random.randint(0,2)
print(40*"-") 
print(game_images[computer_choice])
print("computer chose",(computer_choice))
if  user_choice==0  and computer_choice==2:
    print("You win !!  \U0001f600 \U0001f600 \U0001f600")
elif user_choice==2 & computer_choice==0:
    print("You lose ??\U0001F606 \U0001F606 \U0001F606")
elif computer_choice > user_choice:
    print("You lose ?? \U0001F606 \U0001F606 \U0001F606 ")
elif user_choice > computer_choice:
    print("You win !!\U0001f600 \U0001f600 \U0001f600") 
elif computer_choice==user_choice :
    print("it's a draw &&")
elif  user_choice>=3:
    print("you typed an invalid number, you lose !!!!!!  ")


#"new comment"
    


