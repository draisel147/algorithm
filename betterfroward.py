a1 = [[2,-1,1],[4,1,-1],[1,1,1]]
b1 = [1,5,0]

def bfe(a,b):
    n = len(a)
    for i in range(n):
        a[i].append(b[i])
    for i in range(n-1):
        pivotrow = i
        for j in range(i+1,n):
            # print("***", j,i , a[j][i], a[pivotrow][i])
            if abs(a[j][i] > abs(a[pivotrow][i])):
                pivotrow = j
        for k in range(i,n+1):
            tempvalue = a[i][j]
            a[i][j] = a[pivotrow][j]
            a[pivotrow][j] = tempvalue
        for j in range(i+1,n):
            temp = a[j][i] / a[i][i]
            for k in range(i,n+1):
                a[j][k] =  a[j][k] - a[i][k] * temp
# ตัวรัน bfe
bfe(a1,b1)
print(a1)

x= [1] * len(a1)
def bws(a):
    print(len(a))
    n = len(a)

    print(x)
    for i in range(n-1,-1,-1):
        s = a[i][n]
        for j in range(i+1,n):
            s = s-a[i][j] * x[j]
        x[i] = s/a[i][i]
    return x
bws(a1)
print(x)




