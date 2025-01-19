def menu():
    totalMoney = 0
    memoList = []

    while True:
        print("\nยินดีต้อนรับสู่โปรแกรมธนาคาร \n1. ฝากเงิน \n2. ถอนเงิน \n3. แสดงยอดเงินคงเหลือ \n4. แสดงประวัติธุรกรรม \n5. ออกจากโปรแกรม\n")
        choose = int(input("What do you want to do : "))
        
        if choose == 1:
            deptMoney = int(input("\nEnter your money to deposit : "))
            totalMoney = dept(totalMoney, deptMoney)
            memoList.append(f"ฝากเงิน {deptMoney} บาท")

        elif choose == 2:
            widthMoney = int(input("\nEnter your money to Widthdraw : "))
            totalMoney = width(totalMoney, widthMoney)
            memoList.append(f"ถอนเงิน {widthMoney} บาท")

        
        elif choose == 3:
            print(f"\nยอดเงินทั้งหมดที่มีคือ {totalMoney} บาท\n")

        elif choose == 4:
            for data in memoList:
                print(f"ท่านได้ทำรายการ --{data}--")

        elif choose == 5:
            print("\nYou are exitting this program.......\n")
            break

def width(totalMoney, widthMoney):
    result = totalMoney - widthMoney
    return result


def dept(totalMoney, deptMoney):
    result = totalMoney + deptMoney
    return result

menu()