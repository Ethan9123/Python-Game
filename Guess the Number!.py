# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import simplegui
# helper function to start and restart the game
k = 0
# k is a variable to determine if we should use range100
# and if we should use a Blank line before new game

def new_game():
    # initialize global variables used in your code here
    global count, secret_number, k, low, high, x 
    if k == 2:
        count = 10
        x = 1000
        print
        k = 2
    elif k <= 1:
        count = 7
        x = 100
        if k == 1:
            print
        else:
            k = 1
    secret_number = random.randrange(0, int(x))
    low = 0
    high = x
    print "New game. The range is from 0 to", x
    print "The number of remaining guesses is", count

# define event handlers for control panel
def range100():
    global k
    k = 1
    new_game()
    # make sure every time click range100 button to start a new game
    return 
# button that changes the range to [0,100) and starts a new game

def range1000():    
    global k
    k = 2
    new_game()
    # make sure every time click range1000 button to start a new game
    return 
# button that changes the range to [0,1000) and starts a new game 
    
def input_guess(guess):
    # main game logic goes here	
    global count, secret_number
    guess = int(guess)
    print
    print "Guess was", guess 
    count -= 1
    if guess != secret_number:
        print "The number of remaining guesses is", count 
        if count == 0:
            print "You ran out of guesses. The number was" , secret_number
            count -= 2
        #situation when lose the game 
    if count >= 0:
        if guess < secret_number:
            print ("higher!")
        elif guess > secret_number:
            print ("lower!")
        elif guess == secret_number:
            print ("Correct!")
            count = -1 
            #stop the function when correct 
        else:
            print ("error")
    #imply the relationship between input and answer
    if count < 0.5:
        new_game()
    #make sure start a new game when get "correct" or "lose"

###################################################
def cheat():
    global low, high, guess
    guess = int((high +low)/2)
    input_guess(guess)
    if guess < secret_number:
        low = guess 
    elif guess > secret_number:
        high = guess
#extra code for saving your time by using binary search.        
###################################################
frame = simplegui.create_frame("Guess the number", 200, 200)    
# create frame

frame.add_button("Range is (0:100)", range100, 200)
frame.add_button("Range is (0:1000)", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)

frame.add_button("Cheat", cheat, 70)
frame.start()

# register event handlers for control elements and start frame
new_game()
# call new_game
