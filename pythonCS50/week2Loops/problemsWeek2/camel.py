def main():
    text = input("camelCase: ")
    camelCase_converter(text)

"""
funtions that take a str and checks if have a capital letter if does
return the same str with all letters in lower case and a _ after the letter 
make lower case si no solo regresa el str

a loop that checks all the char in the str and put tem in anoter str if finds a 
upercase letter it puts a _ and the the letter maker lowwer 
"""

def camelCase_converter(text):
    new_text = ""
    for letter in text:
        if letter.isupper():
            new_text = new_text + "_"
            new_text = new_text + letter.lower()
        else:
            new_text = new_text + letter
    print(new_text)

main()