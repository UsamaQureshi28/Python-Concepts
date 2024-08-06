#It is just like a Switch condition

age=int(input("Enter Your age: "))
match age:
    case 17:
        print("You are below 18")
    case 18:
        print("You are 18")
    case 19:
        print("You are over 18")
    case _:
        print("No match Found")