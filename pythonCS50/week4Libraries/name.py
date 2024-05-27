import sys
""""
get the list of the input 
try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")

correcting the index error
if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, my name is", sys.argv[1])
"""

"""
#check for errors and if have a error exit the program
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("hello, my name is", sys.argv[1])

#get slices of the list vith the : at the and of a list
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("hello, my name is", arg)

#get the secon to penultimate number
for arg in sys.argv[1:-1]:
    print("hello, my name is", arg)
"""