LeftSide = ['W', 'G', 'V']
RightSide = []
Direction = 'right'

def receiveShip(LeftSide, RightSide, Direction):
    print('ship to', Direction)
    ship = input('รับค่าขึ้นเรือ(1อย่างเท่านั้น): ').upper()
    while len(ship) != 1 or ship not in LeftSide:
        print('invalid')
        ship = input('รับค่าขึ้นเรือ(1อย่างเท่านั้น): ').upper()

    moveShip(LeftSide, RightSide, Direction, ship)

def moveShip(LeftSide, RightSide, Direction, ship):
    if Direction == 'right':
        LeftSide.remove(ship)
        RightSide.append(ship)
        Direction = 'left'
    else:
        RightSide.remove(ship)
        LeftSide.append(ship)
        Direction = 'right'

    checkWinOrLose(LeftSide, RightSide, Direction)

def checkWinOrLose(LeftSide, RightSide, Direction):
    print(LeftSide)
    print(RightSide)
    
    if (LeftSide == ['W', 'G'] or LeftSide == ['G', 'W']) and 'V' in LeftSide:
        print("Game over")
    elif (RightSide == ['W', 'G'] or RightSide == ['G', 'W']) and 'V' in RightSide:
        print("Game over")
    elif len(RightSide) == 3 and sorted(RightSide) == ['G', 'V', 'W']:
        print("You win")
    else:
        receiveShip(LeftSide, RightSide, Direction)

print('Wolf(W), Goat(G), Vegetable(V)')
print(LeftSide)
print(RightSide)
receiveShip(LeftSide, RightSide, Direction)