from re import L
import sys
# For getting input from input.txt file
sys.stdin = open('input.txt', 'r')
 
# Printing the Output to output.txt file
sys.stdout = open('output.txt', 'w')

line = int(input())
t = line 

for i in range(t):
    line = input()
    n = int(line)
    line = input().split(' ')
    for i in range(len(line)):
        line[i] = int(line[i])
    points = line
    
    ls = line
    while(ls[0]==ls[-1]):
        ls.pop(-1)
        ls.pop(0)
    if(len(ls)==0):
        print("yes")
    ls_rev = ls.copy()
    ls_rev.reverse()

    #list storing possible connections
    al = []


    #dictionary storing the lengths of the connections
    circle = {}
    for i in range(1,n+1):
        a = ls.index(i)
        b = ls_rev.index(i)
        circle[i] = [((2*n-1)-b-1)-a, a, (2*n-1)-b-1, 2]
        al.append(((2*n-1)-b-1)-a)

    # now I can remove adjacent numbers


    # get the largest possible value from the dictionary


    for i in al:
        s = max(al)
        for i in circle.keys():
            if((circle[s][0] > circle[i][1] and circle[s][1]<circle[i][2]) or (circle[s][0] < circle[i][1] and circle[s][1]>circle[i][2])):
                #decrement by 1
                x = circle[i]
                circle[i] = [x[0], x[1], x[2], x[3]-1]
            else:
                continue
        al.remove(s)

    losl = []
    for i in circle.values():
        losl.append(i[3])
        
    if 0 in losl:
        print("no")
    else:
        print("yes")
            
