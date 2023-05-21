def dayOfProgrammer(year):
    # Write your code here
    days = 31 + 0 + 31 + 30 + 31 + 30 + 31 + 31
    if year >= 1700 and year <= 2700:
         if year == 1918:
             days += 15
         if year <= 1917:
             if year % 4 == 0:
                 days += 29
             else:
                 days += 28
         if year >= 1919:
             if year % 400 == 0 or (year % 4 == 0 and not year % 100 == 0):
                 days += 29
             else:
                 days += 28
    day = 256 - days
    print(f"{day}.09.{year}")
    #return f"{day}.09.{year}"
    
dayOfProgrammer(1918)
