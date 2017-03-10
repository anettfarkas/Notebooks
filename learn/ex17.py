from sys import argv
from os.path import exists

script, from_file, to_file = argv

print ("Copying from %s to %s" % (from_file, to_file))

# in_file = open(from_file)
# indata = in_file.read()

# # We could do these two on one line:
in_file = open(from_file).read()

print ("The input file is %d bytes long" % len(in_file))

print ("Does the output file exist? %r" % exists(to_file))
print ("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(in_file)

print ("Alright, all done.")

out_file.close()
# in_file.close()
# When using open(from_file).read(), we don't need to type the extra close().
# It should already be closed by Python once that line runs.
