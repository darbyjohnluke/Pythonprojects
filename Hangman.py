import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
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
stagecounter = 6
word_list = ["aardvark", "baboon", "camel"]
randomword = random.choice(word_list)
gameover = 0
guessedletters = []
while gameover < 6:
        guess = input("Guess a letter!\n")
        showword = ""
        if guess in randomword:
            print("Yes correct")
            for i in randomword:
                if guess == i:
                    showword += guess
                    guessedletters += guess
                elif i in guessedletters:
                     showword += i
                else:
                    showword += "_"
            if "_" not in showword:
                 gameover = 6
                 print("You've won")
            print(showword)
            print(stages[stagecounter])

        else:
            print("incorrect")
            gameover += 1
            stagecounter -= 1
            print(stages[stagecounter])

print("gameover")
print(showword)
