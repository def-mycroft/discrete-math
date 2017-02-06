import helpers

def violations(alist):
    """For ch2-11, calculates the number of violations"""
    count = 0
    for k in alist:
        add = False
        for i in helpers.list_combinations(k,2):
            if abs(i[0]-i[1]) < 2:
                add = True
        if add:
            count += 1

    return count

def ch2_37():
    letters = ['a','b','c','d','e','f']
    aset = []
    # Create the multiset
    for letter in letters:
        for i in range(12):
            aset.append(letter)

    return helpers.list_combinations(aset, 12, multiset=True)

