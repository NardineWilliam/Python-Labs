# 1- Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(last_name + " " + first_name)

#-----------------------------------------------------------------------------------------------------------------------#

# 2- Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
n = int(input("Enter an integer: "))
result = n + int(str(n) * 2) + int(str(n) * 3)
print("Result:", result)

#-----------------------------------------------------------------------------------------------------------------------#

# 3- Write a Python program to print the following here document
here_document = '''
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example
'''
print(here_document)

#-----------------------------------------------------------------------------------------------------------------------#

# 4- Write a Python program to get the volume of a sphere with radius 6.
import math
radius = 6
volume = (4/3) * math.pi * radius**3
print("Volume of the sphere with radius 6=", volume)

#-----------------------------------------------------------------------------------------------------------------------#

# 5- Write a Python program that will accept the base and height of a triangle and compute the area.
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area = 0.5 * base * height
print("The area of the triangle with base", base, "and height", height, "is:", area)

#-----------------------------------------------------------------------------------------------------------------------#

# 6- Write a Python program to construct the following pattern, using a nested for loop.
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

for i in range(rows - 1, 0, -1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

#-----------------------------------------------------------------------------------------------------------------------#

# 7- Write a Python program that accepts a word from the user and reverse it.
word = input("Enter a word: ")
reversed_word = ''.join(reversed(word))
print("Reversed word:", reversed_word)

#-----------------------------------------------------------------------------------------------------------------------#

# 8- Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
for num in range(7):
    if num != 3 and num != 6:
        print(num)

#-----------------------------------------------------------------------------------------------------------------------#

# 9-Write a Python program to get the Fibonacci series between 0 to 50
# Note : The Fibonacci Sequence is the series of numbers :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it.
# Expected Output : 1 1 2 3 5 8 13 21 34
current = 0
next_num = 1
print(current, end=" ")
while next_num <= 50:
    print(next_num, end=" ")
    temp = current
    current = next_num
    next_num = temp + next_num

#-----------------------------------------------------------------------------------------------------------------------#

# 10-write a python program that accepts a string and calculate the number of digits and letters
string = input("Enter a string: ")

digit = 0
letter = 0

for char in string:
    if char.isdigit():
        digit += 1
    elif char.isalpha():
        letter += 1

print("Number of digits:", digit)
print("Number of letters:", letter)