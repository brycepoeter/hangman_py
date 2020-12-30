def validate_letter(s): 
    if len(s) == 1 and s.isalpha(): 
        return True 
    else: 
        return False    

def guess_letter(): 
    letter_guess = input('Guess a letter: ')
    while not validate_letter(letter_guess):
        letter_guess = input('That\'s not valid input. Please enter a single letter: ')  
    letter_guess_lower = letter_guess.lower()      
    return letter_guess_lower #returns lowercase to keep characters consistent for comparison

def guess_word(): 
    word_guess = input('Try to guess the word: ')
    return word_guess

def main(): 
    print('This file is not intended to run on its own. Try hangman.py')

if __name__ == '__main__': 
    main()    
