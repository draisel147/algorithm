import random as rd
def dice():
    return rd.randint(1,6)

def play():
    p = 0 
    num = 0

    while p < 9:    
        result = dice()
        num +=1
        p += result

        if p >9:
            p= 18 - p
        print(f"Roll {num}: {result} - Current Position : {p}")
    print("Total roll:",num)
play()

