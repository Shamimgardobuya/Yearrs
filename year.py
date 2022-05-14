print("This is a function that shows a year if its leap or not")

def time(a):
    if (a%4==0):
        print("This is a leap year and will have 29 days in Feb")
    elif(a%4!=0):
        print(f"{a} is not a leap year")
