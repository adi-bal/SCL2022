import sys
# For getting input from input.txt file
sys.stdin = open('input.txt', 'r')
 
# Printing the Output to output.txt file
sys.stdout = open('output.txt', 'w')

def findDist(point1, point2):
    return abs(point1[0]-point2[0]) + abs(point1[1]-point2[1])

def findDistance(m, n, mat):
    # Initialise dist
    i = 0
    dist = []
    while(i < m):
        dist.append([-1]*n)
        i += 1
    
    # Find for all black hole spots
    blackHole = {}
    blkhl = []
    i = 0
    while(i < m):
        j = 0
        while(j < n):
            if(mat[i][j] != 0):
                if(mat[i][j] in blackHole):
                    blackHole[mat[i][j]].append((i, j))
                    blkhl.append((i, j))
                else:
                    blackHole[mat[i][j]] = [(i, j)]
                    blkhl.append((i, j))
            j += 1
        i += 1
    #print(blackHole)

    # Calculate distance from end for all blackholes and set distance for each point (blackhole) to be that
    for bh in blackHole:
        lst = []
        for el in blackHole[bh]:
            lst.append(findDist(el, (m-1, n-1)))
        mindist = min(lst)
        for el in blackHole[bh]:
            dist[el[0]][el[1]] = mindist

    # Calculate distance between start and all black hole points and take the minimum - Q step
    finalmindist = 10**8
    lst = [findDist((0,0), (m-1,n-1))]
    for el in blkhl:
        lst.append(findDist((0, 0), el) + dist[el[0]][el[1]])
    # print(lst)
    finalmindist = min(lst)

    return finalmindist


    


line = input().split(' ')

m = int(line[0])
n = int(line[1])

matrix = list()

for i in range(m):
    line = input().split(' ')
    for i in range(len(line)):
        line[i] = int(line[i])
    matrix.append(line)

print(findDistance(m, n, matrix))