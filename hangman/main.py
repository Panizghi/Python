
#HANGMAN
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

import random

from wordlist import word_list

chosen_word = random.choice(word_list)
print(chosen_word)
display =[]
for i in range(len(chosen_word)) :
    display += "_"
    
print(display)

end_game = False

lives = 6

while not (end_game or lives == 0) :
 print(stages[lives])
 guess = input("Give me a letter : ").lower()[0]
 
 if guess in chosen_word :
    for position in range(len(chosen_word)):
        if chosen_word[position]==guess :
            display[position]=guess
     
        
 else :
    
    lives -= 1

 print(display)
 print(lives)
 if '_' not in display :
        end_game = True
        print("YAY YOU WIN!")
 elif lives==0 : 
    print(stages[lives])
    print("LOSER")


   


 

    


