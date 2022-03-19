import sys
# For getting input from input.txt file
sys.stdin = open('input.txt', 'r')
 
# Printing the Output to output.txt file
sys.stdout = open('output.txt', 'w')

line = input().split(' ')

m = int(line[0])
n = int(line[1])

matrix = list()

for i in range(m):
    line = input().split(' ')
    for i in range(len(line)):
        line[i] = int(line[i])
    matrix.append(line)


for lines in matrix:
    print(lines)