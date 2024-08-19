from random import randint
ball = int(input("หยิบลูกบอลมากี่ลูก :"))
total = []
ballred = 0 # 1
ballblue = 0 # 2

for i in range(ball):
    n = randint(1,2)
    total.append(n)
    if n == 1 :
        ballred =+1
    else:
        ballblue =+1

print(total)
print("สีแดง :",str(total).count("1"))
print("สีฟ้า :",str(total).count("2"))

#print count ballred
#print count ball
    
