import sys
# For getting input from input.txt file
sys.stdin = open('input.txt', 'r')
 
# Printing the Output to output.txt file
sys.stdout = open('output.txt', 'w')

from collections import defaultdict

n = input()
line = input().split(' ')
ans = list()
for l in line:
    ans.append(int(l))

line = ans


def billboard(line):
    Dic =defaultdict(int)            
    Dic[0]=0                        
    for a in line:                   
        D2=Dic.copy()               
        for d,s in Dic.items():    
            s1 = s+a              
            for d2 in [d-a,d+a]:  
                D2[abs(d2)] = max(D2[abs(d2)],s1) 
        Dic=D2
    return Dic[0]//2               

print(billboard(line)) 