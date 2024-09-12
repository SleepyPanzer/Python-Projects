import random 
 
numbers=random.randint(1,100)
print (numbers)
running = True
guess=0
print("Welocm to number guessing game :")
while running:
    answer=int(input("enter any number between 1 -100 :"))
    if answer == numbers:
        print("you won the game ")
        print(f"you gues {guess}")
        break
        
    elif answer<numbers:
        print(f"answer is greater than {answer} :")
        guess+=1
    elif answer>numbers:
        print(f"answer  is less than the {answer} :")
        guess+=1

    else:
        print("you lost the game ")
        running=False
        