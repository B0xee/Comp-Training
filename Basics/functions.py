#Task
#Determine whether is leap year, True/False

def is_leap(year):
    leap = False
    # Write your logic here
    if year%4==0:
        if year%100==0 and year%400!=0:     # lol syntax
            leap=False
            return leap
        leap=True
    return leap

year = int(input())
print(is_leap(year))