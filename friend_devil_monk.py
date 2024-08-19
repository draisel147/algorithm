#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("กำหนดให้ d เป็นปีศาจ p เป็นนักบวช")
print("ฝั่งซ้าย = l ฝั่งขวา = ") #เพื่อนไม่ได้กำหนดตัวแปรฝั่งขวา ดังนั้นเพื่อให้โค้ดไปต่อจะใช้ตัว r
print("l = [p,p,p,d,d,d] r = []")
print("ทิศทางเรือ right")
l=['p','p','p','d','d','d']
r=[]
Direction = 'right'
ship = ''


def recieveinput (L,R,Direction,ship): #รับค่าสตริง2ตัว
    print('ship to',Direction)
    ship = input('รับค่าสมาชิก(ไม่เกิน2ตัว): ')
    while(len(ship)>2):
        print('Invalid')
        ship = input('รับค่าสมาชิก(ไม่เกิน2ตัว): ')
    direction_track(L,R,Direction,ship)

        
#เนื่องจากflowchartใช้สัญลักษณ์ผิด ละขั้นตอนเรือไปทางซ้ายขวา

if l == [] and r == ['p','p','p','d','d','d'] :
    print("you win")
else :
    print("you lose")

