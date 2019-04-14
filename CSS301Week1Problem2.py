#Benjamin Page
#4/9/2019

#Asks for a starting day number, the length of a stay (on vacation), and the day of the week you will return on.

WeekDay = -1
while WeekDay == -1: #As long as there isn't a valid value for the week day, asks the user to input a day.
    StartDay = input("Enter the day you are leaving (sunday, monday, etc.):")#Converts a string signifying a day into a value, that also terminates the while loop.
    if StartDay == "Sunday" or StartDay == "sunday":
        WeekDay = 0

    elif StartDay == "Monday" or StartDay == "monday":
        WeekDay = 1

    elif StartDay == "Tuesday" or StartDay == "tuesday":
        WeekDay = 2

    elif StartDay == "Wednesday" or StartDay == "wednesday":
        WeekDay = 3

    elif StartDay == "Thursday" or StartDay == "thursday":
        WeekDay = 4

    elif StartDay == "Friday" or StartDay == "friday":
        WeekDay = 5

    elif StartDay == "Saturday" or StartDay == "saturday":
        WeekDay = 6

    else:
        print("Error, please enter a valid day.")

StayLength = int(input("Enter how many days you will be staying."))

TotalLength = WeekDay + StayLength
EndDay = TotalLength % 7 #Divides the amount of days they will be staying out by 7, then finds the remainder to figure out which day of the week that will land on.
print("You will return on day",EndDay,"of the week you return.")

if EndDay == 0:
    print("That day is Sunday.")

elif EndDay == 1:
    print("That day is Monday.")

elif EndDay == 2:
    print("That day is Tuesday.")

elif EndDay == 3:
    print("That day is Wednesday.")

elif EndDay == 4:
    print("That day is Thursday.")

elif EndDay == 5:
    print("That day is Friday.")

elif EndDay == 6:
    print("That day is Saturday.")

