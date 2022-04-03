# Version 2 - error message included when calling function


# Funtions go here
def choice_checker(question, valid_list, error):
 
  valid = False
  while not valid:
    
    # Ask user for choice (and put choice in lowercase)
    response = input(question).lower()

    #iterates through list and if response is an item
    #in the list (or the first letter of an item), the
    #full item name is returned        
    for item in vslid_list:
      if response == item [0] or response == item:
        return item

      #outpost error if item not in list

    if response == "r" or response == "rock":
      return response
    elif response == "p" or response == "paper":
      return response
    elif response == "s" or response == "scissors":
      return response

    #check for exit code...
    elif response == "xxx":
      return response
    else:
      print(error)
      
# Main routine goes here


# Loop for testing purposes
user_choice = ""
while user_choice != "xxx":
  
  # Ask user for choice and check it's valid
  user_choice = choice_checker ("chose rock / paper /"
                                "scissors (r/p/s): ", rps_list,
                                "please choose from rock / " 
                                "paper / scissors (or xxx to quit) ")


  # Print out choice for comparison purpose
  print("you chose {}".format(user_choice))