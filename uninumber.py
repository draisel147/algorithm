# week6rev3 page.13
def uninumber(a):
    for i in range(len(a)-1):
        if a[i] == a[i+1]:
            return False
    return True
    

a1 = [1,2,3,3,4,5,6]
print(uninumber(a1))
# วิธีเช็คจำนวน
print(len(a1))
        