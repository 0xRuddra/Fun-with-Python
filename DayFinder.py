

""" You can find the day of the date between 1900-2100 ."""

import math
print("Do you want to know the Date of the given time you entered (1900-2100 ) .\n Let's find the date ->")
print("Enter the format: date-month-year.exp: 25-mar-2000,12-jan-2022")
date,month,year=input().split("-")
date,year=int(date),int(year)
if(len(month)>3):
    print("you have entered the wrong formated month: format: day-month(only 3 char)-year")
else:
    monthFormula = {
        "jan": 1,
        "feb": 4,
        "mar": 4,
        "apr": 0,
        "may": 2,
        "jun": 5,
        "jul": 0,
        "aug": 3,
        "sep": 6,
        "oct": 1,
        "nov": 4,
        "dec": 6,
    }
    dayFormula = {
        0: "Saturday",
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
    }

    yearCount = year - 1900
    if yearCount % 4 == 0:
        if month == "jan" or month == "feb":
            leapYearcount = (yearCount / 4) - 1
            mainFormula = yearCount + leapYearcount + date + monthFormula[month]
            yourDate = math.floor(mainFormula % 7)

            print(f"The day of the {date}-{month}-{year} is {dayFormula[yourDate]}")
            exit()

        else:
            leapYearcount = yearCount / 4
            mainformula = yearCount + leapYearcount + date + monthFormula[month]
            yourDate = math.floor(mainformula % 7)

            print(f"The day of the {date}-{month}-{year} is {dayFormula[yourDate]}")
            exit()


    else:
        leapYearcount = yearCount / 4
        mainformula = yearCount + leapYearcount + date + monthFormula[month]
        yourDate = math.floor(mainformula % 7)

        print(f"The day of the {date}-{month}-{year} is {dayFormula[yourDate]}")
        exit()



