'''
print("Hello Usama")     # Ctrl+D
print("Hello World")     # Alt+Shift+UpArrow
# Comments

# print("Hello World")
# print("Hello World")
# print("Hello World")     # Ctrl+/   and "' '"f

#Variables

a=1
print(a)
b=6.2
print(b)
c=True
print(c)
d=None
print(d)
e="Usama"
print(e[0:4])  #4-1
#Change DataType

f=10
g="23"
print(f+int(g))
#Operators
Num1=56
Num2=45
print(Num1+Num2)
print(Num1-Num2)
print(Num1*Num2)
print(Num1/Num2)
print(Num1%Num2) #For Remainder
print(Num1//Num2) #Remove Decimal values after point
print(Num1**Num2) #Exponential

print(e.capitalize())
print(e.upper())
print(e.count("a"))
print(e.isalnum())
print(e.find("Y"))
print(e.find("s"))
print(a.is_integer())
print(e.isnumeric())
'''
# name=input("Enter Your Name: ")
# print(name)
# number=input("Enter Number: ")
# print(int(number)+19)
MLString='''Process finished with
exit code 0  as a string'''
print(MLString)
name1=("Usama")  #Strings are immutable
l1=[1,5.6,"Usama",None,10] #Lists are mutable
print(l1)
l1.remove(None)
print(l1)
l1.append("Qureshi")
print(l1)
l1.extend([3,"Hashim",9.8,56])
print(l1)
print(l1.index("Hashim"))