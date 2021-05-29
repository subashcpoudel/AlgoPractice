# Implement a merge sort with recursion
def mergesort(dataset):
    print("Divide and conquer: ", dataset)
    if len(dataset) > 1:
        mid = len(dataset) // 2
        leftarr = dataset[:mid]
        rightarr = dataset[mid:]

        # TODO: recursively break down the arrays
        mergesort(leftarr)
        mergesort(rightarr)

        # TODO: now perform the merging
        i=0 # index into the left array
        j=0 # index into the right array
        k=0 # index into merged array

        # TODO: while both arrays have content
        while i<len(leftarr) and j< len(rightarr):
            if leftarr[i] > rightarr[j]:
                dataset[k] = leftarr[i]
                i+=1
            else:
                dataset[k] = rightarr[j]
                j+=1
            k+=1

        # TODO: if the left array still has values, add them
        while i < len(leftarr):
            dataset[k] = leftarr[i]
            i+=1
            k+=1

        # TODO: if the right array still has values, add them
        while j < len(rightarr):
            dataset[k] = rightarr[j]
            j+=1
            k+=1
    print("Current: ", dataset)

# test the merge sort with data
list = [3,8,5,95,77,18,32,54,42,39,91]
mergesort(list)
print("\n \nFinal Result: ", list)