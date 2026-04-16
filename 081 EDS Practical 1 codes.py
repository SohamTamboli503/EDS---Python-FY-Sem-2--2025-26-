
#1
m = int(input("Enter Mass of object in kg :- "))
c = int(input("Enter Velocity of object in m/s :- "))

momentum = m*(c*c)
print("Momntum of object is :- ",momentum)


#2
n = (input("Enter number :- "))
if(len(n) == 1) :
        print(int(n)**2)
elif(len(n) == 2) :
        print(int(n) ** (1/2))
elif(len(n) == 3) :
        print(int(n) ** (1/3))


#3
from datetime import date

# Input
birth_year = int(input("Enter birth year (YYYY): "))
birth_month = int(input("Enter birth month (MM): "))
birth_day = int(input("Enter birth day (DD): "))

salary_rupees = float(input("Enter salary in rupees: "))

# Calculate age
today = date.today()
birth_date = date(birth_year, birth_month, birth_day)

age = today.year - birth_date.year
if (today.month, today.day) < (birth_date.month, birth_date.day):
    age -= 1

# Convert salary to dollars
USD_RATE = 93  # 1 USD = 93 INR (you can change this)
salary_dollars = salary_rupees / USD_RATE

# Output
print("Age:", age)
print("Salary in dollars: $", round(salary_dollars, 2))

#4
num = int(input("Enter a number: "))

reverse_num = 0
while num > 0:
    digit = num % 10
    reverse_num = reverse_num * 10 + digit
    num //= 10

print("Reversed number:", reverse_num)
print("Number successfully reversed")
    


