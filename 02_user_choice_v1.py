# Funtions go here
def choice_checker(question):

  valid = False
  while not valid:
    
    # Ask user for choice 
    response = input(question)

    if response == "r" or response == "rock":
      return response


# Main routine goes here

# Ask user for choice and check it's valid
user_choice = choice_checker("chose rock / paper / scissore (r/p/s): ")


# Print out choice for comparison purpose