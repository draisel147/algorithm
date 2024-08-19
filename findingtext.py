text = 'adfzcutqertysdfgpzolhkdhdufg'
pattern = 'sdfg'

# เป็นการใช้เมธอด ของ python ที่มีอยู่แล้ว
# x = text.find(pattern)
#? ชื่อ.find(value,start,end)
#? value = คำที่จะหา
#? strat = จุดที่จะเริ่มต้นในการหา (ไม่ต้องระบุก็ได้)
#? end = จุดสุกท้ายที่จะหา (ไม่ต้องระบุก็ได้)
# print(x) 

#ทำตามอาจารย์
def strmatch(text,pattern):
    n= len(text)
    m =len(pattern)
    indexx = -1
    # for i in range(n-m+1):
    i =0
    while i < n-m+1 :
        match = 0
        j = 0
        # for j in range(m):
        while j < m:
            print(pattern[j],text[i])
            if pattern[j] == text[i]:
                match = match + 1
                j = j+1
                i = i+1
                if match == m:
                    print(i-1)
                    return i-m
                
            
                # i =+ 1 ใช้ได้เหมือนกัน
            else:
                j= m
                i =i+1
                if match > 0:
                    i = i
    return 0
print(strmatch(text,pattern))
        