import random

# Functions go here
def check_rounds():
  while true:
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
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scisssors", "xxx"]

# Ask user if they have played before.
# If 'yes_no_listes', show instructions


# Ask user for # of rounds then loop...


# Ask user if they want to see their game history.
# If 'yes' show game history

#show game statistics