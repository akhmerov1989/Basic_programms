# Using the update method

dict_1 = {'a': 1, 'b': 2}
dict_2 = {'c': 3, 'd': 4}

dict_1.update(dict_2)
print("Merged dictionary(update): ", dict_1)

# Using dictionary unpacking

dict_1 = {'a': 1, 'b': 2}
dict_2 = {'c': 3, 'd': 4}

merged_dict = {**dict_1, **dict_2}
print("Merged dictionary(unpacking): ", merged_dict)
