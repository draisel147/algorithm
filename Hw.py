def max_profit(n,prices):
    #* สร้างรายการเก็บกำไรศุงสุดสำหรับแต่ละเมตรของเชือก
    profits = [0] * (n+1)
    
    #* สร้างรายการเก็บจำนวนครั้งที่ตัดเชือกและความยาวของแต่ละการตัด
    cut_counts = [0] *(n+1)
    cut_lengths = [0] * (n+1)

    for i in range (1,n+1):
        max_profit_i = float('-inf')
        best_cut = 0

        # ตัดเชือกยาว i  เมตร
        for j in range (1,i+1):
            if prices[j] + profits[i-j] > max_profit_i:
                max_profit_i = prices[j] + profits[i-j]
                best_cut = j

        profits[i] = max_profit_i
        cut_counts[i] = cut_counts[i - best_cut] + 1
        cut_lengths[i] = best_cut

    return profits[n],cut_counts,cut_lengths

    
#* ราคาตัดเชือก ยาว i เมตร จากตัวอย่าง
prices = [0,2,5,7,9,11]

n = int(input("ป้อนความยาวของเชือก (n เมตร): "))
profit,cut_counts,cut_lengths = max_profit(n,prices)
print("กำไรสูงสุดที่สามารถได้คือ",profit,"บาท")
print("แบ่งเชือกไปทั้งหมด",cut_counts[n],"ครั้ง")

#* แสดงรายละเอียดการตัดเชือก
current_length = n
for i in range(cut_counts[n]):
    cut_length = cut_lengths[current_length]  
    print("ครั้งที่", i + 1, ": ตัดเชือกเป็นเส้นยาว ", cut_length, " เมตร")
    current_length -= cut_length
