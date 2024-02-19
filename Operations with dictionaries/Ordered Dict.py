from collections import OrderedDict

ordered_dict = OrderedDict([('b', 2), ('c', 3), ('d', 4)])

new_item = ('a', 1)
new_ordered_dict = OrderedDict([new_item])
new_ordered_dict.update(ordered_dict)

print("Updated OrderedDict: ", new_ordered_dict)


def check_order(string, reference):
    string_dict = OrderedDict.fromkeys(string)
    reference_dict = OrderedDict.fromkeys(reference)

    return string_dict == reference_dict


input_string = 'Hello world'
reference_string = 'Helo wrd'

if check_order(input_string,reference_string):
    print("The order of char in the input matches reference")
else:
    print("No match")
