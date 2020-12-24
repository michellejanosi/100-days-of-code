'''
sum_pairs([4,2,10,5,1], 6) # [4,2]
sum_pairs([11,20,4,2,1,5], 100) # []
'''


def sum_pairs(items, number):
    '''
    Return first pair of numbers that sum to the number passed to the function.
    '''
    # initiate variable to hold unique item from items
    # iterate items
    # if number minus item equals the number, return list of pair
    # otherwise, add item to value of checked items
    # if no pair adds up to number, return empty list
    checked = set()
    for item in items:
        difference = number - item
        if difference in checked:
            return [difference, item]

        checked.add(item)

    return []
