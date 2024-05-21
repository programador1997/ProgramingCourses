

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

    def is_valid(s):
        print(f"first two: {s[0:2]}")



"""

def is_valid(s):
    i = 0
    flag_isdigit = False
    valid = 0
    for char in s:
        i += i
        #“All vanity plates must start with at least two letters.”
        if i == 1:
            if not char.isalpha():
                return False
        if i == 2:
            if not char.isalpha():
                return False

        #“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
        if i >= 7:
            return False
        if i < 2:
            return False
        #“No periods, spaces, or punctuation marks are allowed.”
        not_allowed = " .,áéíóúÁÉÍÓÚ-/_:;*-+"
        if char in not_allowed:
            return False
    
        
        “Numbers cannot be used in the middle of a plate; they must come at the end.
        For example, AAA222 would be an acceptable … vanity plate;
        AAA22A would not be acceptable. The first number used cannot be a ‘0’.”

        
        if flag_isdigit:
            if char.isalpha():
                return False
            
        if char.isdigit():
            flag_isdigit = True
        
"""
    
        
main()
