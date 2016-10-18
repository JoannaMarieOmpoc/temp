class BMI:
    mass = raw_input("Enter weight in pounds: ")
    height = raw_input("Enter height in inches: ")

    def calculate(self):
        massLBS = float(self.mass)*0.453592
        heightM = float(self.height)*0.0254

        BMI = float(massLBS)/(float(heightM)*float(heightM))
        if BMI < 18.5:
            print "\nUnderweight"
        elif 18.5 <= BMI < 25:
            print "\nNormal"
        elif 25 <= BMI < 30:
            print "\nOverweight"
        elif BMI >= 30:
            print "\nObese"
        else:
            print "\nError"

bmi = BMI()
print(bmi.calculate())