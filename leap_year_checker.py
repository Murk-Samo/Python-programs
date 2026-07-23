leap_year_checker.

import calendar
while True:
  print("===Leap Year Checker===")
  year = int(input("Enter a year: "))
  if calendar.isleap(year):
    print(f"Yes {year} is a leap year.")
  else:
    print(f"No {year} is not leap year.")
  while True:
    again = input("Do you want to check again? (yes/no) ").lower()
    if again == "yes":
      break
    elif again == "no":
      print("Thanks.")
      exit()
    else:
      print("Enter only yes/no.")
      continue
