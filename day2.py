
age=21
height=5.8
AGE=21
name="bhima"
is_student=True
print(type(age))
print(type(height))
if(age==AGE):
    print("age is correct")
else:
    print("age is incorrect")
    

num1=str(input("Enter a name: "))
num2=int(input("Enter another age: "))
currentyear=2026
expyear=2030
for i in range(currentyear, expyear + 1):
    age=num2+1
    currentyear=currentyear+1
print(age)


name = input("Enter your name: ")
age = input("Enter your current age: ")
age = int(age)
new_age = age + 4
print("Hey", name + ", you will be", new_age, "years old in 2030!")


totalamount = float(input("Enter the total bill amount: "))
totalmembers = int(input("Enter the number of people to split the bill: "))
amountperperson = totalamount / totalmembers
print("Each person should pay: ", format(amountperperson, '.2f'))
print("im learning")


item_name = "Laptop"
quantity = 2
price = 499.99
in_stock = True
print("Item:", item_name, ", Qty:", quantity, ", Price:", price, ", Available:", in_stock)
total_cost = quantity * price
print("Total Cost:", total_cost)
