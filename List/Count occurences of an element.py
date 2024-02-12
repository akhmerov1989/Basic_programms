def count_occurrences(l, element):
    count = l.count(element)
    return count


mu_list = [1, 2, 3, 4, 5, 7, 8, 8, 5, 3, 3, 2, 2, 2, 3, 4, 5, 6, ]
element_to_count = int(input("Enter an element in a given list: "))

occurrences = count_occurrences(mu_list, element_to_count)
print(f"THe element {element_to_count} appears {occurrences} times in the list.")
