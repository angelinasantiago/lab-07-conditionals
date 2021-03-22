firstnum = int(input("Give me a number, any number..."))
secondnum = int(input("Wonderful, give me another number..."))
operation = input("And what operation do you want? (mul/div/mod)")

if operation == "mul":
    print(firstnum * secondnum)
elif operation == "div":
    print(firstnum / secondnum)
elif operation == "mod":
    print(firstnum % secondnum)
else:
    print("*** invalid operation! ***")
