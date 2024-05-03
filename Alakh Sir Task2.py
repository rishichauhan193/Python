'''x=str(input("Enter your Fruit:- "))
while True:
 fruits = ["apple", "kiwi", "banana", "cherry", "grapes", "orange"]
 if x==("apple"):
    print("This Fruits is already available in your list.")
    break
 elif x==("kiwi"):
    print("This Fruits is already available in your list.")
    break
 elif x==("banana"):
    print("This Fruits is already available in your list.")
    break
 elif x==("cherry"):
    print("This Fruits is already available in your list.")
    break
 elif x==("grapes"):
    print("This Fruits is already available in your list.")
    break
 elif x==("orange"):
    print("This Fruits is already available in your list.")
    break
 else:
    print("This Fruits is not available in your list.")
    break

print('-------------------------------------------------------- -:ADDITIONAL PROGRAMS:- ----------------------------------------------------')
(1).
number = int(input("Enter a number:  "))    
print(len(str(number)))

(2).



(3).
fruits = ["apple", "kiwi", "banana", "cherry", "grapes", "orange"]
name = "apple"
i = 0
while i < len(name):
    print(name[i])
    i += 1
print('---------------------------------------------------------------------------------------------------------------------------------')
name = "kiwi"
i = 0
while i < len(name):
    print(name[i])
    i += 1
print('---------------------------------------------------------------------------------------------------------------------------------')
name = "banana"
i = 0
while i < len(name):
    print(name[i])
    i += 1
print('---------------------------------------------------------------------------------------------------------------------------------')
name = "cherry"
i = 0
while i < len(name):
    print(name[i])
    i += 1
print('---------------------------------------------------------------------------------------------------------------------------------')
name = "grapes"
i = 0
while i < len(name):
    print(name[i])
    i += 1
print('---------------------------------------------------------------------------------------------------------------------------------')
name = "orange"
i = 0
while i < len(name):
    print(name[i])
    i += 1

(4).

num = int(input("Enter your number:- "))
i = 2
flag = 1
while i < num: # i=2,3,4,5,6,7,...,640
    if num % i == 0:
        print("Your Number is Not Prime.")
        flag = 0
        break
    i += 1
if flag == 1:
    print("Your Number is Prime.")

(5).

num = int(input("Enter your number:- "))

sum = 0
for i in range(1,num):
     if num%i == 0:
      sum= sum +i
     if sum == num:
      print(num,"is a Perfect number.")
      break
else:
      print(num,"is a Not Perfect number.")
     
(6).

num = int(input("Enter your number:- "))

sum=0
temp=num
while temp>0:
    digit=temp%10
    cube=digit**3
    sum=sum+cube
    temp//=10
if num==sum:
      print(num,"is a Armstrong number.")
else:
        print(num,"is a Not Armstrong number.")

(7).
start=int(input("Enter Start Number:- "))
end=int(input("Enter End Number:- "))
print("Prime Number in the Range",start,"to",end)
for i in range(start,end+1):
    count=0
    for j in range(2,i):
        if(i%j==0):
            count = 1
            break
    if (count==0) and i!=1:
        print(i,end=' ')

(8).

start=int(input("Enter Start Number:- "))
end=int(input("Enter End Number:- "))





(9).

start=int(input("Enter Start Number:- "))
end=int(input("Enter End Number:- "))

for num in range(start,end+1):
    length=len(str(num))
    sum=0
    temp=num
    while temp>0:
        digit=temp%10
        sum+=digit**length
        temp//=10

        if num==sum:
            print(num)



fruits = ["apple", "kiwi", "banana", "cherry", "grapes", "orange"]
i=0
while i<len(fruits):
     print(fruits[i])
     i+=1
    
     if fruits==("cherry"):
        continue'''

# def prime(n):
#      count=0
#      for i in range(1,n+1):
#           if n%i==0:
#                count=count+1
#           if(count==2):
#                return 1
#           else:
#                return 0
#      n=int(input("Enter your Number:- "))  
#      r=prime(n) 
#      if(r==1): 
#            print("Prime Number")
#      else:
#           print("Not Prime Number")



    
   
   