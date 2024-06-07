def main():
    date = get_date()
    date = convert_date(date)
    print(date)

def get_date():
    while True:
        date_anno_domini = input("Date mm/dd/yyyy or month dd, yyyy: ")
        try:
            if "/" in date_anno_domini:
                mm, dd, yyyy = date_anno_domini.split("/")
                if mm > 12 and dd > 31:
                    print("invalid date")
            elif "," in date_anno_domini:
                ddmm, yyyy = date_anno_domini.split(",")
                dd , mm = ddmm.split(" ")
                

  
        except ValueError:
            ...
        return date_anno_domini

def get_month_number(month_name):
    months = {
        "january": 1,
        "february": 2,
        "march": 3,
        "april": 4,
        "may": 5,
        "june": 6,
        "july": 7,
        "august": 8,
        "september": 9,
        "october": 10,
        "november": 11,
        "december": 12
    }
    return months.get(month_name.lower())

def convert_date(valid_date):
    if "/" in valid_date:
        mm, dd, yyyy = valid_date.split("/")
    elif "," in valid_date:
        ddmm, yyyy = valid_date.split(",")
        mm, dd = ddmm.split(" ")
        mm = get_month_number(mm)

      
    mm = str(mm)
    dd = str(dd)
    yyyy = str(yyyy)

    return yyyy + "-" + mm +"-" + dd

main()