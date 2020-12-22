# check_for_duplicates(['B', 'D', 'F', 'B', 'M', 'N', 'N']) ['B', 'N']

def check_for_duplicates(items):
    """
    Return a list of duplicate items from passed in list
    """
    duplicates = []
    for item in items:
        if items.count(item) > 1:
            if item not in duplicates:
                duplicates.append(item)

    return duplicates
