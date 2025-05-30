import random
word_list = ["aardvark", "baboon", "camel"]
randomword = random.choice(word_list)
gameover = 0
guessedletters = []
while gameover < 7:
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
                 gameover = 7
                 print("You've won")
            print(showword)

        else:
            print("incorrect")
            gameover += 1
print("gameover")
print(showword)