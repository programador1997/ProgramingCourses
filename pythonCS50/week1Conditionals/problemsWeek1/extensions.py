def main():
    file = input("File name: ")
    checkExtension(file)

def checkExtension(data):
    last = len(data)
    extr = last - 4
    print(last[extr])
    """
    match extension:
        case ".gif ":
            print("image/gif")
        case ".jpg ":
            print("image/jpg")
        case ".jpeg" :
            print("image/jpeg")
        case ".png ":
            print("image/png")
        case ".pdf ":
            print("application/pdf")
        case ".txt ":
            print("text/plain")
        case ".zip ":
            print("application/zip")
        case _:
            print("application/octet-stream ")

    """
main()