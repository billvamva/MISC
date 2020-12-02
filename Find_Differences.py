# Program to find differences between two sample text files and outputting them in a text file
# Used as make shift branch system locally to find changes code

with open('sample_1.txt', 'r') as file1:
    with open('sample_2.txt', 'r') as file2:
        same = set(file1).difference(set(file2))

same.discard('\n')

with open('differences.txt', 'w') as file_out:
    file_out.truncate()
    for line in same:
        file_out.write(line)
