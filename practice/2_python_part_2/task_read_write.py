"""
Read files from ./files and extract values from them.
Write one file with all values separated by commas.

Example:
    Input:

    file_1.txt (content: "23")
    file_2.txt (content: "78")
    file_3.txt (content: "3")

    Output:

    result.txt(content: "23, 78, 3")
"""
import os

location = "./files"
all_files = os.listdir(location)
filename = 'result.txt'


intermediary = []
for i in all_files:
    minimal = len(all_files) - 1
    with open(os.path.join(os.path.dirname(__file__), location, i)) as f:
        content = f.read()
        intermediary.append(content)

result = ', '.join(intermediary)


with open(filename, 'w') as r:
    r.write(result)

with open(filename, 'r') as f:
     print(f'{filename}(content: "{f.read()}")')