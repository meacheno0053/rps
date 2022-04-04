# Version 3 - checks that response is in a given list


# Funtions go here
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
        return response

    #output error if item not in list
    print(error)
    print()
    
# Main routine goes here


# list for checking responses
rps_list = ["rock", "paper", "scissors", "xxx" ]

# Loop for testing purposes
user_choice = ""
while user_choice != "xxx":
  
  # Ask user for choice and check it's valid
  user_choice = choice_checker("chose rock / paper / "
                               "scissors (r/p/s): ", rps_list, 
                               "please chose form rock / paper / "
                               "scissors (or xxx to quit)")
 
  # Print out choice for comparison purpose
  print("you chose {}".format(user_choice))
 