def warshall (a):
    r = a.copy()
    n = len(a)
    for k in range(n):
        for i in range(n):
            for  j in range(n):
                r[i][j] =  r[i][j] or( r[k][j] and r[i][k])
    return r

def floyd (a):
    r = a.copy()
    n = len(a)
    for i in range(n):
        for j in range(n):
            if r[i][j] == 0:
                r[i][j] = 1000000000
        r[i][i] = 0
    print(r)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                r[i][j] = min (r[i][j],r[i][k] + r[k][j])
    return r


b = [[0,1,0,0],[0,0,0,1],[0,0,0,0] ,[1,0,1,0]]
print(b)
print(warshall(b))
c = [[0,0,3,0],[2,0,0,0],[0,7,0,1] ,[6,0,0,0]]
print(c)
print(floyd(c))