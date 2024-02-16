key_values_list = [('a',1),('b',2),('c',3),('d',4)]

flat_dict = {}

for key, value in key_values_list:
    flat_dict[key] = value

print("Flat dictionary: ", flat_dict)