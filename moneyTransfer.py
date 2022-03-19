import sys
# For getting input from input.txt file
sys.stdin = open('input.txt', 'r')
 
# Printing the Output to output.txt file
sys.stdout = open('output.txt', 'w')


line = input().split(' ')
n =line[0]
n = int(n)
t = line[1]
t = int(t)
acc = dict()
order = list()
for i in range(n):
    line = input().split(' ')
    u = line[0]
    b = int(line[1])
    order.append(u)
    acc[u] = b

for i in range(t):
    line = input().split(' ')
    Ua = line[0]
    Ub = line[1]
    x = int(line[2])
    if( x> acc[Ua]):
        continue
    else:
        acc[Ua] -= x
        acc[Ub] += x
order.sort()
for o in order:
    print("{} {}".format(o, acc[o]))

