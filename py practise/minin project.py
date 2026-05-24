# student test checker

student_name = input("enter student name: ")
marks = int(input("enter marks: "))
print("student name:", student_name)
print("marks:", marks)
if marks >= 80:
    print("grade: A")
elif marks >= 60:
    print("grade: B")
else:
    print("grade: C")

# ongratulation message
count = 1
while count <= 1:
    print("keep working hard!")
    count += 1
    

# number guesser 
print("------------------->>>>>>>>>>  Number Guesser  <<<<<<<<<<-------------------")

secret_number = 35

while True:
    guess = int(input("enter a number between 30 to 40: "))
    print("your guess number is:", guess)
    if guess < 30:
        print("Too Low! enter number between 30 to 40")
    elif guess > 40:
        print("Too High! enter number between 30 to 40")
    elif guess == secret_number:
        print("correct guess!")
        break
    elif guess < secret_number:
        print("your number is smaller than the secret number")
    else:
        print("your number is greater than the secret number")
print("game finished")