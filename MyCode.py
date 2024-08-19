def check_0(char_list):
    count = 0
    for char in char_list:
        if char == '0':
            count += 1
    return count
def check_1(char_list):
    count = 0
    for char in char_list:
        if char == '1':
            count += 1
    return count
def check_invalid(u):
    
    valid_chars = set('01')
    if not all(char in valid_chars for char in u):
        return True

    # Check if the input contains at most two characters
    if len(u) > 2:
         print("Invalid input! Please enter '0' or '1' characters only, and at most two characters.")

print("1 คือ พระ , 0 คือ ปีศาจ")
left = ['1','1','1','0','0','0']
right = []
print("left: ", left)
print("right: ",right)
print("เรือ 1 ลำ นั่งได้มากที่สุด 2 คน")
print("----------- กรุณาเว้นช่องว่างตัวอักษร -------------")

x = input()
u = x.split()
i = 1  
if len(u) <= 2:
            while i != 0:
                if len(u) == 2:
                    #ซ้ายไปขวา
                    left.remove(u[0])
                    left.remove(u[1])
                    right.append(u[0])
                    right.append(u[1])
                    if len(right) == 6:
                        print("-----END.-----"+"\n"+"left: "+str(left)+ "\n" +"right: "+str(right)+"\n"+ "จำนวนรอบ: "+str(i)+"\n"+ "You Win!")
                        break
                    elif check_0(left) > check_1(left) or check_0(right) > check_1(right):
                        checked = check_0(left) > check_1(left) or check_0(right) > check_1(right)
                        if ((checked) and check_1(right) != 0) and ((checked) and check_1(left) != 0):
                            print("left: "+str(left)+ "\n" +"right: "+str(right)+"\n"+"จำนวนรอบ: "+str(i)+"\n"+"Game Over.")
                            break
                    print("Left to Rignt >>>"+"\n"+"left: "+str(left)+ "\n" +"right: "+str(right)+"\n"+ "จำนวนรอบ: "+str(i))
                    x = input()
                    u = x.split()
                    i = i+1
                    if len(u) == 1:
                    #ขวาไปซ้าย
                        right.remove(u[0])
                        left.append(u[0])
                        if check_0(left) > check_1(left) or check_0(right) > check_1(right):
                            checked = check_0(left) > check_1(left) or check_0(right) > check_1(right)
                            if ((checked) and check_1(right) != 0) and ((checked) and check_1(left) != 0):
                                print("left: "+str(left)+ "\n" +"right: "+str(right)+"\n"+"จำนวนรอบ: "+str(i)+"\n"+"Game Over.")
                                break
                        print("Right to left <<<"+"\n"+"left: "+str(left)+ "\n" +"right: "+str(right)+"\n"+ "จำนวนรอบ: "+str(i))
                        x = input()
                        u = x.split()
                        i = i+1
                    elif len(u) == 2:
                    #ขวาไปซ้าย
                        right.remove(u[0])
                        right.remove(u[1])
                        left.append(u[0])
                        left.append(u[1])
                        if check_0(left) > check_1(left) or check_0(right) > check_1(right):
                            checked = check_0(left) > check_1(left) or check_0(right) > check_1(right)
                            if ((checked) and check_1(right) != 0) and ((checked) and check_1(left) != 0):
                                print("left: "+str(left)+ "\n" +"right: "+str(right)+"\n"+"จำนวนรอบ: "+str(i)+"\n"+"Game Over.")
                                break
                        print("Right to left <<<"+"\n"+"left: "+str(left)+ "\n" +"right: "+str(right)+"\n"+ "จำนวนรอบ: "+str(i))
                        x = input()
                        u = x.split()
                        i = i+1
                elif len(u) == 1:
                    #ซ้ายไปขวา
                    left.remove(u[0])
                    right.append(u[0])
                    if check_0(left) > check_1(left) or check_0(right) > check_1(right):
                            checked = check_0(left) > check_1(left) or check_0(right) > check_1(right)
                            if ((checked) and check_1(right) != 0) and ((checked) and check_1(left) != 0):
                                print("left: "+str(left)+ "\n" +"right: "+str(right)+"\n"+"จำนวนรอบ: "+str(i)+"\n"+"Game Over.")
                                break
                    print("Left to Rignt >>>"+"\n"+"left: "+str(left)+ "\n" +"right: "+str(right)+"\n"+ "จำนวนรอบ: "+str(i))
                    x = input()
                    u = x.split()
                    i = i+1
                    if len(u) == 1:
                        #ขวาไปซ้าย
                        right.remove(u[0])
                        left.append(u[0])
                        print("Right to left <<<"+"\n"+"left: "+str(left)+ "\n" +"right: "+str(right)+"\n"+ "จำนวนรอบ: "+str(i))
                        x = input()
                        u = x.split()
                        i = i+1
                        if check_0(left) > check_1(left) or check_0(right) > check_1(right):
                            checked = check_0(left) > check_1(left) or check_0(right) > check_1(right)
                            if ((checked) and check_1(right) != 0) and ((checked) and check_1(left) != 0):
                                print("left: "+str(left)+ "\n" +"right: "+str(right)+"\n"+"จำนวนรอบ: "+str(i)+"\n"+"Game Over.")
                                break
                    elif len(u) == 2:
                        #ขวาไปซ้าย
                        right.remove(u[0])
                        right.remove(u[1])
                        left.append(u[0])
                        left.append(u[1])
                        if check_0(left) > check_1(left) or check_0(right) > check_1(right):
                            checked = check_0(left) > check_1(left) or check_0(right) > check_1(right)
                            if ((checked) and check_1(right) != 0) and ((checked) and check_1(left) != 0):
                                print("left: "+str(left)+ "\n" +"right: "+str(right)+"\n"+"จำนวนรอบ: "+str(i)+"\n"+"Game Over.")
                                break
                        print("Right to left <<<"+"\n"+"left: "+str(left)+ "\n" +"right: "+str(right)+"\n"+ "จำนวนรอบ: "+str(i))
                        x = input()
                        u = x.split()
                        i = i+1
elif check_invalid(u):
    print("Invalid input! Please enter '0' or '1' characters only, and at most two characters.")