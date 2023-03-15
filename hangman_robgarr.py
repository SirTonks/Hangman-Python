import random
import time

print("""
_|    _|                                                                    
_|    _|    _|_|_|  _|_|_|      _|_|_|  _|_|_|  _|_|      _|_|_|  _|_|_|    
_|_|_|_|  _|    _|  _|    _|  _|    _|  _|    _|    _|  _|    _|  _|    _|  
_|    _|  _|    _|  _|    _|  _|    _|  _|    _|    _|  _|    _|  _|    _|  
_|    _|    _|_|_|  _|    _|    _|_|_|  _|    _|    _|    _|_|_|  _|    _|  
                                    _|                                      
                                _|_|





""")
time.sleep(1)

class StickMan:

    def visual(self, guesses):
        if (guesses == 6):
            return("""
                            ___________
                            |
                            |
                            |
                            |
                            |
                            |
                            |__________""")
        if (guesses == 5):
            return("""
                            ___________
                            |
                            |
                            |
                            |
                            |
                            |
                            |__________""")
        elif (guesses == 4):
            return("""
                            ___________
                            |     |
                            |
                            |
                            |
                            |
                            |__________""")
        elif (guesses == 3):
            return("""
                            ___________
                            |     |
                            |    (_)
                            |
                            |
                            |
                            |__________""")
        elif (guesses == 2):
            return("""
                            ___________
                            |     |
                            |    (_)
                            |    \|/
                            |
                            |
                            |__________""")

        elif (guesses == 1):
            return("""
                            ___________
                            |     |
                            |    (_)
                            |    \|/
                            |     |
                            |
                            |__________""")
        elif (guesses == 0):
            print("""
                            ___________
                            |     |
                            |   (x_x)
                            |    \|/
                            |     |
                            |    / \\
                            |__________""")
            res = input("Play again? \n [y] or [n] \n> ")
            if res == "y":
                time.sleep(1)
                print("\n\nGood luck!\n\n")
                time.sleep(1)
                play.obtain_word()
            if res == "n":
                time.sleep(1)
                print("Thanks for playing!")
                exit()
            else:
                self.visual(guesses)

class Play_Game:

    def obtain_word(self):
        create = Create_Word()
        create.get_word_length()
        word = create.word_selection
        guesses = 6
        guessed_letter = []
        stick = StickMan()
        while guesses > 0:
            print("===============================================================")
            print("==========",guesses,"========== GUESSES ========== REMAINING ==========" )
            print("===============================================================")
            print(stick.visual(guesses))
            print("\nYour word: ")
            for i in word:
                if i in guessed_letter:
                    print(i, end=" ")
                else:
                    print("_", end=" ")
            print(" ")
            guess = input ("\nPlease guess a letter: ").lower()
            if len(guess) == 1 and guess.isalpha():
                if guess in guessed_letter:
                    time.sleep(1)
                    print("\n\n",guess,"has already been guessed. Please try again.\n\n")
                    time.sleep(1)
                elif guess not in word:
                    print("\n\nINCORRECT!\n\n")
                    guessed_letter.append(guess)
                    guesses -= 1
                    time.sleep(1)
                else:
                    time.sleep(1)
                    print("\n\nYES!\n\n")
                    time.sleep(1)
                    guessed_letter.append(guess)
            else:
                print("Invalid input. Please try again.")
        if guesses < 1:
            print("Oh no, you lost!\n\nThe word was:", create.word_selection)
            print(stick.visual(guesses))

class Create_Word:

    def __init__(self):
        self.word_selection = ()

    def get_word_length(self):
      res = input("Select your word length: \n[a] SMALL (3-5 letters) \n[b] MEDIUM (6-8 letters)  \n[c] HARD (9+ letters) \n>")
      if res == "a":
         time.sleep(1)
         time.sleep(1)
         self.small_word()
      elif res == "b":
          time.sleep(1)
          time.sleep(1)
          self.medium_word()
      elif res == "c":
          time.sleep(1)
          time.sleep(1)
          self.large_word()
      else:
	      print("\n\nIncorrect Entry. Please try again!\n")
	      return self.get_word_length()

    def small_word(self):
        word_list = ["ash", "shy", "bus", "gas", "rub", "food", "soap", "gear", "thaw", "fish", "dress", "final", "dream", "cable", "price"]
        self.word_selection = (random.choice(word_list))
        return self.word_selection

    def medium_word(self):
        word_list = ["amazon", "locate", "carbon", "weapon", "flower", "clinic", "embark", "bracket", "brother", "offense", "network", "feeling", "concern", "addition", "vertical", "folklore", "referral", "addicted", "assembly", "traction" ]
        self.word_selection = (random.choice(word_list))
        return self.word_selection

    def large_word(self):
        word_list = ["breakfast", "marketing", "reception", "precision", "executive", "fisherman", "hilarious", "promotion", "announcement", "operational", "consultation", "application", "nationalism", "strikebreaker", "competition", "headquarters", "infrastructure", "communication", "civilization", "anticipation" ]
        self.word_selection = (random.choice(word_list))
        return self.word_selection

# Call the game
play = Play_Game()
play.obtain_word()

