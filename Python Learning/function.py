def DisplayName(name):
    st=f"Hello my name is {name}"
    print(st)
    print("Hello "+name)
def Average(a,b):
    print(f"Average of {a} and {b} is ",(a+b)/2)
name=input("Enter Name: ")
DisplayName(name)
Average(45,34)