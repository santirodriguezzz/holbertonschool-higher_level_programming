#!/usr/bin/python3
def common_elements(set_1, set_2):
    comm = []
    for i in set_1:
        for x in set_2:
            add_elem = False
            for o_elem in comm:
                if o_elem is x:
                    add_elem = True
            if i is x and add_elem is False:
                comm.append(x)
    return comm
