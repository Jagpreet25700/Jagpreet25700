import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========\nYOU LOSE!
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
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)

lives = 6
word_list = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()
chosen_word = random.choice(word_list)
word_len = len(chosen_word)
display = []

for _ in range(word_len):
    display += "_" 

end_game = False
while end_game == False:
    selected_word = input("Guess a word: ").lower()

    for position  in range(word_len):
        letter = chosen_word[position]

        if letter == selected_word:
            display[position] = letter

    if selected_word not in chosen_word:
        lives -= 1
        if lives == 0:
            end_game = True
    print(display)


    if "_" not in display:
        end_game = True
        print("You win!") 
    print(stages[lives])    