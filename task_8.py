weight = int(input("Weight: "))
while weight not in range(0,1001):
    print("Try again")
    break
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    conversion = int(weight // 0.45)
    print("Your weight is {} pounds".format(conversion))
if unit.upper() == "L":
    conversion = int(weight * 0.45)
    print("Your weight is {} kilos".format(conversion))
elif unit.upper() != "K" or "L":
    print("Please use K or L")