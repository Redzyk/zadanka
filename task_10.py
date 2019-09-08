def showNumbers(limit):
    for element in range(0, limit + 1):
        if element % 2 == 0:
            print(element, "EVEN")
        else:
            print(element, "ODD")


showNumbers(20)