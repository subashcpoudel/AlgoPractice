# Bubble sort algorithm


def bubbleSort(dataset):
    # TODO: start with the array length and decrement each time
    for i in range(len(dataset)-1, 0, -1):
        for j in range(i):
            if dataset[j] > dataset[j+1]:
                temp =  dataset[j]
                dataset[j] = dataset[j+1]
                dataset[j+1] = temp
                print(" Current state: ", dataset)
        

def main():
    list = [12, 2, 21, 9, 0, 36, 18, 1, 3, 12]
    print("Original State: ", list)
    bubbleSort(list)
    print("   Sort Result: ", list)


if __name__ == "__main__":
    main()
