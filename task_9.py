def sum_of_multiples(x):
  numbers = range(0,x+1)
  elements_to_print = [element for element in numbers if element % 3 == 0 or element % 5 == 0]
  print(elements_to_print)
  return sum(elements_to_print)

print(sum_of_multiples(20))