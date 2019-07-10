# ----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------Copy and Paste Comment Bars From Here----------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# --------------------------------Multiplication code in 6 lines--------------------------------------------------------

# numbers_to_multiply = [2,4,6,8]
#
# def multiplier_by_two (number1):
#     result = number1*2
#     print(result)
#
# for i in numbers_to_multiply:
#     multiplier_by_two(i)

# ----------------------------------Use list comprehension to create a list of the results in 2 lines-------------------

# same_as_above = [i * 2 for i in range(1, 9) if i % 2 == 0]
#
# print(f'The results are {", ".join(str(i) for i in same_as_above)}')

# ------------------------------------------------F string play---------------------------------------------------------
#
# name = input('What is your name? ')
#
# age = input('How old are you? ')
#
# print(f'Hi {name}! You are {100 - int(age)} years away from being 100!')

# -----------------------------------------------Map and lists and such-------------------------------------------------

# myList = [1, 3, 5, 7, 9]
#
# print(f'My list is {len(myList)} item(s) long')
# print(myList)

# ---------------------------------------------Trying to use OOP--------------------------------------------------------


class Human:

    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def introduction(self, language):
        if language in ["English", "english", "e", "eng", "ENG", "American", "american"]:
            return print(f"Hi! My name is {self.name}, I am {self.age} years old and I am from {self.country}")
        elif language in ["Japanese", "japanese", "jp", "JP"]:
            return print(f"はじめまして！{self.name}と申します。{self.age}歳です。{self.country}から来ました。宜しくお願いします！")


seth = Human("Seth", 29, "Japan")

loser = Human("Loser", 30, "Britain")

loser.introduction("JP")
seth.introduction("ENG")
