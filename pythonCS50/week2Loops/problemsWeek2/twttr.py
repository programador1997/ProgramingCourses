def main():
    text = input("Input: ")
    converter(text)


def converter(text):
    vowels = "aeiouAEIOU"
    new_text = ""
    for letter in text:
        if letter not in vowels:
            new_text += letter
    print(new_text)

main()