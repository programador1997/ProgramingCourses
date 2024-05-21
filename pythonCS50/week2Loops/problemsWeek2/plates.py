def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    i = 0
    for char in s:
        i += i
        if i == 1:
            if char.isalpha():
                ...
            else:
                return False
        if i == 2:
            if char.isalpha():
                ...
            else:
                return False

        if i >= 7:
            return False
        if i < 2:
            return False
main()

"""
“All vanity plates must start with at least two letters.”

“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”

“Numbers cannot be used in the middle of a plate; they must come at the end.
For example, AAA222 would be an acceptable … vanity plate;
AAA22A would not be acceptable. The first number used cannot be a ‘0’.”

“No periods, spaces, or punctuation marks are allowed.”
"""