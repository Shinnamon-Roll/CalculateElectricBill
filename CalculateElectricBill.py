def main():
    try:
        totalElec = float(input("\n💡 Enter total electricity bill: "))
        consumption = float(input("🔋 Enter your total consumption (units): "))
        allElec = totalElec / consumption

        SOldMonth, SLastMonth = map(int, input("\n📊 Enter Shimon's old and new electricity meter readings (e.g., 1274 1537): ").split())
        if SOldMonth >= SLastMonth:
            print("❌ Error: Old meter reading should be less than the new reading.")
            return main()
        sElecPay = calculateHousePayment(SOldMonth, SLastMonth, allElec)

        HOldMonth, HLastMonth = map(int, input("\n📊 Enter Hom's old and new electricity meter readings (e.g., 1280 1495): ").split())
        if HOldMonth >= HLastMonth:
            print("❌ Error: Old meter reading should be less than the new reading.")
            return main()
        hElecPay = calculateHousePayment(HOldMonth, HLastMonth, allElec)

        totalShi, totalHom, difference = calculateAll(sElecPay, hElecPay, totalElec)

        equalShare = difference / 2
        totalShi += equalShare
        totalHom += equalShare

        shiHouseShare = totalShi / 3
        homHouseShare = totalHom / 4

        displayResults(shiHouseShare, homHouseShare, difference, totalElec)

    except ValueError:
        print("❌ Invalid input. Please enter numeric values only.")
        main()

def calculateHousePayment(old, last, elec):
    electric = last - old
    elecPay = electric * elec
    return elecPay

def calculateAll(shi, hom, totalElec):
    difference = totalElec - (shi + hom)
    return shi, hom, difference

def displayResults(shiHouseShare, homHouseShare, difference, totalElec):
    print("\n================ Electricity Bill Summary ================")
    print(f"🏠 Shimon's House Payment per Person: {shiHouseShare:.2f} THB")
    print(f"🏠 Hom's House Payment per Person:    {homHouseShare:.2f} THB")
    print(f"💰 Total Electricity Bill:            {totalElec:.2f} THB")
    print(f"⚡ Difference Adjusted:               {difference:.2f} THB")
    print("========================================================")

main()
