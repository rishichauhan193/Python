# a=float(input("a: "))
# b=float(input("b: "))

# Operation= input("Which Operation You Want To Perform(+,-,*,/): ")

# if(Operation == '+'):print(f"Add is: {a+b}")
# elif(Operation == '-'):print(f"Sub is: {a-b}")
# elif(Operation == '*'):print(f"Mul is: {a*b}")
# elif(Operation == '/'):print(f"Div is: {a/b}")
# else:print("Sorry Your Choice is Wrong.")

# Printing the score of golf game:

PAR = 10
R=int(input("Enter Your Strokes:- "))

if R==10:print("PAR")
elif R==PAR-1:print("BIRDIE")
elif R==PAR-2:print("EAGLE")
elif R==PAR-3:print("DOUBLE EAGLE")
elif (R==PAR-4)|(R==PAR-5)|(R==PAR-6)|(R==PAR-7)|(R==PAR-8):print("TRIPLE EAGLE")
elif R==PAR-9:print("HOLE IN ONE")
elif R==PAR+1:print("BOGEY")
elif (R==PAR+2)|(R==PAR+3):print("DOUBLE BOGEY")
else:print("GO HOME--->")

'''
(1).
a=float(input("Enter Percentage:- "))

if(a>=75)           : print("A")
elif(65<=a<=74)   : print("B")
elif(55<=a<=64)   : print("C")
elif(45<=a<=54)   : print("D")
elif(35<=a<=44)   : print("E")
else:print("F")

(2).
x = int(input("Enter Your Year:- "))
if(x%400==0) and (x%100==0):print(f"{x} is a Leap Year.")
elif(x%4==0) and (x%100!=0):print(f"{x} is a Leap Year.")
else:print(f"{x} is a not Leap Year.")

(3).
a=int(input("a: "))
b=int(input("b: "))
c=int(input("c: "))

if(b<a>c):print(f"{a} is the largest number.")
elif(a<b>c):print(f"{b} is the largest number.")
else:print(f"{c} is the largest number.")

(4).

a=int(input("x-coordinate: "))
b=int(input("y-coordinate: "))

if(a>0<b):print(f"The coordinate point {a,b} lies in the First quadrant.")
elif(a<0<b):print(f"The coordinate point {a,b} lies in the Second quadrant.")
elif(a<0>b):print(f"The coordinate point {a,b} lies in the Third quadrant.")
elif(a>0>b):print(f"The coordinate point {a,b} lies in the Fourth quadrant.")

(5).
a=int(input("Maths: "))
b=int(input("Physics: "))
c=int(input("Chemestry: "))

if(a>=65)|(b>=55)|(c>=50)|(a+b+c>=190)|(a+b>=140):print(f"Total marks of Maths, Physics and Chemistry : {a+b+c}",end='\n' f"Total marks of Maths and Physics : {a+b}  The candidate is eligible.")
elif(a<65)|(b<55)|(c<50)|(a+b+c<190)|(a+b<140):print(f"Total marks of Maths, Physics and Chemistry : {a+b+c}",end='\n' f"Total marks of Maths and Physics : {a+b}  The candidate is not eligible.")

(6).
X=int(input('Enter Length of Rectangle: '))
W=int(input('Enter Width of Rectangle: ',))

if(X==W):print('This is Square.')
else:print("This is not square.")

(7).

a=int(input("Enter your Quantity Amount: "))
Total=(a*10/100)
if(a>=1000):print(f"Your Total is={a-Total}")
else:print(f"Total Amount= {a}")

(8).
print("                         ------------------------Retail Invoice---------------------")
R=str(input("Customer Name: "))
H=int(input("Contact Number: "))
print("Date of Invoice: 26/01/2023")
X=str(input("Enter Items:- "))
Y=int(input("Enter Price:- "))
Z=int(input("Enter Quantity:- "))
A=str(input("Enter Items:- "))
B=int(input("Enter Price:- "))
C=int(input("Enter Quantity:- "))
D=str(input("Enter Items:- "))
E=int(input("Enter Price:- "))
F=int(input("Enter Quantity:- "))
Total=print(f"Your Total:{Y*Z+B*C+E*F}")
if((Y*Z+B*C+E*F)<1000):
    print('-----------------------------------------------------------')
    print('Items                              Price                     Quantity                          Total')
    print(f"{X}                               {Y}                          {Z}                           {Y*Z} ")
    print(f"{A}                               {B}                          {C}                           {B*C} ")
    print(f"{D}                               {E}                          {F}                           {E*F} ")
    print('                                                                                             ---------')
    print(f"                                                                             Final Amount: {Y*Z+B*C+E*F}")
    print('                             ----------------Thanks for shopping with us!---------------')

else:print('-----------------------------------------------------------')
print('Items                              Price                     Quantity                          Total')
print(f"{X}                               {Y}                          {Z}                           {Y*Z} ")
print(f"{A}                               {B}                          {C}                           {B*C} ")
print(f"{D}                               {E}                          {F}                           {E*F} ")
print('                                                                                             ---------')
print(f"                                                                             Final Amount: {Y*Z+B*C+E}")
print(f"                                                                                 Discount:{(Y*Z+B*C+E)*10/100}                  ")
print(f"                                                                             Grand Final Amount: {(Y*Z+B*C+E)-((Y*Z+B*C+E)*10/100)}")
print('                             ----------------Thanks for shopping with us!---------------')

(9).
R=int(input("Enter Employees Salary:- "))
H=int(input("Enter Years:- "))
Total=(R*5/100)

if(H>5):print(f"Your Total Salary is = {R+Total}")
else:print(f"Your Total Salary is = {R}")


Digit Count:----

a = int(input("Enter a number:  "))
count = 0
while a > 0:
    a = a // 10
    count += 1
print(count)

1. Make a list containing of only strings. Now ask user for any string and re-arrange the list in the decending order of occurance of that string.
for example:
list1 = ['no bun', 'bug bun bug bun bug bug', 'bunny bug', 'buggy bug bug buggy']
input string = 'bug'
output list = ['bug bun bug bun bug bug', 'buggy bug bug buggy', 'bunny bug', 'no bun']

list1 = ['no bun', 'bug bun bug bun bug bug', 'bunny bug', 'buggy bug bug buggy']
test = input("Enter string: ")
list2 = []
for string in list1:
    count = string.count(test)
    list2.append((count, string))
list2.sort(reverse=True)
print(list2)
sorted_list = []
for item in list2:
    sorted_list.append(item[1])
print(sorted_list)

2. Create a Python program to generate user-defined set. Then ask user to eneter any value & check if the given value is present in a set or not.
n = int(input("No of elements: "))
s1 = set()
for i in range(n):
    inp = input(f"Element-{i}: ")
    s1.add(inp)
'''

'''
4. Use dictionary to store antonyms of words. E.g.- 'Right':'Left', 'Up':'Down', etc. Display all words and then ask user to enter a word and display antonym of it.
antonyms = {
    'Right' : 'Left',
    'up' : 'down',
    'positive' : 'negative',
    'big' : 'small'
}
for word in antonyms:
    print(word)
word = input("Enter word: ")
print("Antonym:", antonyms[word])
'''

'''
6. Sort the above dictionary by the names of students.

students = {
    "Aakash" : 80,
    "Jeet" : 78,
    "Raksha" : 94,
    "Jigna" : 92,
    "Sweety" : 90,
    "Mahesh" : 95
}
sorted_list = dict(sorted(students.items()))
print(sorted_list)

temp1 = students.items()
print(temp1)
temp2 = []
for item in temp1:
    temp2.append(item[ : :-1])
temp2.sort()
print(temp2)
temp3 = []
for item in temp2:
    temp3.append(item[ : : -1])
final_dictionary = dict(temp3)
print(final_dictionary)
'''
