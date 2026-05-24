# 1. Print numbers from 1 to 5
for number in range(1, 6):
    print(number)
    
    
# 2. Print names from a list
friends = ["Ali", "Ahmed", "Sara"]
for friend in friends:
    print(friend)
    
    
# 3. Print table of 2
for i in range(1, 11):
    print("2 x", i, "=", 2 * i)
    
    
# 4. Print fruits one by one
fruits = ["Apple", "Banana", "Mango"]
for fruit in fruits:
    print("I like", fruit)
    
    
# 5. Print even numbers
for number in range(2, 11, 2):
    print(number)
    
    
    # ----->>>>    WHILE LOOP <<<<-----
    
# 1. Count from 1 to 5
count = 1
while count <= 5:
    print(count)
    count += 1
    
    
# 2. Simple password attempts
attempts = 3
while attempts > 0:
    print("Try again")
    attempts -= 1
    
    
# 3. Countdown from 5
number = 5
while number > 0:
    print(number)
    number -= 1
    
    
# 4. Print a message 4 times
count = 1
while count <= 4:
    print("Learning Python")
    count += 1
    

# 5. Add numbers until 3
num = 1
total = 0
while num <= 3:
    total += num
    num += 1
print("Total:", total)