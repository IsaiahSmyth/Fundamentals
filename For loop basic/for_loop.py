# Basic
for num in range (0,151):
    print(num)

# Multiple of 5
for nums in range (5, 1001, 5):
    print(nums)

# Counting, the Dojo Way
for number in range (1, 101):
    print(number)
    if number % 5:
        print("Dojo")
        if number % 10:
            print("Coding Dojo")

# Whoa. That Sucker's Huge
# sum is a global variable so it doesn't repeat
sum = 0
for numbers in range (1, 5000, 2):
    
    
    sum += numbers
print(sum)
    

# Countdown by four
for positive_number in range (0,2018,2):
  print(positive_number)
for numbers in range (2018, 0, -4):
  print(numbers)

# Flexible Counter
lowNum = 2
highNum = 9
mult = 3

for flexible_Counter in range (lowNum, highNum+1):
    if flexible_Counter % 3 ==0:

        print(flexible_Counter)
