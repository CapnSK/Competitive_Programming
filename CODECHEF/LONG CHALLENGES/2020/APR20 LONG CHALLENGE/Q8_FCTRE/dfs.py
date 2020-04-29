v = [[] for i in range(100)] 
 
def addEdge(x, y): 
    v[x].append(y) 
    v[y].append(x) 

def printPath(stack): 
    for i in range(len(stack) - 1): 
        print(stack[i], end = " -> ") 
    print(stack[-1]) 

def DFS(vis, x, y, stack):
    #print("Current node is",x)
    stack.append(x)
    #print("Stack before",stack)
    if (x == y): 

        printPath(stack) 
        return [True,stack]
    vis[x] = True
    found=False
    flag = 0
    if (len(v[x]) > 0): 
        for j in v[x]: 
              

            if (vis[j] == False): 
                found,path=DFS(vis, j, y, stack) 
                if found:
                    stack=path
                    flag = 1
                    break
  
    if (flag == 0):
        del stack[-1] 
    #print("stack after",stack)
    return [found,stack]
  

def DFSCall(x, y, n, stack): 
      

    vis = [0 for i in range(n + 1)] 
  
    found,path=DFS(vis, x, y, stack)
    return path
 
n = int(input())
stack = [] 
for i in range(n-1):
    k,l=map(int,input().split())
    addEdge(k,l)
  
# Function Call
t=int(input())
while t>0:
    t-=1
    stack.clear()
    print(DFSCall(int(input()), int(input()), n, stack))