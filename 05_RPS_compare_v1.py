# RPS Component 3 - compare user choice and computer choice
rps_list = ["rock", "paper", "scissors"]
comp_index = 0 
for item in rps_list:
  user_index = 0 
  for item in rps_list:
    user_choice = rps_list[user_index]
    comp_choice = rps_list[comp_index]
    user_index +=1

    # Compare options...
  if comp_choice == user_choice:
    result = "tie"
  elif user_choice == "rock" and comp_choice == "scissors":
    result = "won"
  elif user_choice == "paper" and comp_choice == "rock":
    result = "won"
  elif user_choice == "scissors" and comp_choice == "paper":
    result = "won"
  else:
    result = "loss"  

  if result == "tie":
    print("it's a tie")

  if result == "loss":
    print("it's a loss")

  if result == "won":
    print("you won")
    
    print("you chose{}, the computer chose {}.  "
         "\nResult: {}".format(user_choice, comp_choice, result))