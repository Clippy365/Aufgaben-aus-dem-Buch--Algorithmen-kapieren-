#!/usr/bin/python3

def binary_search(list, object):
    low = 0
    high = len(list) - 1

    if(object < list[low] or object > list[high]):
        return None
        
    while(low <= high):
        index = int((high-low)/2)

        if(object < list[index]):
            high = index
        if(object > list[index]):
            low = index + 1
        if(object == list[index]):
            return list[index]

my_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(binary_search(my_list, 1))
print(binary_search(my_list, 12))