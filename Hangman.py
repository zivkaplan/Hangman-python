import os
import time
import random

def opening_screen():
  """
  the function prints the game logo and the number of tries the player has to guess
  :return: None
  """
  MAX_TRIES = 6
  HANGMAN_ASCII_ART = """
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/ \n"""
  print(HANGMAN_ASCII_ART)
  time.sleep(1)
  print("You have {} tries of failed attempts to guess.".format(MAX_TRIES))
  input("Press enter to continue.")
  os.system('cls')


def secret_word_select():
  """
  function asks the user for input and generates the secret word for the game.
  :return:the secret word for the game
  :rtype: string
  """
  animals = ["Bear", "Monkey", "Cat", "Dog", "Lizard", "Cow", "Tiger", "Lion", "Dolphin", "Whale",
             "Shark", "Beetle", "Duck", "Pig", "Butterfly", "Horse", "Donkey", "Zebra", "Lama",
             "Spider", "Wolf", "Mouse", "Chicken", "Peacock","Fish", "Giraffe", "Elephant", "Crocodile", "Bat", 
             "Camel", "Frog", "Fox", "Eagle", "Swan", "Snail", "Sheep", "Seal", "Rabbit", "Scorpion", "Rat", "Puma",
              "Panther", "Penguin", "Jellyfish", "Hamster", "Goat"]
  cars = ["Mazda", "Toyota", "Hyundai", "Dacia", "BMW", "Skoda", "volkswagen", "Mercedes", "Ferrari",
          "Maserati", "Mitsubishi", "Renault", "Peugeot", "Bugatti","Citroen", "Opel", "Porsche",
          "Smart", "Audi", "Jaguar", "Honda", "Volvo", "Kia", "Fiat", "Lamborghini", "Isuzu", "Lexus",
          "Nissan", "Subaru", "Daihatsu","Suzuki"]
  music_ins = ["Accordion", "Guitar", "Bagpipes", "Banjo", "Bassoon", "Bell", "Castanets", "Cello", "Clarinet",
               "Drumset", "Flute", "Harmonica", "Harp", "Kazoo", "Timpani", "Lute", "Mandolin", "trumpet", "Organ",
                "Oboe", "Piano", "Piccolo", "Recorder", "Sitar", "Triangle", "Tuba", "Ukulele", "Viola", "Violin",
               "Marimba", "Gong", "Xylophone", "Saxophone", "Trombone"]
  while True:
    subject_select = input("""please select a subject:
    1. Animals
    2. Cars
    3. Musical instruments
    type 1 \ 2 \ 3:\n""")
    try:
      if int(subject_select) == 1:
        print("You chose animals!\nOne moment please, we select the secret word...\n")
        secret_word = animals[random.randint(0,len(animals)-1)]
        break
      elif int(subject_select) == 2:
        print("You chose cars!\nOne moment please, we select the secret word...\n")
        secret_word = cars[random.randint(0, len(cars) - 1)]
        break
      elif int(subject_select) == 3:
        print("You chose musical instruments!\nOne moment please, we select the secret word...\n")
        secret_word = music_ins[random.randint(0, len(music_ins) - 1)]
        break
      else:
        print("wrong input!")
        continue
    except:
      print("wrong input!")
      continue

  time.sleep(1.5)
  print("The secret word was selected!\nGood Luck!")
  time.sleep(2)
  os.system('cls')
  return secret_word

def check_win(secret_word, old_letters_guessed):
    """
    checks if the secret word was guessed and user have won.
    :param secret_word: the word that the user is trying to guessing
    :param old_letters_guessed: the letters that the user has already guessed
    :type secret_word: str
    :type old_letters_guessed: list
    :return: if the user guessed all of the secret word letters
    :rtype: boolean
    """
    for i in secret_word:
      if i.lower() not in old_letters_guessed:
        return False
    return True

def show_hidden_word(secret_word, old_letters_guessed):
  """
  function that prints the hidden secret words as serious of dashes.
  if a letter is guessed by the user, it appears.
  starts if the user guessed
  :param secret_word: the word that the user is trying to guessing
  :param old_letters_guessed: the letters that the user has already guessed
  :type secret_word: str
  :type old_letters_guessed: list
  :return: None
  """
  for i in secret_word:
    if i.lower() in old_letters_guessed:
      print(i, end = ' ')
    else:
      print("_", end=' ')
  print("")

