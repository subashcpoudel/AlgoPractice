# demonstrate hashtable usage


# TODO: create a hashtable all at once
items1 = dict({"key1" : 1, "key2" : 2, "key3" : "Nepal"})
print (items1)

# TODO: create a hashtable progressively
items2 = {}
items2["key1"] = "Ram"
items2["key2"] = "Shyam"
items2["key3"] = "Hari"
print(items2)

# TODO: try to access a nonexistent key
#print(items1("key99"))

# TODO: replace an item
items1["key2"]="Pokhara"
print(items1)

# TODO: iterate the keys and values in the dictionary
for key, value in items2.items():
    print("Key: ", key,"Value: ", value)
