import pandas as pd

def load_deck():
    """Loads the deck from csv"""
    # I tested these and the deck is actually unique.
    with open('set_board.csv', 'r') as f:
        deck = pd.read_csv(f)

    return deck


def check_same(attributes):
    """Returns True if lists are the same"""
    return attributes[:-1] == attributes[1:]


def check_different(attributes):
    """Returns True if every element is different"""
    s = set()

    for x in attributes:
        if x in s: return False
        s.add(x)

    return True


def check_for_set(color, shade, shape, quantity):
    """Checks for sets""" 
    is_set = False
    
    color_is_set = check_same(color) or check_different(color)
    shade_is_set = check_same(shade) or check_different(shade)
    shape_is_set = check_same(shape) or check_different(shape)
    quantity_is_set = check_same(quantity) or check_different(quantity)

    if color_is_set and shape_is_set and shade_is_set and quantity_is_set:
        is_set = True

    return is_set


def find_sets(verbose=False):

    count = 0
    deck = load_deck()

    for i in range(len(deck)):
        first_card = deck.iloc[i]
        first_index = i

        for k in range(len(deck)):

            if k != first_index:

                second_card = deck.iloc[k]
                second_index = k

                for n in range(len(deck)):

                    if n != second_index:
                        third_card = deck.iloc[n]

                        color = list([
                            first_card[0],
                            second_card[0],
                            third_card[0]
                            ])

                        shade = list([
                            first_card[1],
                            second_card[1],
                            third_card[1]
                            ])

                        shape = list([
                            first_card[2],
                            second_card[2],
                            third_card[2]
                            ])

                        quantity = list([
                            first_card[3],
                            second_card[3],
                            third_card[3]
                            ])

                        if check_for_set(color, shade, shape, quantity):
                            count += 1

                            if verbose:
                                print('#'*80)
                                print(count)
                                print(first_card)
                                print(second_card)
                                print(third_card)
                                print('#'*80)

    return count





