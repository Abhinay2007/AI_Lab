
from collections import deque

# grid = [
#  [1,0,0,1,],
#  [1,1,1,0],
#  ['S',0,0,1],
#  [1,0,0,'G']
# ]

grid = [
    [0, 0, 0, 1, 0, 0],
    [1, 1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 0],
    ['S', 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 'G'],
    [0, 1, 0, 0, 0, 0]
]

def countX(grid):
    count=0
    for row in grid:
        for col in row:
            if col==1:
                count+=1
                
    return count




rows = len(grid)

cols = len(grid[0])

def findS(r,c,grid):
    
    for i in range(r):
        for j in range(c):
            if grid[i][j]=='S':
                return (i,j)
            
def findG(r,c,grid):
    
    for i in range(r):
        for j in range(c):
            if grid[i][j]=='G':
                return (i,j)
            

start = findS(rows,cols,grid)

goal = findG(rows,cols,grid)

queue = deque([(start,[start])])

visited = set()
visited.add(start)

directions=[(-1,0),(1,0),(0,-1),(0,1)]
print("Grid Navigation Begins\n")

final_path=None

while queue:
    
    
    print("MainQueue: ",queue)
    current,path = queue.popleft()

    
    print("Current Position:",current)
    print("Path: ", path)

    print("After Dequeue Queue: ",queue)
    print("Visited:",visited)



    if current==goal:
        final_path=path
        print("\nGoal Reached!")
        break

    for dr,dc in directions:

        nr=current[0]+dr
        nc=current[1]+dc
        
        print("nr and nc: ",[nr,nc])

        if 0<=nr<rows and 0<=nc<cols:

            if grid[nr][nc]==1:
                print("It contains X")
                continue
                

            if (nr,nc) in visited:
                print("It is Already Visited")
                continue

            visited.add((nr,nc))

            print("Visited: ",visited)

            queue.append(((nr,nc),path+[(nr,nc)]))
            print("MainQueue: ",queue)
        else:
            print("out of matrix")

    print("\n==============================")
            
            
print("\n==============================")
if final_path:
    print("Path Found:")
    print(final_path)
    print("Number of 1:",countX(grid))
else:
    print("No path exists.")
    
print("\nRational Behaviour Analysis")
print("1. The agent remembers visited cells.")
print("2. It never revisits explored locations.")
print("3. It avoids obstacles.")
print("4. It systematically searches for the goal.")
print("Hence, it behaves as a Model-Based Intelligent Agent.")

