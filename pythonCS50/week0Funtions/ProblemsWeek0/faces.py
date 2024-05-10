def main():
    text = (input())
    convert(text)

def convert(text):
    #implementation of convertion to emoji
    new_text = text.replace(":)", "\N{Slightly Smiling Face}")
    final_text =new_text.replace(":(", "\N{Slightly Frowning Face}")
    print(final_text)

main()