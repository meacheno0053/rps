import random

# Functions go here...
def yes_no (question):
  valid = False
  while not valid:
    response = input(question).lower()
    print()
    if response == "yes" or response == "y": 
      print("-- You Chose Yes --")
      return "yes"
    
    elif response == "no" or response == "n": 
      return "no"
    
    else:
      print("Please answer yes / no")



def instructions ():
  print()
  print("**** How to Play ****")
  print()
  print("""

***** INSTRUCTIONS *****

Choose rock / paper / scissors

r - rock
p - paper
s - scissors

Rock beats Scissors
Scissors beats Paper
Paper beats Rock

Choose a number of rounds to play

        <-OR->
        
Press <ENTER> To Play Infinate Mode

Use 'xxx' to quit

Game Summary and History Will Be Displayed After The Game
        
Have fun! :)
        
        """)

  return ""


# Decoration
def statement_generator(statement, decoration, style):

  sides = decoration * 3

  statement = "{} {} {}".format(sides, statement, sides)
  top_bottom = decoration * len(statement)

  if style == 3:
  
    print(top_bottom)
    print(statement)
    print(top_bottom)
  else:
    print(statement)

  return ""

# Main Routine goes here
statement_generator("** Welcome To ROCK vs PAPER vs SCISSORS **", "*", 3)
print()
played_before = yes_no("?? have you played before? ??")
print()
if played_before == "no":
  instructions()
print()

   
# Functions go here
def check_rounds():
  while True:
    response = input ("<< How many rounds: >> ")

    round_error = "Please type either <Enter> " \
                  "or an integer that is more than 0\n"

    # if infinate mode not chosen, check response
    #is an integer more than 0 
    if response != "":
      try:
        response = int(response)
        
        # If response is too low, go back to start of loop
        if response <1:
          print (round_error)
          continue

      except ValueError:
        print(round_error)
        continue

    return response

      # If response is not an integer go back to start of loop


# Lists of valid responses


def choice_checker(question, valid_list, error):

  valid = False
  while not valid:
    
    # Ask user for choice (and put choice in lowercase)
    response = input(question).lower()

    #iterates through list and if response is an item
    # in the lisit (or the first letter of an item), the
    #full item name is returned

    for item in valid_list:
      if response == item[0] or response == item:
        return item

    #output error if item not in list
    print(error)
    print()
    
# Main routine goes here


# list for checking responses


yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

game_summary = []

# Ask user if they have played before.
# If 'no', show instructions


# Ask user for # of rounds then loop...
rounds_played = 0 

#intialise lost / drawn counters
rounds_drawn = 0
rounds_lost = 0

choose_instruction = "Please choose rock (r), paper " \
                     "(p) or scissors (s)"

# Ask user for # of rounds, <enter> for infinate mode
rounds = check_rounds()

end_game = "no"
while end_game =="no":

  # Start of game play loop
  
  # Rounds Heading
  print()
  if rounds =="":
    heading = "Infinate Mode: Round {}".format(rounds_played +1)
  else:
    heading = "Round {} of {}".format(rounds_played + 1, rounds)    
    
  
  print(heading)
  choose_instruction = "Please choose rock (r), paper (p),scissors (s)"

  choice_error = "Please choose from rock " \
                  "paper / scissors (or xxx to quit)"
  
  # Ask user for choice and check it's valid
  user_choice = choice_checker("choose rock / paper / "
                               "scissors (r/p/s): ", rps_list, 
                               "please choose form rock / paper / "
                               "scissors (or xxx to quit)")

  if user_choice == "xxx":
    break

  # get computer choice
  comp_choice = random.choice(rps_list[:-1])
  print("computer chose", comp_choice)

  # compare choices
  if comp_choice == user_choice:
    result = "tie"
    rounds_drawn += 1
  elif user_choice == "rock" and comp_choice == "scissors":
    result = "won"
  elif user_choice == "paper" and comp_choice == "rock":
    result = "won"
  elif user_choice == "scissors" and comp_choice == "paper":
    result = "won"
  else:
    result = "lost"  
    rounds_lost += 1

  if result == "tie":
    feedback = "Result: It's a tie"
  else:
    feedback = "{} vs {} - you {}".format(user_choice, comp_choice, result)

  outcome = "Round {}: {}".format(rounds_played + 1, feedback)
  game_summary.append(outcome)


  # Output results...
  print (feedback)

  rounds_played += 1
  # end game if requested # of rounds has been played
  if rounds_played == rounds:
    break

# Ask user if they want to see their game history.
# If 'yes' show game history

#show game statistics
    
# Quick calculations (stats)
rounds_won = rounds_played - rounds_lost - rounds_drawn

# end of game statements
print()
print('***** End Game Summary *****')
print("won: {} \t|\t Lost: {} \t|\t Draw: " 
      "{}".format(rounds_won, rounds_lost, rounds_drawn))
print()

print("***** Game History *****")
for game in game_summary:
  print (game)

print()

print("^^^ Thanks for playing ^^^")