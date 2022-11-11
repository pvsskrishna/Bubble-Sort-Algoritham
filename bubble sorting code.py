list=eval(input("enter the Homogenous list collection"))
#list=[5,35,10,1,7]
for passno in range(1,len(list)):
   for i in range(0,len(list)-passno):
      if list[i]>list[i+1]:
         list[i],list[i+1]=list[i+1],list[i]
print(list)
