# 1- Given a list of numbers, create a function that returns a list where all similar adjacent
# elements have been reduced to a single element, so [1,2,3.3] returns [1,2,3]
# Note:
# You may create a new list or modify the passed in list.

def reduce_adjacent_duplicates(nums):
    result = []
    for num in nums:
        if not result or num != result[-1]:
            result.append(num)
    return result

nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5]
print(reduce_adjacent_duplicates(nums))  

#-----------------------------------------------------------------------------------------------------------------------#

# 2- Consider dividing a string into two halves
# Case1:
# The length is even, the front and back halves are the same length.
# Case2:
# The length is odd, we’ll say that the extra char goes in the front half.
# E.g. ‘abced’, the front half is ‘abc’, the back half’de.
# Given 2 strings, a and b, return a string of the form:
# (a-front + b-front) + (a-back +b-back)

def string_divider(a, b):
    mid_a = (len(a) + 1) // 2
    mid_b = (len(b) + 1) // 2
    
    return a[:mid_a] + b[:mid_b] + a[mid_a:] + b[mid_b:]

print(string_divider("Nardine", "William"))  
print(string_divider("Apple", "juice"))  

#-----------------------------------------------------------------------------------------------------------------------#

# 3- Write a Python function that takes a sequence of numbers and determines
# whether all the numbers are different from each other.
# E.X. [1,5,7,9] -> True
# [2,4,5,5,7,9] -> False

def different_numbers(nums):
    return len(nums) == len(set(nums))

print(different_numbers([1, 5, 7, 9]))       
print(different_numbers([2, 4, 5, 5, 7, 9]))  

#-----------------------------------------------------------------------------------------------------------------------#

# 4- Given unordered list, sort it using algorithm bubble sort

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [15, 21, 10, 86, 17, 33, 47]
bubble_sort(arr)
print("Sorted array:", arr)

#-----------------------------------------------------------------------------------------------------------------------#

# 5- Gusses game
# ● Your game generates a random number and gives only 10 tries for the user to guess that number.
# ● Get a user input and compare it with the random number
# ● Display a hit message to the user in case the use number is smaller or bigger of the random number
# ● If the user type number is out of range(100), display a message that is not allowed and don’t count this as try.
# ● If user type a number that has been entered before, display a hint message and don’t count this as try
# ● In case the user entered a correct number within the 10 tries, display a congratulations message 
#   and let your application guess another random number with the remain number of tries
# ● If the user finishes all his tries, display a message to ask him if he wants to play again or not.

import random

def guessing_game():
    random_num = random.randint(1, 100)
    tries = 10
    guessed_nums = set()

    print("Welcome to the Guessing Game!")
    print("You have 10 tries to guess the number between 1 and 100.")

    while tries > 0:
        guess = input("Enter your guess: ")

        if not guess.isdigit():
            print("Please enter a valid number between 1 and 100.")
            continue

        guess = int(guess)

        if guess < 1 or guess > 100:
            print("Number out of range! Please enter a number between 1 and 100.")
            continue

        if guess in guessed_nums:
            print("You've already guessed this number. Try a different one.")
            continue

        tries -= 1
        guessed_nums.add(guess)

        if guess == random_num:
            print("Congratulations! You've guessed the correct number:", random_num)
            if tries > 0:
                print("Let's play again! You have", tries, "tries left.")
                random_num = random.randint(1, 100)
                guessed_nums.clear()
            else:
                print("You've run out of tries.")
                break

        elif guess < random_num:
            print("Your guess is smaller than the number. Try a bigger one.")
        else:
            print("Your guess is bigger than the number. Try a smaller one.")

    else:
        print("The correct number was:", random_num)
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == "yes":
            guessing_game()
        else:
            print("Thank you for playing!")

guessing_game()