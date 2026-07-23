table_generator.
while True:
  print("====TABLE GENERATOR====")
  number = int(input("Enter a number: "))
  for i in range(1, 11):
    print(number, "X", i, "=", number*i)
  again = input("Do you want to generate another table? ").lower()
  if again == "no":
    print("Thank you. ")
    break
  else:
    continue
