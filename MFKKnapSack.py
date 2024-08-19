def mfknapsack(i,j) :
    print("----------------")
    print(i,j ," : " , f[i][j])
    
    if f[i][j] < 0 :
        if j < weights[i]:
            print('op1')
            value = mfknapsack(i-1,j)
        else:
            # กรณี ที่ 2
            print('op2')
            value = max(mfknapsack(i-1,j) , values[i] + mfknapsack(i-1,j-weights[i]))
        print('value = ',value, i,j)
        f[i][j] = value    
        print(f)
    else:
        print(i,j,'nothing')
    print('****',i,j,f[i][j])
    return f[i][j] 

#* ราคา 
values = [0,12,10,20,15] 
#* น้ำหนัก
weights = [0,2,1,3,2]
w = 5
f = []
x = [0]*5
f.append(x)

for i in range(1,len(values)):
    x = [0]
    for j in range(w):
        x.append(-1)
    f.append(x)
print(f)
mfknapsack(len(values)-1,len(values)-1)
print(f)