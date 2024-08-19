import random as rd
x = int(input("ใส่จำนวนลูกบอล : "))
l1 = []
c1 = ['Red','Green','Yellow','Black','Gold','Silver','Cyan','Pink','White','Gray']
contx = {}

for i in range (len(c1)):
    contx[c1[i]] = 0
    
for i in range(x):
    j = rd.randint(0,7)    
    contx[c1[j]] = contx[c1[j]] +1

for i in range(len(c1)):
    print(c1[i], ' = ', contx[c1[i]])