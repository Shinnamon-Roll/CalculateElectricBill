class Traveler:

    def __init__(self, name, destination, days):
        self.name = name
        self.destination = destination
        self.days = days

    def showDetails(self):
        print(f"ชื่อ: {self.name}, ประเทศ: {self.destination}, จำนวนวัน: {self.days}")


def main():
    travelers = []

    while True:
        print("\n--- ระบบจัดการนักเดินทาง ---")
        print("1. เพิ่มข้อมูลนักเดินทาง")
        print("2. แสดงรายชื่อนักเดินทางทั้งหมด")
        print("3. ออกจากโปรแกรม")
        
        choice = int(input("กรุณาเลือกเมนู: "))

        if choice == 1:
            name = input("ชื่อ: ")
            destination = input("ประเทศที่ต้องการไปเยือน: ")
            days = int(input("จำนวนวันเดินทาง: "))
            
            traveler = Traveler(name, destination, days)
            travelers.append(traveler)
            print(f"เพิ่มข้อมูลนักเดินทาง {name} สำเร็จ!")

        elif choice == 2:
            if travelers:
                print("\n--- รายชื่อนักเดินทางทั้งหมด ---")
                for traveler in travelers:
                    traveler.showDetails()
            else:
                print("ยังไม่มีข้อมูลนักเดินทางในระบบ")

        elif choice == 3:
            print("ขอบคุณที่ใช้โปรแกรม")
            break

        else:
            print("กรุณาเลือกเมนูที่ถูกต้อง")

main()
