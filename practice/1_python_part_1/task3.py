"""
Write function which receives list of text lines (which is space separated words) and word number.
It should enumerate unique words from each line and then build string from all words of given number.
Restriction: word_number >= 0
Examples:
    >>> build_from_unique_words('a b c', '1 1 1 2 3', 'cat dog milk', word_number=1)
    'b 2 dog'
    >>> build_from_unique_words('a b c', '', 'cat dog milk', word_number=0)
    'a cat'
    >>> build_from_unique_words('1 2', '1 2 3', word_number=10)
    ''
    >>> build_from_unique_words(word_number=10)
    ''
"""
from typing import Iterable
from ordered_set import OrderedSet

def build_from_unique_words(*lines: Iterable[str], word_number: int) -> str:
    if lines:
        inter = list(lines)
        i = 0
        result = []
        while i < len(inter):
            y = inter[i]
            part = y.split(' ')
            result.append(part)
            i += 1
        answer = []
        for each in result:
            data = list(OrderedSet(each))
            for key in data:
                if key:
                    if data.index(key) == word_number:
                        answer.append(key)
            total = ' '.join(answer)
        if total:
            return '{}'.format(total)
        else:
            print("''")
    else:
        print("''")
