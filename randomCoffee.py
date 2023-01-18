#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import random

print("Export Members by typing /who in the slack channel")
members_import = input("Enter members: \n")

# Split the input string into a list of members
members_list = members_import.split(', ')

# As the organizer, you can add your name here, so that you don't always need to manually add yourself to the list.

# Append "@YourSlackTag" to the list if it's not already in it
# if '@YourSlackTag' not in members_list:
#    members_list.append('@YourSlackTag')

# Remove "@RandomCoffee" from the list if it's in it
if '@RandomCoffee' in members_list:
    members_list.remove('@RandomCoffee')

# Initialize an empty list to store the pairs
pairs = []

# Print the number of members
print('Number of Members', len(members_list))

# Define a function to randomly pop an element from a list
def pop_random(lst):
    idx = random.randrange(0, len(lst))
    return lst.pop(idx)

# While there are more than one members in the list
while len(members_list) > 1:
    # Pop two random members from the list
    rand1 = pop_random(members_list)
    rand2 = pop_random(members_list)
    # Create a tuple representing the pair and append it to the pairs list
    pair = (rand1, "☕️", rand2)
    pairs.append(pair)

# If there's an odd number of members, add the remaining member to the last pair
if len(members_list) != 0:
    group = list(pop_random(pairs))
    group.extend(["☕️", members_list.pop(0)])
    pairs.append(tuple(group))

# Print the pairs in a formatted way
print('\n -', '\n - '.join([str(' '.join(i)) for i in pairs]))
