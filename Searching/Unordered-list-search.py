#Linear search

# Unordered list
items = [15, 30, 6, 29, 64, 34, 15, 53, 46, 63]

def find_item(item, itemlist):
    for i in range(0, len(items)):
        if item == itemlist[i]:
            return i
    return None


print(find_item(63, items))
print(find_item(250, items))
