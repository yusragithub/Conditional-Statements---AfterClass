number = int(input("Enter your marks: "))
attendance = int(input("Enter your attendance: "))
if number > 60 :
    if attendance > 75 :
        print("You are pass")
    elif attendance == 75 :
        print("You secured passing marks")
    else :
        print("You secured passing marks but didn't secure passing attendance")
elif number == 60 :
    print("You secured passing marks")
else :
    print("You didn't secured passing marks")