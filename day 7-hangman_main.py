import random
from hangman_words import word_list
from hangman_art import logo, stages

lives = 6


print(logo)
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    #update on how many lives they have
    print(f"**************************** {lives}/6 LIVES LEFT****************************")
    s = input("Guess a letter: ")[0].lower()
    guess = ''.join(char.lower() for char in s if char.isalnum())

    # if they already guessed the word without reducing the life letting them know that they have already guessed it
    if guess in correct_letters:
        print(f"you have already guessed the letter:{guess}")

        
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"


    print("Word to guess: " + display)

    if guess not in chosen_word:
        print(f"you have guessed {guess},that's not in the word.You lose a life")
        lives -= 1

        if lives == 0:
            game_over = True

           #Give the user the coreect word they were trying to guess
            print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # displays the art or figure of the hangman
    print(stages[lives])