def check_valid_input(letter_guessed, old_letters_guessed):
  """
  the function checks is the user input is valid.
  Only 1 english character that does not appear in the old_letters_guessed list.
  :param letter_guessed: the guess input from the user
  :param old_letters_guessed: the letters that the user has already guessed
  :type letter_guessed: str
  :type old_letters_guessed: list
  :return: boolean
  """
  if (len(letter_guessed) >= 2) or (letter_guessed.isalpha() == False) or (
          letter_guessed.lower() in old_letters_guessed):
    return False
  else:
    return True

def try_update_letter_guessed(secret_word, letter_guessed, old_letters_guessed):
  """
  the function validates the user's input guess by calling "check_valid_input" function.
  option 1: invalid guess - print X and the old_letters_guesses list sorted.
  option 2: valid guess - adds it to the old_letters_guessed list.
   if the valid guess is wrong -  prints ":("
  :param secret_word: the word that the user is trying to guessing
  :param letter_guessed: the guess input from the user
  :param old_letters_guessed: the letters that the user has already guessed
  :type secret_word: str
  :type letter_guessed: str
  :type old_letters_guessed: list
  :return: determines if the users guess was valid and updates the old_letters_guessed list if needed
  :rtype: boolean
  """
  if check_valid_input(letter_guessed, old_letters_guessed):
    old_letters_guessed.append(letter_guessed)
    return True
  else:
    if old_letters_guessed == []:
      print("X")
    else:
      sorted_guessed = sorted(old_letters_guessed)
      print("X\n" + "You have already guessed: "+ " -> ".join(sorted_guessed))
    return False

def print_hangman(number_of_tries):
  """
  the function print the right hangman drawing for the remaining user's guessing tries.
  :param number_of_tries: the number of tries the user still has.
  :type number_of_tries: int
  :return: None
  """
  HANGMAN_PHOTOS = {1: """
  x-------x\n\n\n\n\n""",
    2: """
    x-------x
    |
    |
    |
    |
    |\n
    """,
    3: """
    x-------x
    |       |
    |       0
    |
    |
    |\n""",
    4:"""
    x-------x
    |       |
    |       0
    |       |
    |
    |\n""",
    5:"""
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |\n
    """,
    6:"""
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |\n
    """,
    7:"""
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |\n
    """}
  print(HANGMAN_PHOTOS[number_of_tries])

def play_again():
  """
  asks the player if he wants to play again or not.
  return a boolean that can keeps or stops the while loop that surrounds the main().
  :return: if the players wants to play again or not.
  :rtype: boolean
  """
  while True:
    play_again = input("would you like to play again? Y/N:\n")
    if play_again.lower() == 'y':
      os.system('cls')
      return True
      False
    if play_again.lower() == 'n':
      os.system('cls')
      return False
      False
    else:
      print("wrong input!")
      continue

def starting_position(secret_word, old_letters_guessed):
  """
  prints the first step of the game: the first hangman drawing, the secret word as blank lines.
  :param secret_word: the word that the user is trying to guessing
  :param old_letters_guessed: the letters that the user has already guessed
  :type secret_word: str
  :type old_letters_guessed: list
  :return: None
  """
  print_hangman(1)
  show_hidden_word(secret_word, old_letters_guessed)

def main():
  will_play_again = True
  while will_play_again == True:
    old_letters_guessed = []
    opening_screen()
    secret_word = secret_word_select()
    number_of_tries = 0
    is_playing = True
    starting_position(secret_word, old_letters_guessed)
    while is_playing:
        guessed_letter = input("Guess a letter: ")
        if not try_update_letter_guessed(secret_word, guessed_letter, old_letters_guessed):
          continue
        else:
          if guessed_letter not in secret_word.lower():
            number_of_tries += 1
            os.system('cls')
            print_hangman(number_of_tries + 1)
          if check_win(secret_word, old_letters_guessed):
            show_hidden_word(secret_word, old_letters_guessed)
            print("\nYOU WIN!")
            is_playing = False
            break
          show_hidden_word(secret_word, old_letters_guessed)
          if number_of_tries == 6 and not check_win(secret_word, old_letters_guessed):
            print("\nYOU LOSE!")
            is_playing = False
    time.sleep(1)
    will_play_again = play_again()

if __name__ == '__main__':
  main()