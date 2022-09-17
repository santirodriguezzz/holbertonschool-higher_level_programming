#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_element = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            new_element.append(replace)
        else:
            new_element.append(my_list[i])
    return new_element
