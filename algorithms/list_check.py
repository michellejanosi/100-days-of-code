'''
list_check([[],[1],[2,3], (1,2)]) # False
list_check([1, True, [],[1],[2,3]]) # False
list_check([[],[1],[2,3]]) # True
'''

def list_check(items):
    """
    Returns True if each value in the list is a list. Otherwise, returns False
    """
    # loop through item in the list 
    # check type of each item 
    # if the item type equals 'list' return True
    # if the item type does not equal 'list' return False

    for item in items:
        return all(type(item) == list for item in items)
