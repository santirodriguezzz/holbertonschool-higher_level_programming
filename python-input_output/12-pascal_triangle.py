#!/usr/bin/python3
"""python interpreter"""


def pascal_triangle(n):
    """triangle"""
    megaList = []
    elem = [1]
    if n <= 0:
        return []

    for rows in range(n):
        miniList = [1]
        for num in range(rows):
            if num + 1 < len(elem):
                miniList.append(elem[num] + elem[num + 1])
            else:
                miniList.append(1)
                elem = list(miniList)
        megaList.append(miniList)
    return megaList
