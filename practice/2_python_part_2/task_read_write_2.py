"""
Use function 'generate_words' to generate random words.
Write them to a new file encoded in UTF-8. Separator - '\n'.
Write second file encoded in CP1252, reverse words order. Separator - ','.

Example:
    Input: ['abc', 'def', 'xyz']

    Output:
        file1.txt (content: "abc\ndef\nxyz", encoding: UTF-8)
        file2.txt (content: "xyz,def,abc", encoding: CP1252)
"""
import textwrap


def generate_words(n=20):
    import string
    import random

    words = list()
    for _ in range(n):
        word = ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 10)))
        words.append(word)

    return words


wordlist = generate_words()
utf = '\\n'.join(wordlist)
charset_one = 'utf-8'
utffile = 'utffile.txt'
with open(utffile, 'w', encoding=charset_one) as r:
    r.write(utf)

with open(utffile, 'r') as u:
    print(f'{utffile}(content: "{textwrap.fill(utf, width=500)}", encoding: {charset_one})')

wordlist.reverse()
cp1252 = ','.join(wordlist)
charset_two = 'cp1252'
cp1252file = 'cp1252file.txt'
with open(cp1252file, 'w', encoding=charset_two) as f:
    f.write(cp1252)

with open(cp1252file, 'r') as g:
    print(f'{cp1252file}(content: "{g.read()}", encoding: {charset_two})')