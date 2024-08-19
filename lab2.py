import random

def get_days_in_month(month_name):
    if month_name in ["january", "march", "may", "july", "august", "october", "december"]:
        return 31
    elif month_name == "february":
        return 28
    else:
        return 30

def categorize_numbers(numbers):
    low_count = sum(1 for num in numbers if num <= 30)
    mid_count = 0
    high_count = 0
    damage_count = 0
    consecutive_high_count = 0
    
    for num in numbers:
        if 61 <= num <= 100:
            if high_count == 0:
                damage_count += 1
            high_count += 1
            consecutive_high_count += 1
            
            if consecutive_high_count > 2:  # แก้ไขตรงนี้ให้นับความเสียหายเมื่อตัวเลข 61-100 ติดกันมากกว่า 2 ตัว
                damage_count += 1
        else:
            consecutive_high_count = 0
            if 31 <= num <= 60:
                mid_count += 1
    
    return low_count, mid_count, high_count, damage_count

def main():
    month_name = input("ป้อนชื่อเดือน: ")

    if month_name.lower() in ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]:
        days = get_days_in_month(month_name)
        random_numbers = [random.randint(0, 100) for _ in range(days)]
        print(f"จำนวนวันในเดือน {month_name} คือ {days} วัน")
        
        low_count, mid_count, high_count, damage_count = categorize_numbers(random_numbers)
        print(f"จำนวนตัวเลขน้อย (0-30): {low_count}")
        print(f"จำนวนตัวเลขปานกลาง (31-60): {mid_count}")
        print(f"จำนวนตัวเลขมาก (61-100): {high_count}")
        print(f"ความเสียหาย: {damage_count} ครั้ง")
        
        print("ตัวเลขที่สุ่มมาในลิสต์:")
        print(random_numbers)
    else:
        print("เดือนไม่ถูกต้อง")

if __name__ == "__main__":
    main()
