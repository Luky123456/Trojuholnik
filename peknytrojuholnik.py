def trojuholnik(riadky):
    for i in range(riadky):
        for x in range(riadky-i-1):
            print(end=" ")
        for x in range(i+1):
            print("*",end=" ")
        print()
trojuholnik(8)