# Using a recursive function to find maxumum value in list

items = [534,12,2,4,112,946,13,86,465,11,45]

def find_max(items):
    #breaking condition for recursion
    if(len(items)==1):
        return items[0]
    
    #Recursively call find_max without first element on the list
    op1 = items[0]
    op2 = find_max(items[1:])

    print("Op1 =" , op1)
    print("Op2 =" , op2)

    #When there are only two items on left
    if op1>op2:
        print("Big =" , op1,"\n")
        return op1
    else:
        print("Big =" , op2,"\n")
        return op2

print("Maximum value= ",find_max(items))