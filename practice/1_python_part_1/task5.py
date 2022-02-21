"""
Write function which receives line of space sepparated words.
Remove all duplicated words from line.
Restriction:
Examples:
    >>> remove_duplicated_words('cat cat dog 1 dog 2')
    'cat dog 1 2'
    >>> remove_duplicated_words('cat cat cat')
    'cat'
    >>> remove_duplicated_words('1 2 3')
    '1 2 3'
"""


def remove_duplicated_words(line: str) -> str:
    inter = line.split(' ')
    i = 0
    unique = []
    while i < len(inter):
        check = unique.count(inter[i])
        if check == 0:
            unique.append(inter[i])
        else:
            i += 1
    result = " ".join(unique)
    returned = f"'{result}'"
    print(returned)
