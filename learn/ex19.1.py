def last_week(var1, var2, ques):
    print("We had %d views last week." % var1)
    print("People touched %d times." % var2)
    print("That equals %d touches per view." % (var2 / var1))
    print("This is what you think about that: %s" % ques)

views = int(input("How many views? "))
touches = int(input("How many touches? "))
thoughts = input("What do you think about that? ")

last_week(views, touches, thoughts)
