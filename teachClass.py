Mylite=[]

class Traveler:

    def __init__(self,num1,num2,num3,num4):

        self.num1=num1
        self.num2=num2
        self.num3=num3
        self.num4=num4

    def data(self):
        Mylite.append(f" {self.num1}   {self.num2}   {self.num3}   {self.num4}") 

        for Hoho in Mylite:
            print(Hoho)


while True:

    name=input("ชื่อ")
    destination=input("ประเทศที่ต้องการไปเยือน")
    days=int(input("จำนวนวันเดินทาง :"))
    tei=int(input("เบอร์โทร :"))
    a=int(input("\nป้อน 0 (อยากลาออกแล้วเพื่อออก) :"))

    if a!=0 :
        pmon=Traveler(name,destination,days,tei)
        pmon.data()

    elif a==0:
        break