# 1. Write a program that generate 26 text files named A.txt, B.txt, and so on up to Z.txt.
#     2. To each file append a random number between 1 and 100.
#     3. Create a summary file (summary.txt) that contains name of the file and number in that file:

#         A.txt: 67

#         B.txt: 12

#         ...

#         Z.txt: 98
from random import randint as rd
def create_alphabet_files_func1():
    # print(ord('A'), ord('Z'))
    for i in range(ord('A'), ord('Z') + 1):
        num = rd(1, 100)
        with open(chr(i) + '.txt', 'w') as opened_file:
            opened_file.write(str(num))

    for i in range(ord('A'), ord('Z') + 1):
        with open(chr(i) + '.txt', "r") as file_for_read, open('summary.txt', 'a') as file_for_write:
            data = file_for_read.read()
            file_for_write.write(chr(i) + '.txt :' + str(data) + '\n')
create_alphabet_files_func1()

# Create file with some content. As example you can take this one
#     Тому що ніколи тебе не вирвеш,
#     ніколи не забереш,
#     тому що вся твоя свобода
#     складається з меж,
#     тому що в тебе немає
#     жодного вантажу,
#     тому що ти ніколи не слухаєш,
#     оскільки знаєш і так,
#     що я скажу,
# Create second file and copy content of the first file to the second file in upper case

data0 = '''
    Тому що ніколи тебе не вирвеш, 
    ніколи не забереш, 
    тому що вся твоя свобода 
    складається з меж, 
    тому що в тебе немає 
    жодного вантажу, 
    тому що ти ніколи не слухаєш, 
    оскільки знаєш і так, 
    що я скажу, 
'''
def copy_upper_file_func(data_):
    with open('some_content.txt', mode='w', encoding='UTF-8') as file:
        file.write(data_)

    with open('copy_content.txt', mode="w", encoding="UTF-8") as second, open('some_content.txt', 'r', encoding='UTF-8') as first:
        some_data = first.read()
        second.write(some_data.upper())



# Write a program that will simulate user score in a game. Create a list with 5 player's names.
# After that simulate 100 games for each player. As a result of the game create a list with player's name and his score (0-1000 range). 
# And save it to a CSV file. 


import csv
def first_var():

    data = [('Josh', 'Luke', 'Kate', 'Mark', 'Mary'), ]

    for i in range(100):
        result = [rd(0, 1000) for j in range(5)]
        data.append(result)


    with open("the_game.csv", mode="w") as game:
        writer = csv.writer(game)
        for row in data:
            writer.writerow(row)


    summary = []
    with open('score.csv', mode="w") as score, open('the_game.csv', mode="r") as game:
        reader = csv.reader(game)
        reader0 = [i for i in reader if bool(i) is not False]
        for num in range(5): 
            sum = 0
            for row in range(len(list(reader0[1:100]))):
                sum += int(reader0[1:100][row][num])
            summary.append(sum/100)
        data.append(summary)
        writer = csv.writer(score)
        for row in data:
            writer.writerow(row)


def second_var():

    data = [('Josh', 'Luke', 'Kate', 'Mark', 'Mary'), ]
    summary = []

    for i in range(100):
        result = [rd(0, 100) for j in range(5)]
        data.append(result)

    with open('the_game_2.csv', mode="w") as game:
        writer = csv.writer(game)
        for row in data:
            writer.writerow(row) 
    
    with open('the_game_2.csv', mode="r") as game, open('score_2.csv', mode="w") as score:
        reader = csv.reader(game)
        reader0 = [i for i in reader if bool(i) is not False]
        for num in range(5):
            sum = 0
            for row in range(len(reader0[1:100])):
                sum += int(reader0[1:100][row][num])
            summary.append(sum)
        data = [('Josh', 'Luke', 'Kate', 'Mark', 'Mary'), ]  
        data.append(summary) 
        writer = csv.writer(score)
        for row in data:
            writer.writerow(row)


# Write a script that reads the data from previous CSV file and creates a new file called high_scores.csv
# where each row contains the player name and their highest score. 
# Final score should sorted by descending of highest score

# The output CSV file should look like this:

# Player name, Highest score
# Kate, 907
# Mary, 897
# Luke, 784
# Mark, 725
# Josh, 345

# with open("the_game.csv", mode="r") as game, open("high_scores.csv", mode="w", newline='') as high:
#     reader = csv.reader(game)
#     reader0 = [i for i in reader if bool(i) != False]
#     result = []
#     for num in range(5):
#             list_ = []
#             for row in range(len(reader0[1:100])):
#                 list_.append(int(reader0[1:100][row][num]))
#             result.append(max(list_))
#     player_list = ('Josh', 'Luke', 'Kate', 'Mark', 'Mary')
#     headers = ("Player name", "Highest score")
#     writer = csv.DictWriter(high, fieldnames=headers)
#     writer.writeheader()
#     for i in range(5):
#         writer.writerow({"Player name" : player_list[i], "Highest score" : result[i]})





# print('Привіт, світ!'.encode())

# file = open("hello.txt", mode="w")
# file.write('Hello, world!')
# file.write('Abracadabra')

# file.write('Ololo')


