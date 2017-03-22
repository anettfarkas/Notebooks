def while_function(answer, add):

    i = 0
    numbers = []

    while i < int(answer):
        print ("At the top i is %d" % i)
        numbers.append(i)
        print ("Numbers now: ", numbers)

        i = i + int(add)
        print ("At the bottom i is %d \n" % i)

        print ("The numbers: ")

        for num in numbers:
            print (num)


while_function(input("How many is too many? "), input("How many should we add? "))
