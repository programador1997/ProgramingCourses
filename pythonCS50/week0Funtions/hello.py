#comment one line in py

"""
multiple 
lines 
comments
"""
#print("hello, World")

# create variable name with the input of the user
#u can convine the fintions 
name = input("What's ur name? ").strip().title()

#split user's name into first name and last name in two new varialbes
first, last =name.split(" ")


# remove whiteespace from str
#name = name.strip()

# capitalice the first word of the str
#name = name.capitalize()

# capitalice the first letter of all words of the str
#name = name.title()

# show in console a greating and the name input by the user in concatenetion "+" 
#print ("hello, " + name)

# show in console a greating and the name input by the user with two arguments divided by the ","
#print ("hello,", name)

#override the funtion print it modify the end of the print insted of making a jump of line it make nothnig
#print("Hello, ", end='')
#print(name)

#print with "" int the console
#print("hello, , \"friend\" ")

#if you add and "f" in the beginig of the stream and put the variable bethen brackets {} it thake the str as a varialbe
print (f"hello,  {first}, {last}")
