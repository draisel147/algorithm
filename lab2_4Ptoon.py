import itertools

# Matrix บอกค่า
earnings_matrix = [
    [0, 40, 60, 15, 50],
    [40, 0, 55, 20, 100],
    [60, 55, 0, 30, 45],
    [15, 20, 30, 0, 80],
    [50, 100, 45, 80, 0]
]

points = ['a', 'b', 'c', 'd', 'e']

def calculate_earnings(route):
    total_earnings = 0
    for i in range(len(route) - 1):
        start_point = route[i]
        end_point = route[i + 1]
        total_earnings += earnings_matrix[points.index(start_point)][points.index(end_point)]
    return total_earnings

def print_route(route):
    print(" -> ".join(route))

# สร้างการเรียงสับเปปลี่ยนที่เป็นไปได้ในแต่ละจุด
all_routes = list(itertools.permutations(points))

max_earnings = 0
best_route = []

# เลิอกจุดเริ่มต้น
print("นายตูนต้องการวิ่งรับเงินบริจาคเพื่อสร้างโรงพยาบาล โดยจะวิ่งผ่านเริ่มต้นที่จุดใดจุดหนึ่งแล้ววิ่งกลับไปยังจุดเริ่มต้น")
print("วิ่งทั้งหมด 5 จังหวัดโดยจะเลือกเส้นทางที่ได้รับเงินบริจาคสูงสุด  โดยมีข้อมูลดังนี้")
print("    a    b    c    d    e  ")
print("a [00,  40,  60,  15,  50]")
print("b [40,  00,  55,  20,  100]")
print("c [60,  55,  00,  30,  45]")
print("d [15,  20,  30,  00,  80]")
print("e [50,  100, 45,  80,  00]")

print(f"โรงพยาบาล ที่ต้องการวิ่งผ่าน: {' | '.join(points)}")
starting_point = input("เลือกโรงพยาบาล: ").lower()

if starting_point not in points:
    print("กรุณากรอกโรงพยาบาลที่มีอยู่ในจุด.")
    exit()

# กรองเส้นทางเพื่อพิจารณาเริ่มต้นจากจุดที่เลือกเท่านั้น
all_routes = [route for route in all_routes if route[0] == starting_point]

for route in all_routes:
    
    current_route = list(route) + [route[0]]

   
    earnings = calculate_earnings(current_route)

    
    if earnings > max_earnings:
        max_earnings = earnings
        best_route = current_route

print(f"\nจุดเริ่มต้นคือ '{starting_point}'.")
print("เลือกจุดต่อไป :")

# Main game loop
visited_points = [starting_point]
while len(visited_points) < len(points):
    available_points = [p for p in points if p not in visited_points]

    if not available_points:
        print("\nนายตูนวิ่งรับเงินบริจาคเพื่อสร้างโรงพยาบาลทั้ง 5 จุดแล้ว.")
        print("ผลลัพธ์เส้นทางที่เดินมา:")
        print_route(visited_points)
        print(f"จำนวนเงินตอนนี้: {calculate_earnings(visited_points)} บาท")
        if calculate_earnings(visited_points) == 235:
            print("ผลลัพธ์ตอนนี้ : เป็นทางที่ได้เงินมากที่สุด")
        else:
            print("ผลลัพธ์ตอนนี้ : ไม่ใช่ทางที่ได้เงินมากที่สุด")
        break

    print("\nจุดที่เหลืออยู่:", " | ".join(available_points))

    next_point = input("เลือกจุดต่อไป: ").lower()

    if next_point not in available_points:
        print("\nกรุณากรอกโรงพยาบาลที่มีอยู่ในจุด.")
        continue

    visited_points.append(next_point)
    print(f"ได้รับเงิน {earnings_matrix[points.index(visited_points[-2])][points.index(next_point)]} บาท จากจุด {visited_points[-2]} ไปยัง {next_point}.")
    print(f"จำนวนเงินตอนนี้: {calculate_earnings(visited_points)} บาท")
    print("เส้นทางที่เดินมา:")
    print_route(visited_points)

print("\nนายตูนวิ่งรับเงินบริจาคเพื่อสร้างโรงพยาบาลทั้ง 5 จุดแล้ว.")
print("ผลลัพธ์เส้นทางที่เดินมา:")
print_route(visited_points)

if calculate_earnings != 235:
    print(f"จำนวนเงินตอนนี้: {calculate_earnings(visited_points)} บาท")
    print("ผลลัพธ์ตอนนี้ : ไม่ใช่ทางที่ได้เงินมากที่สุด")
if calculate_earnings == 235:
    print(f"จำนวนเงินตอนนี้: {calculate_earnings} บาท")
    print("ผลลัพธ์ตอนนี้ : เป็นทางที่ได้เงินมากที่สุด")