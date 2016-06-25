houses = []
test_cases = input()
sum = []
for ts in range(test_cases):
    total=0
    no_of_houses,exponent_k = [int(i) for i in raw_input().split()]
    #print "no of houses",no_of_houses
    #print "exponent value",exponent_k
    #for noh in range(no_of_houses):
    houses = [int(i) for i in raw_input().split()]
    #print "houseslist: ",houses
    for i in range(houses.__len__()):
        #print houses.index(houses[i])
        if houses.index(houses[i]) == 0:
            #print "value of sum before at start of first element",total
            keyf=i+1
            while(keyf < houses.__len__() ):
                total = total + abs((houses[i]-houses[keyf]))**exponent_k
                keyf = keyf+1
        elif houses.index(houses[i]) > 0 and houses.index(houses[i]) < (houses.__len__()-1):
            #print "value of sum before at start of middle element",total
            keyb=i-1
            keyf=i+1
            while(keyb >= 0):
                total = total + abs((houses[i]-houses[keyb]))**exponent_k
                keyb = keyb - 1
            while(keyf < houses.__len__()):
                total = total + abs((houses[i]-houses[keyf]))**exponent_k
                keyf = keyf + 1
        elif houses.index(houses[i]) == (houses.__len__()-1):
            #print "value of sum before at start of last element",total
            keyb = i-1
            while(keyb >= 0):
                total = total + abs((houses[i]-houses[keyb]))**exponent_k
                keyb = keyb - 1
    sum.append(total)
for ts1 in range(test_cases):
    print sum[ts1]


