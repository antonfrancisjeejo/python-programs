from math import ceil
graph=[[] for i in range(100)]
path=[];temp=[]
c_A=0;c_B=0


def find(i,prev):
    global path
    temp.append(i)
    if i==n:
        path=temp
        return
    for j in graph[i]:
        if j!=prev:
            find(j,i)
    del temp[-1]


def mark(i,visited,c):
    global c_A,c_B
    if visited[i]==0:
        if c==1:
            c_A+=1
        else:
            c_B+=1
    visited[i]=c
    if c==1:
        c_A+=1
    else:
        c_B+=1
    for j in graph[i]:
        if visited[j]==0:
            mark(j,visited,c)


def findwinner():
    global c_A,c_B,path
    find(1,-1)
    visited=[0 for i in range(n+1)]
    for i in range(len(path)):
        if(i<ceil(len(path)/2.0)):
            visited[path[i]]=1
            c_A+=1
        else:
            visited[path[i]]=2
            c_B+=1
    for j in path:
        mark(j,visited,visited[j])
    if c_A>c_B:
        print('A wins')
    elif c_B<c_B:
        print('B wins')
    else:
        print('Draw')

n=7
graph[1].append(4)
graph[2].append(5)
graph[3].append(4)
graph[4].append(6)
graph[4].append(3)
graph[5].append(6)
graph[5].append(7)
graph[5].append(2)
graph[6].append(4)
graph[6].append(5)
findwinner()