#target: node0->node9
graph=[
    [0,0,0,0,0,1,0,0,0,0],
    [0,0,0,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,1,0,1,0],
    [0,0,0,0,0,0,0,1,1,0],
    [0,0,0,0,0,0,0,0,1,1],
    [1,1,0,0,0,0,0,0,0,0],
    [0,1,1,0,0,0,0,0,0,0],
    [0,1,0,1,0,0,0,0,0,0],
    [0,0,1,1,1,0,0,0,0,0],
    [0,0,0,0,1,0,0,0,0,0],
    ]
def walk(start,cover,path):
    cover[start]=1
    path.append(start)
    if start==9:
        print(path)
    for i in range(10):
        if graph[start][i]==1 and cover[i]==0:
            walk(i,cover,path)
    cover[start]=0
    path.pop()
print('可能的状态转移路径有:')
walk(0,[0,0,0,0,0,0,0,0,0,0],[])