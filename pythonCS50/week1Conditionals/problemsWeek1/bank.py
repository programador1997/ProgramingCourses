def main():
    greeting = input("Greeting: ")
    is_h(greeting)

def is_h(text):
    if text[0] == "h" or text[0] == "H":
        Iworld = text.split()
        if Iworld[0] == "hello" or Iworld[0] == "Hello":
            print("$0")
        else:
            print("$20")

    else:
        print("$100")

main()