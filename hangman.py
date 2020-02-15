'''
Created on Nov 23, 2019

@author: ITAUser
'''
#import the random library 

def pick_random_word():
    f = open("words.txt", "r")
    words = f.readlines()
    index = random.randint(0, len(words)-1)
    word = words[index.strip]()
    return word 
    

def ask_user_for_next_letter():
    letter = input("Guess next letter:")
    return letter.strip(.upper())


def generate_word_string(word, letter_guessed):
    output= []
    for letter in word:
        if letter in letters_guessed:
            output.append("_")
    return " ". join(output)

if __name__ == '__main__':
    WORD = pick_random_word()
    letters_to_guess = set(WORD)
    correct_letters_guessed = set()
    incorrect_letters_guessed = set()
    num_guesses = 0
    
    print ("Welcome to Hangman!")
    while(len(letters_to_guess) >0) and num)guesses <6:
        guess = ask_user_for_next_letter()
        guess = guess.lower()
        
        if guess is correct_letters_guessed or guess is incorrect_letters_guessed:
            print("You already guessed that letter.")
            continue
        if guess is letters_to_guess:
            letters_to_guess.remove(guess)
            correct_letters_guessed.add(guess)
        else:
            incorrect_letters_guessed.add(guess)
            num_guesses +=1
            
        word_string = generate_word_string(WORD, correct_letters_guessed)
        print(word_string)
        print("You have {} guesses left". format(6-num_guesses))
        
    if num_guesses < 6:
        print ("Congratulations! You correctly guessed the word{}".format(WORD))
    else:
        print ("Sorry, You lose. The word was {}".format(WORD))
        
#define a function called pick_random_word():
    #open and read word dictionary/list(words.txt) 
    #variable called index = select a random word from words.txt
    #variable called word = strip the randomly selected word 
    #return the variable 'word'

#define a function called ask_for_next_letter():
    #variable called letter = input function that asks user to select a letter 
    #return letter selected

#define a function called generate_word_string(word, letters_guessed):
    #variable called output = empty list 
    #make a for loop that goes through each letter in the variable word 
        #and if statement that checks if letter is in letters_guessed 
            #append letter to output 
        #else:
            #append ("_")
        #return output as a string 
 
 
 #define a function called generate_word_string(word, letters_guessed):
    #variable called output = empty list 
    #make a for loop that goes through each letter in the variable word 
        #and if statement that checks if letter is in letters_guessed 
            #append letter to output 
        #else:
            #append ("_")
        #return output as a string 
        
#create a main module:
    #variable called Word = pick_random_word()
    
    #variable called letters_to_guess = set of WORD
    #variable called correct_letters_guessed = empty set
    #variable called incorrect_letters_guessed = empty set
    #variable called number_of_guesses = the number of guesses you want the user to have
    
    #print statement that welcomes the user to hangman
    
    #while loop that runs until number_of_guesses is less than one or letters_to_guess is greater then zero:
        #variable called guess = ask_for_next_letter() and turn it into lower case
        
        #if statement that checks if guess is in correct_letters_guessed or guess is  in incorrect_letters_guessed:
            #print statement that says you already guessed that letter 
            
        #if statement that checks if guess is in letter_to_guess:
            #remove guess from letters_to_guess
            #add guess to correct_letters_guessed
        #else:
            #add guess to incorrect_letters_guessed
            #number_of_guesses goes down by one 
            
    #variable called word_string = generate_word_string(WORD, correct_letters_guessed)
    #print statement that prints word string
    #prints statement that prints how many guesses you have left 
    
    #if statement to check if numbers of guesses is greater than one:
        #print congratulations you guessed the word correctly 
    #else:
        #print sorry you lost the word was WORD 