import datetime
current_year = datetime.datetime.now()
while True:
  name = input("Name: ")
  age = int(input("Age: "))
  print (f"""Your name is {name}.
You are {age} years old.""")
  year_of_turning_100 = current_year.year + (100 - age)
  print (f"You will turn 100 years old in {year_of_turning_100}.")