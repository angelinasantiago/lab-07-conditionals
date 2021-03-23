usertime = int(input("What hour is it? (0-23)"))

if usertime <= 5:
    print("It's early. You should be sleeping!")
elif usertime <= 7:
    print("Time to go to work.")
elif usertime <= 9:
    print("You should be working!")
elif usertime <= 12:
    print("Take your lunch break!")
elif usertime <= 13:
    print("Do you feel that afternoon lull?")
elif usertime <= 17:
    print("Time to hit the gym…")
elif usertime <= 19:
    print("Gotta eat that dinner.")
elif usertime <= 21:
    print("Get that SLEEP. And rePEAT!")

else:
    print("You didn’t type an acceptable value! (0-23)")
