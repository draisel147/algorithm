# page8 week7 rev01
# เรียงจากน้อยไปมาก
def compcount(a):
    n = len(a) #for i << 0 to n -1 do count[i] << 0 (เป็นการเขียนย่อ)
    countx = [0] * n
    for i in range(n-1):
        for j in range(i+1,n):
            if a[i] < a[j]:
                countx[j] = countx[j] + 1 
            else:
                countx[i] = countx[i] + 1
    s = [0] * n
    for i in range(n) :
        s[countx[i]] = a[i]

    return s

a = [17,5,19,14,28,2] #ชุดตัวเลขที่ต้องการให้เรียง
print(compcount(a))