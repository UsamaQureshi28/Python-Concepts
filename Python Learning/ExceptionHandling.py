try:
    number=int(input("Enter Number: "))
    print(number+63)
#except:
except Exception as E:      #To check which type of exception occur
    print("Some Error Occur",E)