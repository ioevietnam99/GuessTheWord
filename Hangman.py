import random
from words import hangman_list

# Function to get a random word

def get_word():   
   word = random.choice(hangman_list)
   return word.upper()

#Function to draw a Hangman

def draw_hangman(turn): # With 9 turn is for 9 stages of the draw
   draw=[      # full body  
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |      |
                   |      |
                   |     / \\
                   -----
                """,
                # head, full torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      |
                   |      |
                   |     / \\
                   -----
                """,
                # head, full torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      |
                   |      |
                   |      
                   -----
                """,
                # head, full torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |      |
                   |      |
                   |     
                   -----
                """,
                # head, fulltorso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |      |
                   |      |
                   |     
                   -----
                """,
                 # head, 3rd torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |      |
                   |      
                   |     
                   -----
                """,
                 # head, 2ndtorso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |      
                   |      
                   |     
                   -----
                """,
                # head - 1st torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |
                   |      
                   |      
                   |     
                   -----
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |
                   |
                   |      
                   |     
                   -----
                """,
                # no one here
                """
                   --------
                   |      |
                   |      
                   |    
                   |
                   |
                   |      
                   |     
                   -----
                """
    ]
   return draw[turn] # Return the value of Draw

# Function for game

def play_guess(word):
   turn = 9
   word_guessed = False # Initial for False
   guessed_letter = []  # Store guessed letter here
   guessed_word = [] # Store guess word here
   word_to_guess = "_" * len(word)
   word_listed=list(word)
   i = int(0)
    
   print("Welcome to Hangman Game") # Print the Welcome
   print(word_to_guess,"This word has:",len(word),"for you to guess. Good Luck !!!")  # Announce the number of word to guess
   print(draw_hangman(turn))  # Print the initial draw of Hangman, turn = 9
   print("-------------------------------------------") # Seperate
    
   # How the game run

   while not word_guessed and turn > 0:
      # Ask user to input while still playing

      guess = input("Please input the letter to guess or word: ").upper()
      
      # Guess letter

      if len(guess) == 1 and guess.isalpha():   # len(guess) == 1 equal to the input is a letter
           
         # Guess letter is in guessed_letter already
         
         if guess in guessed_letter:
            print("You already guess this letter", guess)
            
         # If guess wrong

         elif guess not in word_listed:
            print(guess, "is not in the word")
            turn -= 1   # Decrease the turn by 1
            guessed_letter.append(guess)  # Add guess to guessed_letter list
            
         # If guess correct

         else :
            print("Congratulation your guess:",guess,"is right")
            guessed_letter.append(guess)  # Add the guess letter to the guessed letter list
            for i in range(len(word_listed)):   # For loop that goes through each letter in word
               if word_listed[i] == guess :  # If guess in word it will replace the "_"
                  word_to_guess = word_to_guess[:i]+guess+word_to_guess[i+1:]
                  
                  # If statement to check if there is "_" in word_to_guess

                  if "_" not in word_to_guess:
                     word_guessed = True
                  
      # Guess word

      elif len(guess) == len(word) and guess.isalpha():

         # Guess word is in guessed_word already

         if guess in guessed_word:
            print("You already guess this word", word)
         
         # If guess wrong

         elif guess not in guessed_word:
            print(guess, "is not in the word")
            turn -=1
            guessed_word.append(guess)
         
         # If guess correct:

         else:
            print("Congratulation your guess: ",guess,"is correct")
            guess = True
            guess = word_to_guess
      
      # Invalid Guess
      
      else:
         print("Not a valid guess")

      print("You have",turn,"left")  
      print(word_to_guess) #print the current word after finish round
      print(draw_hangman(turn))  #print the current Hangman after finish round
      print("-------------------------------------------")


# The main of the game

def main():
   word = get_word()
   play_guess(word)
   print("The word to guess is", word)
   yes = ["YES","Y"]
   # Loop to ask player want to continue after first game
   
   while input("Do you want to play again: ").upper() in yes:
      word = get_word()   # Get a new word
      play_guess(word)  

main()
