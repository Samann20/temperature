l1=[]
for i in range(0,8):
    print("enter the temperature:",end="")
    no=eval(input())
    l1.append(no)
print(l1)

l2=[1,2,3,4,5,6,7,8,9,10]
print(l2)

max=l2[0]
for i in range(0,len(l2)):
  if l2[i]>max:
    max=l2[i]
print(max)

del(l2[3])
 print(l2)

list1=[x for x in range(0,5)]
list1

list2=[0.5*x for x in list1]
print(list2)

print
