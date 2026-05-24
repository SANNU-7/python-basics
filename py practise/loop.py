# a for loop repeats code a specific number  of time . 
for i in range (1,7):
    print ("count:", i)

    
students = ["salar", "junaid ", "sanan"]
for student in students:
    print("Hello", student)

# while loop :  loops keep repeating until condition is true 

count = 1 
while count <= 7:
    print("count:", count)
    count += 1 
    
# Basic problem solvong :

    # step 1 --> understand the problem clearly 
    # step 2 --> write step in plan english
    # stpe 3 --> translate steps into python code or other computer language 
    # step 4--> test with different inputs
    # step 5 --> fix errors 


secret = 7
while True :
    guess = int(input("enter you gussing number between 1 to 10: "))
    if guess == 7:
        print("you won")
        break
    elif guess > 10:
        print("please enter num between 1 to 10")
    elif guess < 1:
        print("please enter num between 1 to 10")
    else :
        print("your guess is worng ")






















