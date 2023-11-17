import random
print("~~~ROCK PAPER SCISSORS~~~")
user_score=0
comp_score=0
ties=0
name=input("Enter Your Name Here:")
print("""
Winning Rules:
1.Rock vs Scissors--->Rock
2.Paper vs Rock--->Paper
3.Scissors vs Paper--->Scissors""")
while True:
    print("""
    YOUR CHOICES ARE---
    1.Rock
    2.Paper 
    3.scissors""")
    choice=int(input("Enter Your Choice 1-3:"))
    while choice < 1 or choice > 3:
      choice=int(input("Enter Valid choice"))
    if(choice==1):
        user_choice="Rock"
    elif(choice==2):
        user_choice="Paper"
    else:
        user_choice="Scissors"

    print("user_choice is:",user_choice)
    print()
    print("Now it's Computer turn:")
    print()
    computer=random.randint(1,3)
    if(computer==1):
        computer_choice="Rock"
    elif(computer==2):
        computer_choice="Paper"
    else:
        computer_choice="Scissors"
    print("computer choice is:",computer_choice)
    if((user_choice=="Paper" and computer_choice=="Rock"))or((user_choice=="Rock" and computer_choice=="Paper")):
        print("Paper wins")
        result="Paper"
    elif((user_choice=="Rock" and computer_choice=="Scissors"))or((user_choice=="scissors" and computer_choice=="Rock")):
        print("Rock wins")
        result="Rock"
    elif user_choice==computer_choice:
        print("IT'S A TIE")
        result = "tie"
    else:
        print("Scissors wins")
        result = "Scissors"

    if result == "TIE":
     ties+=1
    elif result == user_choice:
     print("***YOU WIN***")
     user_score +=1
    else:
     print("**computer wins**")
     comp_score +=1

    print("scores are---->")
    print(name,'s score is',user_score)
    print("computer score",comp_score)
    print("ties are",ties)

    repeat=input("do you want to play again?")
    if repeat=="N" or repeat=="NO" or repeat=="n" or repeat=="no":
      break
print("GAME OVER")
print("THANKS FOR PLAYING!!!")