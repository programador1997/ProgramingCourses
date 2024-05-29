import emoji

def main():
    emoji = input("Input: ")
    emojizador(emoji)

def emojizador(emo):
    print(emoji.emojize(f'Python is {emo}'))

main()