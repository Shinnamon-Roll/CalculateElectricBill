class naphi:

    def __init__(ihere, name, sirname, age):
        ihere.name = name
        ihere.sirname = sirname
        ihere.age = age


    def output(self):
        print(f"MY name is {self.name} {self.sirname} and age {self.age}")

age = int(input("Enter your age : "))

dungKorMool = naphi("Naphi", "Throngbunrod", age)

dungKorMool.output()


        
