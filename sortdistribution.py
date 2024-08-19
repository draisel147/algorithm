# page 12 week 7
# เรียงค่าซ้ำ
def distcount(a,l,u):
    n = len(a)
    s = [0] * n
    d = [0] * (u - l + 1)
    for i in range(n):
        d[a[i]-l] = d[a[i]-l] + 1 
    for j in range(1,u - l +1):
        d[j] = d[j-1] +d[j]
    for i in range(n-1,-1,-1):
        j= a[i]-l
        s[d[j]-1] = a[i]
        d[j] = d[j] -1
    return s

# n = 8
# x = list(range(n-1,-1,-1))
# print(x)
# เรียงจากมากไปน้อย

a = [12,11,14,12,11,13,14,11,12,14] #ชุดตัวเลข
l = 11 #ตัวน้อยสุด
u = 14 #ตัวมากสุด
print(distcount(a,l,u))