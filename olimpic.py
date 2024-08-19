def olim(n):
    listx = [0]*130
    listx[6] = 1
    listx[9] = 1
    listx[20] = 1
    for i in range(6,n+1): 
        if(listx[i] == 1):
            listx[i+6] = 1
            listx[i+9] = 1
            listx[i+20] = 1
    
    return listx
n = 50
xxx= olim(50)
for i in range(n+1):
    if xxx[i] == 1:
        print(i)

print(xxx)


    