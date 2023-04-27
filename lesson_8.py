import random
import math
# Task 1. Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).


def the_numbe_of_odd(first_num: int, second_num: int) -> int:
    counter_ = 0
    if first_num < second_num:
        for i in range(first_num, second_num + 1):
            if i % 2 != 0:
                counter_ += 1
    else:
        print("Wrong order")
    return counter_

# Task 2. You are given an array of unique integers salary where salary[i] is the salary of the ith employee.
# Return the average salary of employees excluding the minimum and maximum salary.


def average_salary(salery: list) -> int:
    sum_ = 0
    for i in salery:
        if i != max(salery) and i != min(salery):
            sum_ += i
    return sum_/(len(salery) - 2)


# Practice 1

# Create emtpy dictionary named en_ua_dictionary.

en_ua_dictionary = {}

# Add few key-value pairs to the dictionary. Example: 'red': 'червоний'

en_ua_dictionary.update(red='червоний', blue='синій', green='зелений', black='чорний',
                        white='білий', yellow='жовтий', orange='помаранчевий', brown='коричневий')

# Check if the dictionary contains key 'blue' and 'purple'. If not, set their values to unknown.

en_ua_dictionary.setdefault('blue')
en_ua_dictionary.setdefault('purple')

# Create a loop over existing values and print them to the console in the following format: Red in Ukrainian is червоний


def en_ua_loop():
    for i, j in en_ua_dictionary.items():
        print(f'{i} in Ukrainian is {j}')

# Delete all key-values pairs from the dictionary if the lenght of value is lower than 5.


for i in en_ua_dictionary.values():
    if i is not None:
        if len(i) < 5:
            en_ua_dictionary.popitem(i)

# Write a game where user should guess of a capital of the country that you have in your dictionary.
# You should show user a random country from the list and ask him to guess the capital. If user input right capital,
# print "You are right!", add him a point and ask him to guess another country. If not, you should ask again.
# User should be able to quit the game by typing "exit".
# You should print current score after each round. Also, you should print the final score before user quit the game.

# If user make a mistake you should decrement his lives. Initial amount of lives is 3.
# Game will end when user has no lives left.
# You should print the final score after user has no lives left.

# Give user a hint if he guesses wrong. Hint should looks like first letter of the capital.
# If you user make another mistake, you should print one more letter from the capital.

capitals = {'Ukraine': 'Kyiv', 'France': 'Paris', 'Germany': 'Berlin', 'Italy': 'Rome', 'USA': 'Washington', 'Canada': 'Ottawa', 'Switzerland': 'Bern', 'Austria': 'Vienna', 'Belgium': 'Brussels',
            'Sweden': 'Stockholm', 'Norway': 'Oslo', 'Denmark': 'Copenhagen', 'Finland': 'Helsinki', 'Poland': 'Warsaw', 'Romania': 'Bucharest', 'Bulgaria': 'Sofia', 'Greece': 'Athens'}


def guess_the_capital_bad():
    lives = 3
    score = 0
    next_letter = 0
    key_ = random.randint(0, len(capitals.keys()) - 1)
    user_var = input(f'Guess the capital of {tuple(capitals.keys())[key_]}: ')
    check = tuple(capitals.values())[key_] == user_var
    while lives > 0:
        if check:
            next_letter = 0
            score += 1
            print(f'You are right! Your score is {score}')
            key_ = random.randint(0, len(capitals.keys()) - 1)
            user_var = input(
                f'Guess the capital of {tuple(capitals.keys())[key_]}: ')
            check = tuple(capitals.values())[key_] == user_var
        elif user_var == 'Exit':
            print(f'Your final score is {score}')
            break
        else:
            lives -= 1
            print(f'You have {lives} lives left')
            if lives != 0:
                print(
                    f'The next letter is {tuple(capitals.values())[key_][next_letter]}')
                next_letter += 1
                user_var = input(
                    f'Guess the capital of {tuple(capitals.keys())[key_]}: ')
                check = tuple(capitals.values())[key_] == user_var
    print(f'Game is over. Your final score is {score}')


def get_next_country():
    key_ = random.randint(0, len(capitals.keys()) - 1)
    return tuple(capitals.keys())[key_]


