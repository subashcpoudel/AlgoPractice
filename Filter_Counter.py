#Filter and count list of items

#Fruits List
items = ["Apple", "Mango", "Banana", "Orange", "Pear", "Mango", "Apple", "Banana", "Pear", "Banana", "Apple", "Apple", "Pear", "Mango"]


filter = dict()

for item  in items:
    if (item in filter.keys()):
        filter[item] += 1
    else:
        filter[item] = 1

print(filter)