my_dict = {
    'a': 10,
    'b': 20,
    'c': 10,
    'd': 30,
    'e': 20
}
uni_val = set()

for i in my_dict.values():
    uni_val.add(i)

unique_value_list = list(uni_val)

print("Unique values in the dictionary: ", unique_value_list)