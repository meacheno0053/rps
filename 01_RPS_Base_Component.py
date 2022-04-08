import random

# Functions go here
def check_rounds():
  while True:
    response = input ("How many rounds: ")

    round_error = "Please typr either <Enter> " \
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

# Main routine goes here

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
rps_list = ["rock", "paper", "scisssors", "xxx"]

# Ask user if they have played before.
# If 'yes_no_listes', show instructions


# Ask user for # of rounds then loop...

rounds_played = 0 
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
    heading = "Continuous Mode: Round {}".format(rounds_played +1)
  else:
    heading = "Round {} of {}".format(rounds_played + 1, rounds)    

  
  print(heading)
  choose_instruction = "Please choose rock (r), paper (p),scissors (s)"

  choice_error = "Please choose from rock " \
                  "paper / scissors (or xxx to quit)"
  
  # Ask user for choice and check it's valid
  user_choice = choice_checker("chose rock / paper / "
                               "scissors (r/p/s): ", rps_list, 
                               "please chose form rock / paper / "
                               "scissors (or xxx to quit)")


  # End game if exit code is typed
  if user_choice == "xxx":
    break

  # **** rest of loop / game ****
  print("You chose {}".format(user_choice))

  rounds_played += 1

  # end game if requested # of rounds has been played
  if rounds_played == rounds:
    break

# Ask user if they want to see their game history.
# If 'yes' show game history

#show game statistics