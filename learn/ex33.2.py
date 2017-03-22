def while_function(answer):

    i = 0
    numbers = []

    while i < int(answer):
        print ("At the top i is %d" % i)

        for i in range (0, int(answer) + 1, 2):
            numbers.append(i)
            print ("Numbers now: ", numbers)
            print ("At the bottom i is %d \n" % i)

            for num in numbers:
                print (num)


while_function(input("How many is too many? "))
