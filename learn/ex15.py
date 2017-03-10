from sys import argv

script, filename = argv

txt = open(filename)

print ("Here's your file %r:" % filename)
print (txt.read())

print ("Type the filename again for the first line of the file:")
file_again = input("> ")

txt_again = open(file_again)

print (txt_again.readline())

# Close files when done with them:
txt.close()
txt_again.close()
