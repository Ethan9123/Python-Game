# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    if name == "rock":
        o_number = 0
    elif name == "Spock":
        o_number = 1
    elif name == "paper":
        o_number = 2
    elif name == "lizard":
        o_number = 3
    elif name == "scissors":
        o_number = 4
    else:
        print("error")
    return o_number

    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    if number == 0:
        o_name = "rock"
    elif number ==1:
        o_name = "Spock"
    elif number == 2:
        o_name = "paper"
    elif number == 3:
        o_name = "lizard"
    elif number == 4:
        o_name = "scissors"
    else:
        print("error")
    return o_name
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
import random     

def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
    player_number = name_to_number(player_choice)
        # convert the player's choice to player_number using the function name_to_number()

    comp_number = random.randrange(0, 5)
        # compute random guess for comp_number using random.randrange()

        # convert comp_number to comp_choice using the function number_to_name()

    answer_n = (player_number - comp_number)%5
        # compute difference of comp_number and player_number modulo five

    if answer_n > 2.5:
        winner = "Computer"
    elif answer_n < 2.5 and answer_n != 0:
        winner = "Player"
            
    print("Player chooses " + number_to_name(player_number))
        # print out the message for the player's choice

    print("Computer chooses " + number_to_name(comp_number))
        # print out the message for computer's choice

    if answer_n == 0:
        print("Player and computer tie!")
        print
    elif answer_n != 0:
        print winner + " wins!"
        print 	 # print a blank line to separate consecutive games
    return
   

    # print out the message for the player's choice


    # use if/elif/else to determine winner, print winner message

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


