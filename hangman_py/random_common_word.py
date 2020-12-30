import random
import os

file_name = 'common_words.txt'
dir_name = os.path.dirname(__file__)
file_path = os.path.join(dir_name, file_name)

def process_file(file): 
    try: 
        f = open(file_path, 'r')
        all_words = []
        for line in f: 
            clean_line = line.strip()
            all_words.append(clean_line)
        f.close()
        return all_words
    except: 
        return 'That\'s not a file in this working directory'   

def choose_random_word(): 
    words = process_file(file_path)
    choice = random.choice(words)
    return choice 

def main(): 
    print('Here\'s a random common word:')
    choice = choose_random_word()
    print(choice)

if __name__ == '__main__': 
    main()    


