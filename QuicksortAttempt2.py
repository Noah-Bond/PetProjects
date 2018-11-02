import random
def quicksort(alist):
    if len(alist) <= 1:
        return alist
    else:
        x = random.randint(0,len(alist)-1)
        llist = []
        rlist = []
        for item in alist:
            if item == alist[x]:
                if item in llist:
                    rlist.append(item)
                    #print(f"Duplicate {item} added to rlist")
                else:
                    llist.append(item)
                    #print(f"appended {item} to llist")
            if item < alist[x]:
                llist.append(item)
                #print(f"appended {item} to llist")
            elif item > alist[x]:
                rlist.append(item)
                #print(f"appended {item} to rlist")
        #print(alist[x])
        #print(llist)
        #print(rlist)
        return quicksort(llist) + quicksort(rlist)
#print(quicksort([5,6,20,11,7,2,14,70,1,69,700,20,4,53]))

def randomlistgenerator(num):
    randomlist = []
    for i in range(num):
        randomlist.append(random.randint(0,300))
    return randomlist

anum = int(input("Please input a number."))
print(quicksort(randomlistgenerator(anum)))
# I wrote this in response to a video I saw on TedEd concerning the fastest way to sort a series of books. 
# Of the three methods they used in the video, this is the one I liked the most, so I decided I'd try and work it out myself.
# Friday, November 2, 2018
