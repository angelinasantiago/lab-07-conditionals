myVar = input("What is your answer to my 1st question? (yes/no) ")
if myVar == "yes":
  myNextVar = input("What is your answer to my 2nd question? (yes/no) ")
  if myNextVar == "yes":
    print("No problem")
  elif myNextVar == "no":
    print("Then use duct tape!!!")
  else:
    print("Answer my question! You didn't type yes or no.")
elif myVar == "no":
  myNextVar = input("What is your answer to my 2nd question? (yes/no) ")
  if myNextVar == "yes":
    print("Then use WD-40.")
  elif myNextVar == "no":
    print("No problem.")
  else:
    print("Answer my question! You didn't type yes or no.")
else:
  print("Answer my question! You didn't type yes or no.")
                             