def guess_the_capital():
    lives, score, opend_letters = 3, 0, 0

    country = get_next_country()

    while lives > 0:
        input_message = f'Now you unlocked {capitals[country][0:opend_letters]}\n' if opend_letters > 0 else ""
        input_message += f'Guess the capital of {country}: '

        user_answer = input(input_message)

        if user_answer == 'Exit':
            break

        if capitals[country] == user_answer:
            opend_letters = 0
            score += 1
            country = get_next_country()
            print(f'You are right! Your score is {score}\n')
        else:
            lives -= 1
            opend_letters += 1
            print(f'You have {lives} lives left\n')

    if lives > 0:
        print(f'\nCongrats!!! You still have some extra lifes. \nBut you decide to finish, so your final score is {score}')
    else:
        print(f'Game is over. You are looser\nYour final score is just {score}')

# guess_the_capital()
# Task 3

# In an array of integers of length n + 1 (n > 1), every number in the range 1...n appears once except for one number which appears twice
# (so the array’s length is n+1). Write an efficient function that finds the number that appears twice.


def redundant_value(arr: list) -> int:
    return [i for i in arr if arr.count(i) > 1][0]

# Task 4 Intersection
# Given two arrays of numbers where each one contains unique values and is already sorted in ascending order,
# find the number of elements that belong to both arrays.


def belong_to_both_arrays(arr1: list, arr2: list) -> int:
    return len(set(arr1).intersection(set(arr2)))

# Task 5. RLE
# Given a string of letters (without numbers), create a string encoding it by the rules where the first character
# is char itself, followed by a number indicating the number of letter repeats.


def RLE(string: str) -> str:
    new_string = ''
    counter = 1
    for i in range(1, len(string)):
        if string[i-1] != string[i]:
            new_string += string[i-1]
            new_string += str(counter)
            counter = 1
        else:
            counter += 1
    new_string += string[i]
    new_string += str(counter)
    return new_string

# Given a string s, find the length of the longest substring without repeating characters.


def longest_substr_without_rep_char(s: str) -> int:
    check_str = ''
    max_ = 1
    i = 0
    while i < len(s):
        if s[i] not in check_str:
            check_str += s[i]
            i += 1
        else:
            if max_ <= len(check_str):
                max_ = len(check_str)
                i -= len(check_str) - 1
                check_str = ''
            else:
                check_str = ''
    if max_ < len(check_str):
        max_ = len(check_str)
    return max_

# Write an algorithm to determine if a number n is happy.


def is_happy_number(number: int) -> bool:
    loop = (4, 16, 37, 58, 145, 42, 20)
    sum_ = 0
    while number not in loop:
        number = str(number)
        for i in number:
            i = int(i)
            sum_ += i**2
        number = sum_
        sum_ = 0
        if number == 1:
            return True
    return False

# Given a roman numeral, convert it to an integer.


def roman_to_int(roman: str) -> int:
    roman_dict = {"I": 1, "V": 5, "X": 10,
                  "L": 50, "C": 100, "D": 500, "M": 1000}
    summ = 0
    i = 0
    while i < len(roman):
        a1 = roman_dict.get(roman[i])
        if i == len(roman) - 1:
            summ += roman_dict.get(roman[i])
            break
        a2 = roman_dict.get(roman[i+1])
        if a1 >= a2:
            summ += roman_dict.get(roman[i])
            i += 1
        else:
            if i == 0:
                summ += roman_dict.get(roman[i+1])
                summ -= roman_dict.get(roman[i])
                i += 2
            else:
                summ += roman_dict.get(roman[i+1]) - roman_dict.get(roman[i])
                i += 2
    return summ

print(roman_to_int("CCLXXXIV"))
def test_roman_to_int():
    result1 = roman_to_int("III")
    assert result1 == 3

    result1 = roman_to_int("LVIII")
    assert result1 == 58

    result1 = roman_to_int("MCMXCIV")
    assert result1 == 1994

    result1 = roman_to_int("CCLXXXIV")
    assert result1 == 284

    result1 = roman_to_int("CMXCI")
    assert result1 == 991

# test_roman_to_int()




