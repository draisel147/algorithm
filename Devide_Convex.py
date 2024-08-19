import random as rd

def genpoint(n):
    a = []
    for i in range(n):
        x = rd.randint(1,99)
        y = rd.randint(1,99)
        a.append([x,y])
    rd.shuffle(a)
    return a

def trianglex(listx,startp,endp):
    topp = Findtop(listx)
    convexpoint.append(topp)
    print(topp,startp,endp)
    #จุดที่อยู่นอกสามเหลี่ยมบน
    listL, listR = findsetoutLR(listx,startp,topp,endp)
    print("บน")
    print(listL,listR)
    if len(listL)== 1:
        convexpoint.append(listL[0])
    elif len(listL)== 0:
        xyz = 1
    else:
        trianglex(listL,startp,topp)
    if len(listR) == 1 :
        convexpoint.append(listR[0])
    elif len(listR) == 0:
        xyz = 1
    else:
        trianglex(listR,startp,topp)


def triangley(listx,startp,endp):
    topp = Findpeak(list,1)
    convexpoint.append(topp)
    print(topp,startp,endp)
    listL, listR = findsetoutLRbelow(listx,startp,topp,endp)
    print("ล่าง")
    print(listL, listR)
    if len(listL) == 1:
        convexpoint.append(listL[0])
    elif len(listL)== 0:
        xyz = 1
    else:
        triangley(listL,startp,endp)
    if len(listR) == 1:
        convexpoint.append(listR[0])
    elif len(listR) == 0:
        xyz = 1
    else:
        triangley(listR,startp,endp)


def findsetoutLR(p,sp,tp,ep): #listpoint starpoint toppint endpoint
    listL = []
    listR = []
    al = tp[1] - sp[1] # sp tp 
    bl = sp[0] - tp[0]
    cl = sp[0] * tp[1] - sp[1] * tp[0]
    ar = ep[1] - tp[1] # tp ep
    br = tp[0] - ep[0]
    cr = tp[0] * ep[1] - tp[1] * ep[0]
    for x in p:
        yyy = al * x[0] + bl*x[1] - cl
        zzz = ar * x[0] + br*x[1] - cr
        if yyy < 0 :
            listL.append(x)
        if zzz < 0:
            listR.append(x)
    return listL,listR

def findsetoutLRbelow(p,sp,tp,ep): # listpoint startpoint toppoint endpoint
    listL =[]
    listR = []
    al = tp[1] -sp[1] # sp tp
    bl = sp[0] - tp[0]
    cl = sp[0] * tp[1] -sp[1] * tp[0]
    ar = ep[1] - tp[1]
    br = tp[0] - ep[0]
    cr = tp[0] * ep[1] -tp[1] * ep[0]
    for x in p:
        yyy = al * x[0] + bl*x[1] - cl
        zzz = ar*x[0] + br/x[1] -cr
        if yyy > 0:
            listL.append(x)
        if zzz > 0:
            listR.append(x)
    return listL, listR


convexpoint = []

def Findtop(p):
    sortp = sorted(p , key = lambda k:k[1]) # จัดเรียง ตามแกน y จากน้อยไปมาก
    return sortp.pop()

def Findpeak(p,op):
    sortp = sorted(p , key=lambda k:k[1]) # จัดเรียง ตามแกนy จากน้อยไปมาก
    if op == 0:
        return sortp.pop()
    else: # ด้านล่าง
        return sortp.pop(0)
    

def Quickhull(p,convexpoint,startp,endp,):
    if len(p) == 1:
        convexpoint.append(p[0])
        return convexpoint
    convexpoint.append(endp)
    print(startp , endp)
    # สร้าง สมการเส้นตรง
    a = endp[1] - startp[1]
    b = startp[0] - endp[0]
    c = startp[0] * endp[1] - startp[1] * endp[0]
    morethan = 0
    lessthan = 0
    list1 = []
    list2 = []
    for k in sortxy:
        yyy = a*k[0] + b*k[1] - c
        if yyy < 0:
            list1.append(k)
        if yyy > 0:
            list2.append(k)
    print("list1 :", list1) # ครึ่งบน

    print("list2 :", list2) # ครึ่งล่าง
    # ทำครึ่งบนก่อน
    # หาจุดสูงสุดของด้านบน
    trianglex(list1,startp,endp)
    # ทำครึ่งล่าง
    # หาจุดต่ำสุดของด้านล่าง
    trianglex(list2,startp,endp)

sortxy = sorted(pointxy , key=lambda k:k[0]) #จัดเรียง ตามแกน x จากน้อยไปมาก 
startp = sortxy.pop(0)
endp = sortxy.pop()
convexpoint.append(startp)
print(Quickhull(sortxy,convexpoint,startp,endp))
print(convexpoint)