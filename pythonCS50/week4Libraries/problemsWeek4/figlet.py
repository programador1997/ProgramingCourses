import sys
import random
from pyfiglet import Figlet


figlet = Figlet()
fonts = figlet.getFonts()


def main():
    text = ""
    if len(sys.argv) == 3:
        #chech the commad for font
        if sys.argv[2] == "-f" or sys.argv[2] == "--font":
            print("goood -f  or -font encounter")
            s_font = sys.argv[3] 
            #ask for font
            text = input("Input: ")
            #check if font is in fonts
            for font in fonts:
                if font == s_font:
                    figlet.setFont(font=s_font)
                    print(figlet.renderText(text))
                    sys.exit()
            print("no valid font")
            sys.exit()
        else:
            #if there is not a valid flag
            print(f"{sys.argv[2]} is not a valid command")
            sys.exit()        
    elif len(sys.argv) == 1:
        #call rndFont and print with the funtions piglet
        text = input("Input: ")
        s_font = rndFont()
        figlet.setFont(font=s_font)
        print(figlet.renderText(text))
    else:
        print("not enough inputs ")
        sys.exit()

def rndFont():
    random.shuffle(fonts)
    for font in fonts:
        return font

main()