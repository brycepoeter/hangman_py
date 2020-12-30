from random_common_word import choose_random_word
from user_guess import guess_letter, guess_word

guesses_remaining = 5
letters_guessed = []
word_guessed = False 

# choose secret word 
secret_word = choose_random_word()
secret_lower = secret_word.lower()

#display _ _ _ _ for length of secret word 
def make_display_string(): 
    '''makes hangman display string using _ and right guesses'''
    display = ''
    for char in secret_lower: 
        if char in letters_guessed: 
            char_upper = char.upper()
            display += char_upper
            display += ' '
        else: 
            display += '_ '    
    print(display)        

#handle one round of the game
def handle_game_round(): 
    '''handles one round of hangman'''
    global letters_guessed
    global word_guessed
    print(f'Guesses remaining: {guesses_remaining} Guessed letters: {letters_guessed}')
    make_display_string()
    letter_guess = guess_letter()
    while letter_guess in letters_guessed: 
        print('You\'ve already guessed that one, silly!')
        print('Guessed letters:', letters_guessed)
        make_display_string()
        letter_guess = guess_letter()
    letters_guessed += letter_guess    
    if letter_guess in secret_lower: #test case of secret_word = 'I' led to secret_word and secret_lower
        print(f'You guessed right! {letter_guess.upper()} is in the word')
        make_display_string()
        word_guess = guess_word()
        if word_guess == secret_word or word_guess == secret_lower: 
            print(f'YOU WON!!! {secret_word} was the secret word')
            word_guessed = True 
        else: 
            print('Nope, that\'s not the word')
    else: #if letter guess not in secret_word 
        print('Nope! That\'s not in the word')        

#call handle_game_round and handle end-game logic 
def handle_game(): 
    '''calls handle_game_round for hangman and handles end-game logic'''
    global guesses_remaining
    global word_guessed
    while guesses_remaining > 0 and word_guessed == False: 
        handle_game_round()
        guesses_remaining -= 1
    if guesses_remaining == 0 and word_guessed == False: 
        print('Alright, you\'re all out of letter guesses')
        print('You get one shot at guessing the word')
        make_display_string()
        word_guess = guess_word()
        if word_guess == secret_word or word_guess == secret_lower: 
            print(f'HOLY MOLY YOU WON!!! YOU PULLED IT OFF! {secret_word} was the secret word')
        else: 
            print(f'Sorry! You lose :( Secret word was {secret_word}')        

def main(): 
    handle_game()

if __name__ == '__main__': 
    main()    





