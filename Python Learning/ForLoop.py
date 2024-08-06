       #For Loop

for i in range(5):
    if(i==3):
        #break
        continue       #Skip the next statement of loop
    print(i)
a=[2,4,6,8,10,12,14,16,18,20]
for items in a:
    print(items)
num=int(input("Enter Number: "))
for i in range(1,11):
    print(num," X ",i," = ",num*i)