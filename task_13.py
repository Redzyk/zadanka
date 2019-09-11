number = int(input("Please enter an integer: "))
print(f"These are the divisors of {number}:")
for element in range(0+1 ,number + 1):
    if number % element == 0:
        print (element)