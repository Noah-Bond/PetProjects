import random
def eggdropfloors(floornum):
    mystery = random.randint(1,floornum)
    intcounter = 0
    tosscounter = 0
    x = 0
    while x < floornum:
        #print(math.factorial(intcounter))
        x = 0
        intcounter +=1
        for i in range(intcounter,0,-1):
            x += i   
    print(intcounter)
    currentfloor = 0
    while currentfloor < mystery:
        currentfloor += intcounter
        tosscounter+=1
    print(f'The first egg broke at {currentfloor}. We must have gone too far.')
    currentfloor -= intcounter
    while currentfloor < mystery:
        currentfloor += 1
        tosscounter += 1
        print(f"Egg didn't break at {currentfloor}")
    
    print(f'The most valuable egg you can steal is on floor {mystery}. It took {tosscounter} tosses to get there.')
    
