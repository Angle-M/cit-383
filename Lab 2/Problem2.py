import datetime
#I could only get the program to work for a single user 
#INput validation only for date and not ssn
class HealthPro:

    def __init__(self, SSN, fname, lname, m, d, y, h, w):
        self.SSN = SSN
        self.fname = fname
        self.lname = lname
        self.m = m
        self.d = d
        self.y = y
        self.h = h
        self.w = w
        
    def age(self):
        today = datetime.date.today()
        age = today.year - self.y
        if today.month < self.m or (today.month == self.m and today.day < self.d):
            age -= 1
        return age
    
    def maxHR(self):
        maxHR= 220 - self.age
        return maxHR
    
    def tarHR(self):
        hR = (.50 * (220 - self.age) - (.80 * (220 - self.age)))
        return hR
    
    def bmi(self):
        return (self.w * 703) / (self.h * self.h)
    
    def bmiCat(self):
        bmi = self.bmi()
        if bmi < 18.5:
            return "Underweight"
        elif bmi >= 18.5 and bmi <= 24.9:
            return "Normal"
        elif bmi >= 25 and bmi <= 29.9:
            return "Overweight"
        else:
            return "Obese"
healthProfile = {}
numPeople = int(input("Enter the number of people: "))

for m in range(numPeople):
    SSN = input("Enter SSN: ")
    fname = input("Enter first name: ")
    lname = input("Enter last name: ")
    m = int(input("Enter month of birth (1-12): "))
    d = int(input("Enter day of birth (1-31): "))
    y = int(input("Enter year of birth (YYYY): "))
    while y > datetime.datetime.now().year:
        print("Year of birth cannot be greater than current year.")
        y = int(input("Enter year of birth (YYYY): "))
    h = float(input("Enter height (in inches): "))
    w = float(input("Enter weight (in pounds): "))
    if SSN in healthProfile:
        print("SSN Already Exits: Enter a new one")
        SSN = input("Enter SSN: ")
        continue

client = HealthPro(SSN, fname, lname, m, d, y, h, w)

print("\nSSN\tName\tAge\tBMI\tBMI Category\tTarget Heart Rate")

print("First name:", client.fname)
print("Last name:", client.lname)
print("Age:", client.age())
print("BMI:", client.bmi())
#print("Target heart rate:", client.tarHR())
print("BMI category:", client.bmiCat())