"""
Write function which updates dictionary with defined values but only if new value more then in dict
Restriction: do not use .update() method of dictionary
Examples:
    >>> set_to_dict({'a': 1, 'b': 2, 'c': 3}, a=0, b=4)  # only b updated because new value for a less then original value
    {'a': 1, 'b': 4, 'c': 3}
    >>> set_to_dict({}, a=0)
    {a: 0}
    >>> set_to_dict({'a': 5})
    {'a': 5}
"""
from typing import Dict


def set_to_dict(dict_to_update: Dict[str, int], **items_to_set) -> Dict:
    if dict_to_update:
        for a, b in dict_to_update.items():
            if items_to_set:
                for x, y in items_to_set.items():
                    if x == a:
                        if dict_to_update[a] < items_to_set[x]:
                            dict_to_update[a] = items_to_set[x]
        print(dict_to_update)
    else:
        return items_to_set

