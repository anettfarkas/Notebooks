print ("It's snowday! Do you go sledding or stay inside?")

prompt = "Type your answer here: "
snowday = input(prompt)

if snowday == "sledding" or snowday == "Sledding":
    print ("Yay! Which park do you go to?")
    print ("1. Central Park")
    print ("2. Riverside Park")
    print ("3. Park Slope")

    park = input(prompt)

    if park == "1" or park == "1.":
        print ("Where's a good hill in Central Park?")

        cp_hill = input(prompt)

        if cp_hill == "I don't know" or cp_hill == "idk" or cp_hill == "not sure":
            print("Bummer. Would love to find a good hill in Central Park.")
        else:
            print("Nice! I'll have to go try it.")

    elif park == "2" or park == "2.":
        print("That's my favorite too!")
    elif park == "3" or park == "3.":
        print("Nice! I should go to Brooklyn to try sledding there sometime.")
    else:
        print ("That sounds like fun!")

elif snowday == "stay inside":
    print("What's your favorite thing to do inside on a snowday?")
    print("1. Drink tea\n2. Stay in bed\n\t3. Watch a movie")

    inside = input(prompt)

    if inside == "1" or inside == "2":
        print("Would love to be doing that right now.")
    else:
        print("I like doing that too.")

else:
    print("That's a good idea too!")
