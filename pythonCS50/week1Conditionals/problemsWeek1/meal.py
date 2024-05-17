def main():
    time = input("What time is it? ")
    convert(time)

def convert(time):
    hour, minute = time.split(":")
    hour = int(hour)
    print(f"hour:  {hour}, min: {minute}")
    if hour >= 7 and hour < 8:
        print("breakfast time!!!")
    elif hour >= 12 and hour < 13:
        print("lunch time!!!")
    elif hour >= 18 and hour < 19:
        print("dinner time!!!")
    else:
        return


if __name__ == "__main__":
    main()

    """
    breakfast between 7:00 and 8:00, 
    lunch     between 12:00 and 13:00 
    dinner    between 18:00 and 19:00
    """