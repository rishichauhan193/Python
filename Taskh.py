# [1] WAP to print "helloworld".
# print("helloworld")

# [2] WAP to findout sum of two variables.
# a=int(input("Enter First Digit:- "))
# b=int(input("Enter Second Digit:- "))
# c=a+b
# print(c)

# [3] WAP to find square of given number
# n=int(input("Enter Digit:- "))
# square=n*n
# print(square)

# [4] WAP to find cube of given number
# n=int(input("Enter Digit:- "))
# cube=n*n*n
# print(cube)

# [5] WAP to create marksheet of student, input sub1,sub2,sub3 marks and display total, percentage and of student.
# name=str(input("Enter Name:- "))
# sub1=int(input("Enter sub1 Marks:- "))
# sub2=int(input("Enter sub2 Marks:- "))
# sub3=int(input("Enter sub3 Marks:- "))
# Total=sub1+sub2+sub3
# Percentage=Total/3
# print(f"Student name is {name}.")
# print(f"Total is {Total}.")
# print(f"Percentage is {Percentage}.")

# [6] WAP to findout biggest from given 3 values using if..else only.
# a=int(input("Enter First Digit:- "))
# b=int(input("Enter Second Digit:- "))
# c=int(input("Enter Third Digit:- "))
# if(b<a>c):print(a)
# elif(a<b>c):print(b)
# else:print(c)

# [7] Write a Python program that calculates the area of a circle based on the radius entered by the user.
# PI=3.14
# radius=int(input("Enter Radius:- "))
# area=PI*radius*radius
# print(f"{area} It is a area of circle.")

# [8] WAP to convert farenhit to celcius (celsius = (fahrenheit -32)*5/9)
# fahrenheit=int(input("Enter fahrenheit:- "))
# celsius = (fahrenheit-32)*5/9
# print(celsius)


# [9] WAP to findout area of circle.
# PI=3.14
# radius=int(input("Enter Radius:- "))
# area=PI*radius*radius
# print(f"{area} It is a area of circle.")

# [10] WAP to findout radious of circle(2*PI*R*R)
# PI=3.14
# R=int(input("Enter Radius:- "))
# circle=2*PI*R*R
# print(f"{circle} It is a radious of circle.")

# [11] WAP to findout area of square.(L*H)
# L=int(input("Enter Length:- "))
# H=int(input("Enter Height:- "))
# area=L*H
# print(f"{area} It is a area of square.")

# [12] WAP to swap two variables values without using third variabl
# a=int(input("Enter a:- "))
# b=int(input("Enter b:- "))
# print(f"Before Swaping a={a} and b={b}")
# a,b=b,a
# print(f"After Swaping a={a} and b={b}")

class Products():
    all_products = []
    country = "India"
    category = None

    def __init__(self, name:str, cost_price:float, mrp:float, quantity:int):
        assert isinstance(name, str), "Name should be a string..."
        self.name = name
        assert isinstance(cost_price, float), "Qunatity should be float."
        assert cost_price > 0, "Cost_price should be greater than 0!"
        self.cost_price = cost_price
        assert isinstance(mrp, float), "Qunatity should be float."
        assert mrp > 0, "MRP should be greater than 0!"
        self.mrp = mrp
        assert isinstance(quantity, int), "Qunatity should be integer."
        assert quantity > 0, "Quantity should be greater than 0!"
        self.quantity = quantity
        Products.all_products.append(self)

    def show_details(self):
        print(f"------------- Details of {self.name} -------------")
        print("Category:", self.category)
        print("Cost price:", self.cost_price)
        print("MRP:", self.mrp)
        print("Stock:", self.quantity)

    @staticmethod
    def addNewItem():
        print("Enter the following details:")
        name = input("Name: ")
        cost_price = float(input("Cost Price: "))
        mrp = float(input("MRP: "))
        quantity = int(input("Quantity: "))
        return name, cost_price, mrp, quantity

if __name__ == '__main__' :
    p1 = Products("1234", 35.5, 50, 10)
    p1.show_details()
    # s1 = 123
    # print(isinstance(s1, str))