def is_leap_year(a_year):
    leap = False
    if a_year % 400 == 0:
        leap = True
    if a_year % 100 == 0:
        leap = False
    if a_year % 4 == 0:
        leap = True
    return leap
a_year = 2400
if(is_leap_year(a_year)):
    print("Leap Year! Yay!")
else:
    print("Not a Leap Year :(")