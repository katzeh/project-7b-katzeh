# Author: Catherine Cook
# GitHub username: katzeh
# Date: 5/10/2022
# Description: Project 7b - Write a function named reverse_list that takes as a parameter a list and reverses the order
# of the elements in that list. It should not return anything - it should mutate the original list.

def reverse_list(vals):
    """Takes list and reverses the order of the elements of that list"""
    first = 0  # This will be used to index the first element in the original list
    last = len(vals) - 1  # This will be used to index the last element of the original list

    while first < last:  # While the order of what was the last element of the original list is greater than the first
        newlist = vals[first]  # The new list contains the first object in the list
        vals[first] = vals[last]  # The first object in the list is mutated to be the last object in the list
        vals[last] = newlist  # The last object in the list begins the creation of the new list
        first = first + 1  # We move from the first object in the original list to the next
        last = last - 1  # We move from the last object in the original list to the next last
