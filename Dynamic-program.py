
#! Fibonaci
def fibonaci (n):
    a = [0,1]
    for i in range(2,n+1):
        a.append(a[i-1] + a[i-2])
    return a
print(fibonaci(10))

#! coinrow
def coinrow (c):
    f = [0,c[0]]
    n= len(c)
    for i in range(1,len(c)):
        f.append(max(c[i] + f[i-1],f[i]))
    return f[n]
c = [5,1,2,10,6,2]
# print(coinrow(c))

#! changcoin
def changcoin(d,n):
    f= [0]
    for i in range(1,n+1):
        temp = 9223372036854775807
        j = 0
        m = len(d)
        while j < m and i >= d[j]:
            temp = min(f[i-d[j]],temp)
            j = j+1
        f.append(temp+1)
    return f[n]
d= [1,2,5,10]
n= 9
# print(changcoin(d,n))

#TODO:  Hw


