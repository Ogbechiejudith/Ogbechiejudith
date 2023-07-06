
"""Judith Easter day finder
Easter day Finder """
def calculate_easter_date(year):

#Gauss Algorithm to calculate the date of Easter
    a = year % 19
    b = year // 100
    c = year % 100
    d = (19 * a + b - b // 4 - ((b - (b + 8) // 25 + 1) // 3) + 15) % 30
    e = (32 + 2 * (b % 4) + 2 * (c // 4) - d - (c % 4)) % 7
    f = d + e - 7 * ((a + 11 * d + 22 * e) // 451) + 114

    month = f // 31
    day = (f % 31) + 1


    return month, day

print("Welcome to Judith Easter day finder.")

while True:
     year = int(input("Enter a year: "))
     if year == year:
          month, day = calculate_easter_date(year)

          print("Easter Date:", month, "/", day)

          print("successful: Happy Easter ", month, "/",day ,"/",year,)

          print("Let the celebration begin")
          continue
     
     #Enter as many years as you wish
         


       

        
     



