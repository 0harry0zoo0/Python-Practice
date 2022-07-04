import random
import math
import json
from bokeh.plotting import figure, show, output_file
import datetime
import os

"""
# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
#1
name_1 = str(input("name: "))
age_1 = int(input("age: "))
print(name_1 + ", you will be 100 years old in the year " + str(100 - age_1 + 2022) + ".")

# Ask the user for a number.
# Depending on whether the number is even or odd, print out an appropriate message to the user.
#2
num_2 = int(input("number: "))
if num_2%2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# Write a program that prints out all the elements of the list that are less than 5.
#3
list_3 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in list_3:
    if i<5:
        print(i)

# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
#4
num_4 = int(input("number: "))
list_4 = []
for i in range(1, num_4 + 1):
    if num_4%i == 0:
        list_4.append(i)
print(list_4)

# Write a program that returns a list that contains only
# the elements that are common between the lists (without duplicates).
#5
list_5a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_5b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
common_10 = []
for i in list_5a:
    if i in list_5b:
        if i not in common:
            common.append(i)
print(common)

# Ask the user for a string and print out whether this string is a palindrome or not.
#6
string_6 = input("string: ")
palindrome_6 = True
for i in range(0, len(string_6)):
    if string_6[i] != string_6[len(string_6) - 1 - i]:
        palindrome_6 = False
print("This statement of this string being a palindrome is " + str(palindrome_6).lower() + ".")

# Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
#7
list_7 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
even_7 = []
for i in list_7:
    if i%2 == 0:
        even_7.append(i)
print(even_7)

# Make a two-player Rock-Paper-Scissors game.
#8
play_8 = True
while play_8:
    player_1_8 = input("Player 1 choose rock, paper, or scissors: ")
    player_2_8 = input("Player 2 choose rock, paper, or scissors: ")
    if player_1_8 == player_2_8:
        print("The two player have tied, one more round.")
    elif (player_1_8 == "rock" and player_2_8 == "scissors") or (player_1_8 == "paper" and player_2_8 == "rock") or (player_1_8 == "scissors" and player_2_8 == "paper"):
        print("Player 1 wins.")
        play_8 = False
    else:
        print("Player 2 wins.")
        play_8 = False

# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
#9
random_9 = random.randint(1, 10)
guess = int(input("Guess a number from 1 to 9: "))
while guess != random_9:
    if guess > random_9:
        guess = int(input("Too high!\nGuess again: "))
    elif guess < random_9:
        guess = int(input("Too low!\nGuess again: "))
    if guess == random_9:
        print("You got it.")

# Write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
# Write it using list comprehensions.
#10
list_10a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_10b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
common_10 = [i for i in list_10a if i in list_10b]
for i in common_10:
    while common_10.count(i) > 1:
        common_10.remove(i)
print(common_10)

# Ask the user for a number and determine whether the number is prime or not.
#11
number_11 = int(input("number: "))
prime = True
for i in range(2, number_11):
    if number_11%i == 0:
        prime = False
print("The statement that " + str(number_11) + " is prime is " + str(prime).lower() + ".")

# Write a program that takes a list of numbers and makes a new list of only the first and last elements of the given list.
#12
list_12 = [5, 10, 15, 20, 25]
new_list_12 = [list_12[0], list_12[len(list_12) - 1]]
print(new_list_12)

# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
#13
fibonacci_13 = [1, 1]
amount_13 = int(input("amount: "))
if amount_13 == 0:
    print("[]")
elif amount_13 == 1:
    print("[1]")
else:
    while amount_13 > 2:
        fibonacci_13.append(fibonacci_13[len(fibonacci_13) - 2] + fibonacci_13[len(fibonacci_13) - 1])
        amount_13 -= 1
    print(fibonacci_13)

# Write a program (function!) that takes a list and returns a new list
# that contains all the elements of the first list minus all the duplicates.
#14
def remove_dup_14(input):
    new = []
    for i in input:
        if i not in new:
            new.append(i)
    return new
print(remove_dup_14([1, 1, 2, 3, 5]))

# Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order.
#15
def string_backwards_15(input):
    new = ""
    for i in range(0, len(input)):
        new += input[len(input) - 1 - i]
    return new
print(string_backwards_15("qwerty"))

# Generate a random password.
#16
length = int(input("length of password: "))
characters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()-_=+[{]}\|;:'\",<.>/?"
password = ""
while length > 0:
    password += characters[random.randint(0, len(characters))]
    length -= 1
print(password)

# Create a program that will play the “cows and bulls” game with the user. The game works like this:
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number.
# For every digit that the user guessed correctly in the correct place, they have a “cow”.
# For every digit the user guessed correctly in the wrong place is a “bull.”
# Every time the user makes a guess, tell them how many “cows” and “bulls” they have.
# Once the user guesses the correct number, the game is over.
# Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.
#18
number_18 = [random.randint(1, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)]
count_18 = 0
guess = input("guess a 4-digit number: ")
while guess != str(number_18[0]) + str(number_18[1]) + str(number_18[2]) + str(number_18[3]):
    count_18 += 1
    cow_18 = 0
    bull_18 = 0
    bull_limit_18 = 0
    for i in range(0, 4):
        if guess[i] not in guess[0:i] and i != 0:
            bull_limit_18 = 0
        if number_18[i] == int(guess[i]):
            cow_18 += 1
            bull_limit_18 += 1
        elif int(guess[i]) in number_18 and bull_limit_18 < number_18.count(int(guess[i])):
            bull_18 += 1
            bull_limit_18 += 1
    if guess == "0000":
        print(number_18)
    if guess != str(number_18[0]) + str(number_18[1]) + str(number_18[2]) + str(number_18[3]):
        print(str(cow_18) + " cows, " + str(bull_18) + " bulls")
        guess = input("guess a 4-digit number: ")
print("You guessed correct! You took ") + str(count_18) + " guess(es)."

# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest)
# and another number. The function decides whether or not the given number is inside the list and returns
# (then prints) an appropriate boolean.
#20
list_20 = [10, 23, 26, 78, 101, 300]
guess_20 = 10
def in_or_not_20(list, guess):
    return guess_20 in list_20
print(in_or_not_20(list_20, guess_20))

# Given two .txt files that have lists of numbers in them, find the numbers that are overlapping.
#23
import os
os.getcwd()
os.chdir("/Users/simplepineapples/PycharmProjects/Practice")
read_prime_23 = open('primes_under_1000.txt', "r")
read_happy_23 = open('happy_under_1000.txt', "r")
primes_23 = read_prime_23.read().split(", ")
happy_23 = read_happy_23.read().split(", ")
common_23 = []
for i in primes_23:
    if i in happy_23:
        common_23.append(i)
print(common_23)

# Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.
#24
size_24 = input("board size: ")
dimensions_24 = size_24.split('x')
for i in range(0, int(dimensions_24[1]) + 1):
    for j in range(0, int(dimensions_24[0])):
        print(" ___", end= "")
    print("\n")
    if i != int(dimensions_24[1]):
        print("|", end= "")
        for j in range(0, int(dimensions_24[0])):
            print("   ", end="|")
    print("\n")

# Write a program that guesses a number between 0-100 that the user has chosen.
#25
response_25 = ""
numbers_25 = [i for i in range(1, 100)]
alter_25 = numbers_25.copy()
while response_25 != "correct":
    guess_25 = alter_25[math.floor(len(alter_25)/2)]
    print(guess_25)
    response_25 = input("is " + str(guess_25) + " high, low, or correct: ")
    if response_25 == "high":
        alter_25 = numbers_25[numbers_25.index(alter_25[0]):guess_25 - 1]
        print(alter_25)
    if response_25 == "low":
        alter_25 = numbers_25[guess_25:numbers_25.index(alter_25[-1]) + 1]
        print(alter_25)

# Make a tic-tac-toe winner checker.
#26
def tic_tac_toe_checker_26(lists):
    if (lists[0][0] == lists[0][1] == lists[0][2] or lists[0][0] == lists[1][0] == lists[2][0]) and lists[0][0] != 0:
        return lists[0][0]
    elif (lists[2][0] == lists[2][1] == lists[2][2] or lists[0][2] == lists[1][2] == lists[2][2]) and lists[2][2] != 0:
        return lists[2][2]
    elif (lists[1][0] == lists[1][1] == lists[1][2] or lists[0][1] == lists[1][1] == lists[2][1] or lists[0][0] == lists[1][1] == lists[2][2] or lists[2][0] == lists[1][1] == lists[0][2]) and lists[1][1] != 0:
        return lists[1][1]
    else:
        return 0
def winner_statement_26(number):
    if number == 0:
        print("There is currently no winner.")
    else:
        print("The winner is player " + str(number) + ".")

# Create a function to print out and place symbols on a tic-tac-toe board.
#27
def place_symbol_27(symbol, location, board):
    location_list = location.split(",")
    new_board = board.copy()
    new_board[int(location_list[0]) - 1][int(location_list[1]) - 1] = symbol
    return new_board
def play_ttt_27():
    board = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    while 0 == 0:
        placement = input("Player 1 pick a coordinate to place your symbol (R,C): ")
        board = place_symbol_27("X", placement, board)
        print(board[0])
        print(board[1])
        print(board[2])
        placement = input("Player 2 pick a coordinate to place your symbol (R,C): ")
        board = place_symbol_27("O", placement, board)
        print(board[0])
        print(board[1])
        print(board[2])
play_ttt_27()

# Implement a function that takes as input three variables, and returns the largest of the three.
# Do this without using the Python max() function!
#28
def max_of_three_28(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num3:
        return num2
    else:
        return num3
print(max_of_three_28(3, 2, 2))

# Use the previous functions created to make a functional tic-tac-toe game.
# Create a congratulatory message for the winner and stop if there are no more moves left.
#29
def place_symbol_29(symbol, location, board):
    location_list = location.split(",")
    new_board = board.copy()
    new_board[int(location_list[0]) - 1][int(location_list[1]) - 1] = symbol
    return new_board
def tic_tac_toe_checker_29(lists):
    if (lists[0][0] == lists[0][1] == lists[0][2] or lists[0][0] == lists[1][0] == lists[2][0]) and lists[0][0] != 0:
        return lists[0][0]
    elif (lists[2][0] == lists[2][1] == lists[2][2] or lists[0][2] == lists[1][2] == lists[2][2]) and lists[2][2] != 0:
        return lists[2][2]
    elif (lists[1][0] == lists[1][1] == lists[1][2] or lists[0][1] == lists[1][1] == lists[2][1] or lists[0][0] == lists[1][1] == lists[2][2] or lists[2][0] == lists[1][1] == lists[0][2]) and lists[1][1] != 0:
        return lists[1][1]
    else:
        return 0
def print_board_29(board):
    size = "3x3"
    dimensions = size.split('x')
    for i in range(0, int(dimensions[0]) + 1):
        for j in range(0, int(dimensions[1])):
            print(" ___", end="")
        print("")
        if i != int(dimensions[0]):
            print("|", end="")
            for j in range(0, int(dimensions[1])):
                print(" " + str(board[i][j]) + " ", end="|")
        print("")
def play_ttt_29():
    board = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    winner = False
    turns = 0
    while not winner and turns < 9:
        placement = input("Player 1 pick a coordinate to place your symbol (R,C): ")
        board = place_symbol_29("X", placement, board)
        print_board_29(board)
        if tic_tac_toe_checker_29(board) != 0:
            winner = True
        turns += 1
        if turns < 9 and not winner:
            placement = input("Player 2 pick a coordinate to place your symbol (R,C): ")
            board = place_symbol_29("O", placement, board)
            print_board_29(board)
            if tic_tac_toe_checker_29(board) != 0:
                winner = True
            turns += 1
    if tic_tac_toe_checker_29(board) == 0:
        print("No one won.")
    else:
        if tic_tac_toe_checker_29(board) == "X":
            print(("Player 1 has won."))
        else:
            print("Player 2 has won.")
play_ttt_29()

# In this exercise, the task is to write a function that picks a random word
# from a list of words from the SOWPODS dictionary.
#30
dictionary_30 = open("engmix.txt", "r")
word_list_30 = dictionary_30.read().split("\n")
word_30 = word_list_30[random.randint(0, len(word_list_30))]
print(word_30)

# In the game of Hangman, a clue word is given by the program that the player has to guess, letter by letter.
# The player guesses one letter at a time until the entire word has been guessed.
#31
dictionary_31 = open("engmix.txt", "r")
word_list_31 = dictionary_31.read().split("\n")
word_31 = word_list_31[random.randint(0, len(word_list_31))]
answer_31 = "_"*(len(word_31))
guessed_31 = []
print("Welcome to hangman!")
print(answer_31)
while answer_31 != word_31:
    letter_guess_31 = input("Guess your letter: ")
    if letter_guess_31 not in guessed_31 and letter_guess_31 in word_31:
        for i in range(0, len(word_31)):
            if word_31[i] == letter_guess_31:
                answer_31 = answer_31[0:i] + word_31[i] + answer_31[i + 1:len(answer_31)]
        guessed_31.append(letter_guess_31)
        print(answer_31)
    elif letter_guess_31 in guessed_31:
        print("You already guessed this letter.")
    else:
        print("Incorrect.")
        guessed_31.append(letter_guess_31)
print("You guessed the word!")

# Create the full hangman game using code before with only 6 tries.
dictionary_32 = open("engmix.txt", "r")
word_list_32 = dictionary_32.read().split("\n")
word_32 = word_list_32[random.randint(0, len(word_list_32))]
answer_32 = "_"*(len(word_32))
guessed_32 = []
tries_32 = 6
print("Welcome to hangman!")
print(answer_32)
while answer_32 != word_32 and tries_32 > 0:
    letter_guess_32 = input("Guess your letter: ")
    if letter_guess_32 not in guessed_32 and letter_guess_32 in word_32:
        for i in range(0, len(word_32)):
            if word_32[i] == letter_guess_32:
                answer_32 = answer_32[0:i] + word_32[i] + answer_32[i + 1:len(answer_32)]
        guessed_32.append(letter_guess_32)
        print(answer_32)
    elif letter_guess_32 in guessed_32:
        print("You already guessed this letter.")
    else:
        print("Incorrect.")
        tries_32 -= 1
        print("You have " + str(tries_32) + " tries left.")
        guessed_32.append(letter_guess_32)
if tries_32 == 0:
    print("You did not guess the word.\nThe word was " + word_32 + ".")
else:
    print("You guessed the word!")

# Create a dictionary (in your file) of names and birthdays.
# When you run your program it should ask the user to enter a name, and return the birthday of that person back to them.
#33
birthdays_33 = {"Josh Tinham":"03/22/2005", "Bertha Lee":"05/12/2008", "Benjamin Franklin":"01/17/1706"}
print("We have the birthdays of: ")
for i in birthdays_33.keys():
    print(i)
who_33 = input("Who do you want the birthday of: ")
print("The birthday of " + who_33 + " is " + birthdays_33[who_33] + ".")

# In this exercise, modify your program from Part 1 to load the birthday dictionary from a JSON file on disk,
# rather than having the dictionary defined in the program.
#34
put_in_34 = open("birthdays.json", "w")
json.dump({"Josh Tinham":"03/22/2005", "Bertha Lee":"05/12/2008", "Benjamin Franklin":"01/17/1706"}, put_in_34)
put_in_34.close()
check_34 = open("birthdays.json", "r")
birthdays_34 = json.load(check_34)
print("We have the birthdays of: ")
for i in birthdays_34.keys():
    print(i)
who_34 = input("Who do you want the birthday of: ")
print("The birthday of " + who_34 + " is " + birthdays_34[who_34] + ".")

# In the previous exercise we saved information about famous scientists’ names and birthdays to disk.
# In this exercise, load that JSON file from disk, extract the months of all the birthdays,
# and count how many scientists have a birthday in each month.
#35
check_35 = open("birthdays.json", "r")
birthdays_35 = json.load(check_35)
def number_to_month_35(number_string):
    if number_string == "01":
        return "Jan."
    elif number_string == "02":
        return "Feb."
    elif number_string == "03":
        return "Mar."
    elif number_string == "04":
        return "Apr."
    elif number_string == "05":
        return "May."
    elif number_string == "06":
        return "Jun."
    elif number_string == "07":
        return "Jul."
    elif number_string == "08":
        return "Aug."
    elif number_string == "09":
        return "Sep."
    elif number_string == "10":
        return "Oct."
    elif number_string == "11":
        return "Nov."
    else:
        return "Dec."
months_35 = []
for i in birthdays_35.keys():
    months_35.append(number_to_month_35(birthdays_35[i][0:2]))
month_count_35 = {}
for i in months_35:
    if i not in month_count_35.keys():
        month_count_35[i] = months_35.count(i)
print(month_count_35)

# In this exercise, use the bokeh Python library to plot a histogram of which months the scientists have birthdays in!
#36
check_36 = open("birthdays.json", "r")
birthdays_36 = json.load(check_36)
def number_to_month_36(number_string):
    if number_string == "01":
        return "Jan."
    elif number_string == "02":
        return "Feb."
    elif number_string == "03":
        return "Mar."
    elif number_string == "04":
        return "Apr."
    elif number_string == "05":
        return "May."
    elif number_string == "06":
        return "Jun."
    elif number_string == "07":
        return "Jul."
    elif number_string == "08":
        return "Aug."
    elif number_string == "09":
        return "Sep."
    elif number_string == "10":
        return "Oct."
    elif number_string == "11":
        return "Nov."
    else:
        return "Dec."
months_36 = []
for i in birthdays_36.keys():
    months_36.append(number_to_month_36(birthdays_36[i][0:2]))
month_count_36 = {}
for i in months_36:
    if i not in month_count_36.keys():
        month_count_36[i] = months_36.count(i)
output_file("practice_36_output.html")
chart_36 = figure(x_range=[i for i in month_count_36.keys()])
chart_36.vbar(x=[i for i in month_count_36.keys()], top=[month_count_36[i] for i in month_count_36.keys()], width=0.8)
chart_36.xgrid.grid_line_color = None
chart_36.y_range.start = 0
show(chart_36)

# So in this exercise, we will be stretching our functions muscle by refactoring
# an existing code snippet into using functions.
# Here is the code snippet to refactor (taken from a correct but very repeated solution to exercise 24 on this website):
#37
size_37 = input("board size: ")
dimensions_37 = size_37.split('x')
def horizontal_37(width):
    print(" ___" * width)
def vertical_37(width):
    print("|   " * width, end="|\n")
for i in range(0, int(dimensions_37[1])):
    horizontal_37(int(dimensions_37[0]))
    vertical_37(int(dimensions_37[0]))
horizontal_37(int(dimensions_37[0]))

# Implement the same exercise as Exercise 1 (Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old),
# except use f-strings instead of the + operator to print the resulting output message.
#38
name_38 = str(input("name: "))
age_38 = int(input("age: "))
print(f"{name_38}, you will be 100 years old in the year {100 - age_38 + 2022}.")

# Use the built-in Python datetime library to make the code you write work during every year,
# not just the one we are currently in.
#39
name_39 = str(input("name: "))
age_39 = int(input("age: "))
current_year = datetime.datetime.now().year
print(name_39 + ", you will be 100 years old in the year " + str(100 - age_39 + current_year) + ".")
"""
