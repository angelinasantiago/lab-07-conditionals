import datetime

# usertime = (input("What hour is it? (0-23)"))


now = datetime.datetime.now()
print (now.year, now.month, now.day, now.minute, now.second)

if usertime <= 5:
    print("It's early. You should be sleeping!")
elif usertime <= 7:
        print("It's early. You should be sleeping!")")
elif usertime <= 9:
    print("Time to go to work.")
elif usertime <= 12:
    print("You should be working!")

else:
    print("You didn’t type an acceptable value! (0-23)")
