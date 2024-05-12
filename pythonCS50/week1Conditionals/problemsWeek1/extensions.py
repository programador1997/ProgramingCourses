def main():
    file = input("File name: ")
    checkExtension(file)

def checkExtension(data):
    if "." in data:
        split_data = data.split(".")
        second_data = split_data[1]

        print(second_data)
        match second_data:
            case "gif":
                print("image/gif")
            case "jpg":
                print("image/jpg")
            case "jpe" :
                print("image/jpeg")
            case "png":
                print("image/png")
            case "pdf":
                print("application/pdf")
            case "txt":
                print("text/plain")
            case "zip":
                print("application/zip")
            case _:
                print("application/octet-stream ")
    else:
        print("please introduce a file with extension")

    
main()