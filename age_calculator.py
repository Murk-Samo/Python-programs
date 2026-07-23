age_calculator.

import datetime
print("===AGE CALCULATOR===")
current = datetime.datetime.now()
birth_year = int(input("What is your birthyear? "))
age = current.year - birth_year
print(f"You are {age} years old.")
