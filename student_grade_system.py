Student_grade_system.
while True:
  print("="*5, "STUDENT GRADE SYSTEM", "="*5)
  name = input("Enter student name: ")
  marks = int(input("Enter marks (0-100): "))
  if marks <100 and marks >=80:
    print("Grade: A")
  elif marks <80 and marks >=50:
    print("Grade: B")
  elif marks <50 and marks >=30:
    print("Grade: C")
  elif marks <30 and marks >=0:
    print("Grade: D")
  else:
    print("Invalid marks! ")
  while True:

    ask_again = input("Do you want to check again? (yes/no)").lower()
    if ask_again == "yes":
      break
    elif ask_again =="no":
      print("Thank you for using our system.")
      exit()
    else:
      print("Enter only yes or no.")
      continue
