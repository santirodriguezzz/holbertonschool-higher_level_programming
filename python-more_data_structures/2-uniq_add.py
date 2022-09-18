#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_nums = []
    result = 0
    for i in my_list:
        found = False
        for x in uniq_nums:
            if i is x:
                found = True
        if found is False:
            uniq_nums.append(i)
            result += i
    return result
