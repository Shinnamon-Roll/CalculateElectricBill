def main():

    Mylist=[]
    bigbank = 0

    while True :
        print("ยินดีต้อนรับสู่โปรแกรมธนาคาร\n 1.ฝากเงิน\n 2.ถอนเงิน\n 3.แสดงยอดเงินคงเหลือ\n 4.แสดงประวัติธุรกรรม\n 5.ออกจากโปรแกรม\n")
        num1 = int(input("กรุณาเลือกเมนู:"))

        if num1==1 :
            savemoney=int(input("กรุณากรอกจำนวนเงินที่ต้องการฝาก :"))
            bigbank = (pm(bigbank, savemoney))
            print(f"ฝากเงินสำเร็จ! ยอดเงินคงเหลือ {bigbank} บาท")

            Mylist.append(f"ฝากเงินสำเร็จ! ยอด {savemoney} บาท")

        elif num1==2 :
            savemoney=int(input("กรุณากรอกจำนวนเงินที่ต้องการถอน :"))
            bigbank = (sm(bigbank, savemoney))
            print(f"ถอนเงินสำเร็จ! ยอดเงินคงเหลือ {bigbank} บาท")
            
            Mylist.append(f"ถอนเงินสำเร็จ! ยอด {savemoney} บาท")

        elif num1==3 :
           print(f"ยอดเงินคงเหลือ {bigbank} บาท ")

        elif num1==4 :
            for data in Mylist:
                print(f">>>{data}")

        elif num1 == 5:
            print("ขอบคุณที่ใช้บริการ")
            break

def pm(bigBank, savemoney):
    bigBank = bigBank + savemoney

    return bigBank

def sm(bigbank, savemoney):
    m = bigbank - savemoney
    return m

main()