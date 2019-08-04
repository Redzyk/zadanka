def sentence(x):
    for element in x.split():
        if len(element)%2==0:
            print (element + " : has even number of letters")
        else:
            print ("W morde")

sentence("Piotrek jest słaby")