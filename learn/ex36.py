from sys import exit

def what_time(day):
    time = input("When? For lunch, during the afternoon, for dinner or afterwards? ")

    if "lunch" in time and day == "sunday":
        join_us("This is where we will be having lunch on Sunday: ")
    elif "lunch" in time and day == "monday":
        join_us("This is where we will be having lunch on Monday: ")
    elif "lunch" in time and day == "friday":
        join_us("This is where we will be having lunch on Friday: ")
    elif "lunch" in time and day == "thursday":
        join_us("This is where we will be having lunch on Thursday: ")

    elif "afternoon" in time and day == "sunday":
        join_us("This is where we will be Sunday afternoon: ")
    elif "afternoon" in time and day == "monday":
        join_us("This is where we will be Monday afternoon: ")
    elif "afternoon" in time and day == "friday":
        join_us("This is where we will be Friday afternoon: ")
    elif "afternoon" in time and day == "thursday":
        join_us("This is where we will be Thursday afternoon: ")

    elif "dinner" in time and day == "sunday":
        join_us("This is where we will be having dinner on Sunday: ")
    elif "dinner" in time and day == "monday":
        join_us("This is where we will be having dinner on Monday: ")
    elif ("dinner" in time or "evening" in time) and day == "friday":
        join_us("Please join us for a drink here anytime after 7:30pm: ")
    elif ("dinner" in time or "evening" in time) and day == "thursday":
        join_us("Start the festivities with us here: ")

def what_day():
    day = input("What day would you like to hang out with us? ").lower()

    if day == "sunday" or day == "monday" or day == "friday" or day == "thursday":
        what_time(day)
    else:
        join_us("Here are our plans for Thursday, Friday, Sunday and Monday: ")

def hang_out():
    hang_out = input("Would you like to hang out with us outside of the wedding? ")

    if "yes" in hang_out or "of course" in hang_out:
        what_day()
    elif hang_out == "no" or "can't" in hang_out:
        print ("Super excited to see you at the wedding!")
    else:
        hang_out = input("Please type yes or no: ")
        if hang_out == "yes":
            what_day()
        else: exit(0)

def bach_parties():
    print ("Select your gender:")
    print ("1. Female\n2. Male")

    gender = input("> ")

    if gender == "2":
        print ("Would you like to join Willem's bachelor party?")
        print ("1. Yes\n2. No")
        willem = input("> ")

        if willem == "yes" or willem == "1":
            print ("Amazing! This what you need to know: ")
            print ("One more question: ")
            hang_out()

        else:
            hang_out()

    elif gender == "1":
        print ("Would you like to join Anett's bachelor party?")
        print ("1. Yes\n2. No")
        anett = input("> ")

        if anett == "yes" or anett == "1":
            print ("Amazing! This what you need to know: ")
            print ("One more question: ")
            hang_out()

        else:
            hang_out()

def arrival():
    arrival_day = input("What day are you arriving to Budapest? ").lower()

    if arrival_day == "wednesday":
        bach_parties()
    else:
        hang_out()

def attending():
    print ("Hi there! Are you coming to celebrate our wedding with us in Budapest?")
    print ("1. Of course I am!")
    print ("2. Unfortunately I can't make it.")
    rsvp = input ("> ")

    if rsvp == "1":
        arrival()
    else:
        print("Sad to hear that. Hope we can celebrate together soon!")

def join_us(text):
    print(text, "Come join us!")
    exit(0)

attending()
