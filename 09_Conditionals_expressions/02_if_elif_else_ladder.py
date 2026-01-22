age = int(input("enter your age : "))

if (age > 18):
    print("you are eligible to drive a car")
    
elif (age<0):
    print("you are entering an invalid age !")
    
elif (age==0):
    print("you are entering a 0 age !")
    
else:
    print("you are not eligible for driving a car ")