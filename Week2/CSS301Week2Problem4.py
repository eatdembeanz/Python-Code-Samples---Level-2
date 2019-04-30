#Benjamin Page
#4/16/2019


#'banana' was misspelled, and should have been 'bananas'

#Length of dictionary 'd' is 4, because a fourth key was added to the list. The previous one had only three keys: apples, bananas, and grapes.

#'grapes' in d == True, because there IS an item named 'grapes' in dictionary 'd'.

#d['pears'] gives a KeyError, because there is no value assigned to 'pears', nor is 'pears' in the dictionary.

#d.get('pears', 0) returns '0', because the second part of the command (, 0) assigns a value of '0' to the key 'pears', even though neither are in the dictionary.

#fruits = d.keys() assigns a value equal to all the keys in the dictionary (apples, bananas, grapes, oranges) to the value 'fruits

#del d['apples'] deletes the key 'apples' in the dictionary, as well as its corresponding value.



def add_fruit(inventory, fruit, quantity):
    if fruit not in inventory:
       inventory[fruit] = quantity
    else:
        inventory[fruit] += quantity
    

new_inventory = {}
add_fruit(new_inventory, 'strawberries', 10)
print(new_inventory)

add_fruit(new_inventory,'strawberries',25)
print(new_inventory)
