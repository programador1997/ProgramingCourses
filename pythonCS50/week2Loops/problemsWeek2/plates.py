

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")






def is_valid(s):
    i = 0
    flag_isdigit = False
    valid = True
    #“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    if len(s) > 6:
        print("longer than 7")
        valid = False
    if len(s) < 2:
        print("shorter than 2")
        valid = False
    for char in s:
        i += i
        #“All vanity plates must start with at least two letters.”
        if i == 1:
            if not char.isalpha():
                print("first char is not letter")
                valid = False
        if i == 2:
            if not char.isalpha():
                print("second char is not letter")
                valid = False

        #“No periods, spaces, or punctuation marks are allowed.”
        not_allowed = " .,áéíóúÁÉÍÓÚ-/_:;*-+"
        if char in not_allowed:
            print(f"invalid caracter: {char}")
            valid = False
    
        """
        “Numbers cannot be used in the middle of a plate; they must come at the end.
        For example, AAA222 would be an acceptable … vanity plate;
        AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
        """    
        
        if flag_isdigit:
            if char.isalpha():
                print("a letter before a digit")
                valid = False
            
        if char.isdigit():
            flag_isdigit = True
            if char == "0":
                print("first digit is 0")
                valid = False

    return valid

    
        
main()
