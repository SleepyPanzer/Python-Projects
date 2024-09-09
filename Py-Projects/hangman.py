import random 
word_list=["apple","peach"]

    
HANGMAN_PICS = { 0:('''
     +---+
         |
         |
         |
        ==='''), 1:('''
     +---+
     O   |
        |
        |
       ==='''),2:( '''
    +---+
    O   |
    |   |
        |
       ==='''),3:( '''
    +---+
    O   |
   /|   |
        |
       ==='''),4:( '''
    +---+
    O   |
   /|\  |
        |
       ==='''), 5:('''
    +---+
    O   |
   /|\  |
   /    |
       ==='''), 6:('''
    +---+
    O   |
   /|\  |
   / \  |
       ===''')}


def display_hanman(wrong_guess):
   # for i in HANGMAN_PICS[wrong_guess]:
   #  print(i)
   print(HANGMAN_PICS[wrong_guess])
def dis_hint(hint):
   print("".join(hint))
def answer(word):
   print("".join(word))
   

   
   
def main():
      word_list=["apple","peach"]
      guessed_letter=set()
      word=random.choice(word_list)
      running=True
      hint=['_']*len(word)
      wrong_guess=0
      while running:
            display_hanman(wrong_guess)
            dis_hint(hint)
            answer=input("guess the letter :").lower()
            if answer in word:
                  for i in range(len(word)):
                     if word[i] == answer:
                         hint[i] = answer
            else:
               wrong_guess+=1
            if "_" not in hint:
               print("You won the game ")
               running=False
               
          
         
      
if __name__ == "__main__":
    main()
      

   
   
   
    
