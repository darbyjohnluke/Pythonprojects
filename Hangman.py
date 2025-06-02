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
word_list = ["python", "keyboard", "hangman", "developer", "function", "variable", "syntax", "compile",
    "debug", "algorithm", "network", "program", "boolean", "integer", "iterate", "object",
    "package", "script", "tuple", "runtime", "command", "string", "console", "lambda",
    "virtual", "binary", "process", "execute", "server", "client", "module", "desktop",
    "version", "thread", "storage", "gateway", "pointer", "webpage", "session", "router",
    "kernel", "window", "library", "syntax", "dynamic", "integer", "hardware", "monitor",
    "browser", "address", "cookie", "compile", "session", "update", "archive", "cluster",
    "feature", "encrypt", "access", "system", "syntax", "record", "mobile", "string",
    "backup", "upload", "download", "cache", "script", "input", "output", "random",
    "pythonic", "numeric", "networking", "login", "logout", "reboot", "firewall", "storage",
    "keyboard", "execute", "monitor", "database", "host", "domain", "function", "array",
    "index", "value", "stack", "queue", "class", "method", "return", "import",
    "global", "local", "nested", "parameter", "argument", "keyword", "boolean","loop"
]

logo = r''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

print(logo)
randomword = random.choice(word_list)
gameover = 0
guessedletters = []
while gameover < 6:
        showword = ""
        guess = input("Guess a letter!\n")
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
            print(stages[stagecounter])
            print(showword)

        else:
            print("incorrect")
            for i in randomword:
                if guess == i:
                    showword += guess
                    guessedletters += guess
                elif i in guessedletters:
                     showword += i
                else:
                    showword += "_"
            gameover += 1
            stagecounter -= 1
            print(stages[stagecounter])
            print(showword)

            
if gameover == 6:
     print(randomword)
print("gameover")
print(showword)
