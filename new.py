# a = "Apple"

# for i in a: 
#     if i == "l":
#         continue
#     print(i)
# else:
#     pass

# b = "People"
# for i in b:
#     if i=="o":
#         break
#     print(i)

c = [1,2,3,4,5]
i = 0
sum = 0
while i<len(c):
 if c[i]== 4:
    print(i)
    break
 else:
   sum+=c[i]
   i+=1
print(sum)



