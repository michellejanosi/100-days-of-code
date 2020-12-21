'''
remove_every_other([1,2,3,4,5]) # [1,3,5] 
remove_every_other([5,1,2,4,1]) # [5,2,1]
remove_every_other([1]) # [1] 
'''


def remove_every_other(items):
    """
    Returns a new list with every second value removed.
    """
    # slice list starting at first item and skipping every other
    # return sliced list
    return items[::2]


print(remove_every_other([1]))
