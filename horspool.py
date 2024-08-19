# page 19 week7 

# shifttable
t = "asdfhgasjkdgzxcbvabarbersdfasdfqwerqq"
p = "barber"

def shifttable(p):
    m = len(p)
    dic = {}
    for j in range(0, m - 1):
        dic[p[j]] = m - 1 - j
    return dic

def horspool(p, t):
    dicx = shifttable(p)
    m = len(p)
    n = len(t)
    i = m - 1
    while i <= n - 1:
        k = 0
        while k <= m - 1 and p[m - 1 - k] == t[i - k]:
            k = k + 1
        if k == m:
            return i - m + 1
        else:
            if t[i] in dicx.keys():
                i = i + dicx[t[i]]
                print('shift', dicx[t[i]])
            else:
                i = i + m
                print('shift', m)
    return -1

print(horspool(p, t))