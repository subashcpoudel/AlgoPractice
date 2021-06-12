#Binary Search
items=[2,4,5,8,12,16,18,26,29,45,124,235,756,999]
print("List:             ",items, "\n")


def binarysearch(item,itemslist):
    listsize= len(itemslist)

    lowerIx = 0
    upperIx = listsize

    if(item > itemslist[upperIx-1] or item < itemslist[lowerIx]):
           return None

    while lowerIx <= upperIx:
        
        # Calculate Midpoint
        midpoint = (lowerIx + upperIx) // 2
        print ("Current midpoint = ", midpoint)

        #If item found 
        if itemslist[midpoint] == item:
            return midpoint
        
        #IF item not found, set new array to search on
        if item > itemslist[midpoint]:
            lowerIx = midpoint + 1
        else:
            upperIx = midpoint - 1
    return None
    


print("Item", 1,"found at index : ",binarysearch(1, items), "\n")
print("Item", 4,"found at index : ",binarysearch(4, items), "\n")
print("Item", 21,"found at index : ",binarysearch(21, items), "\n")
print("Item", 124,"found at index : ",binarysearch(124, items), "\n")
print("Item", 2000,"found at index : ",binarysearch(2000, items), "\n")

