from random import randint

#
# lst = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#
# with open("colours.txt", "w") as colours:
#     for i in lst:
#         colours.write(i + '\n')
#
#
#
# def upercase(file):
#     count = 0
#     with open(file, 'r') as color:
#         for line in color:
#             words = line.split()
#             for word in words:
#                 if word.isupper():
#                     count += 1
#     return count
#
# file = 'colours.txt'
# x = upercase(file)
# print(x)
#
#
import csv

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# email = input("Enter your email: ")

# lst = [{'name': input("Enter your name: "), 'age': int(input("Enter your age: ")), 'email': input("Enter your email: ") }]
#
# with open('test.csv', 'w') as file:
#     writer = csv.DictWriter(file, fieldnames=["name", "age", "email"] )
#     writer.writeheader()
#     writer.writerows(lst)

# ამ კოდის მიხედვით input ების საშუალებით შექმენით csv ფაილი
# with open('data.csv', "w") as file:
# writer = csv.DictWriter(file, fieldnames=["name", "age", "email"])
# writer.writeheader()
# writer.writerows(data)

#
# with open('test.txt', 'w') as file:
#     for i in range(20):
#         if i



lines = [1, 5, 9]
line_words = ['one', 'five', 'nine']


with open("test.txt", "w") as file:
    for i in range(1, 11):
        if i in lines:
            index = lines.index(i)
            file.write(line_words[index] + "\n")
        else:
            file.write("\n")


