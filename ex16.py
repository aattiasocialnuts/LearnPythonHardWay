from sys import argv

script, filename = argv

print "We're going to eraser %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURE."

raw_input("?")

print "Openning the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()


print "Now I'm going to ask you for three lines.."

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "I am going to write these to the file."

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)

lines = line1 + '\n' + line2 + '\n' + line3
target.write(lines)

print "And finally, we close it."
target.close()



