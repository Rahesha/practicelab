print("Variable and Assignment Exercises.")   #Variable and Assignment
integer = 56
flo = 3.45
boolean = True
integer += 4
integer = 60

print("Comments and Math Operators")
integer2 = 4 + 6
integer3 = 10 - 5
integer4 = 15 / 3
integer5 = 2 * 3
integer6 = 3 ** 8
integer7 = 10 // 3
integer8 = 17 % 3

print("print exercise")
boolean2 = False
print(boolean2)
print("read the book.")
print(4 + 9)
print(3.14)
print(4 * 6)

def func_grocery():
    print("Grocery Store Purchase")
    penne = 16.68
    arrabiata = 6.98
    garlic_cloves = 16.78
    italian_seasoning = 15.26
    baguettes = 3.00
    meatballs = 4.39
    total = (penne + arrabiata + garlic_cloves + italian_seasoning + baguettes + meatballs) * 100 / 100
    total1 = round((penne + arrabiata + garlic_cloves + italian_seasoning + baguettes + meatballs), 2)
    print(total)
    print(total1)


func_grocery()

print("string exercise")
string = "Just do it!"
print(string[10])
print(string[5:7])
print(string[8:])
print(string[:5])
concatenate = "Don't " + string[5:]
print(concatenate)

float2 = 4.56
print(type(float2))
print(str(float2) + " is a string.")
print("\"Hello, I\'m Rahesha, it\'s nice to meet you.\"")


print("*******\n *****\n  ***\n   *")
def func_1():
    user = int(input("Enter an integer."))
    print((user) + 10)
    user1 = input("Enter an integer.")
    print(int(user1) + 10)

def hello_world_printer():
    print("Hello World")


hello_world_printer()


def name_printer(user_input):  # using one parameter as argument
    print(user_input)

  #variable assigned to give as a value to parameter
    #value of parameter given as variable


def func_multiple_para(p1, p2, p3):
    print(p1, p2, p3)



func_multiple_para("The string" , str(2.3) , " is converted to an integer.")

def func_default(def1 = 3, def2 = 6):
    print(def1 * def2)


func_default(5, 2)

def func_volume():
    lenght = int(input("Enter the length of prism"))
    width = int(input("Enter the width."))
    height = int(input("Enter the height."))
    volume = lenght * width * height
    print("The volume of the prism is " + str(volume) + " cubic feet.")





def func_volume(len, wid, ht):
    volume = len * wid * ht
    print("The volume of the prism is " + str(volume) + " cubic feet.")







from random import randint

fuel = randint(10, 25)
miles = randint(200, 400)
print("The car can travel " + str(miles // fuel) + " miles per gallon.")


def score():
    if grade >= 90:
        print("your score is A " + "and grade is " + str(grade))
    else:
        if grade >= 80:
            print("your score is B.")
        else:
            if grade >= 70:
                print("your score is C.")
            else:
                if grade >= 60:
                    print("Your score is D.")
                else:
                    print("Your score is F.")



from random import randint
numbers = randint(1, 10)
def roman():
    if numbers == 1:
        print("the Roman Equivalent is I.")
    elif numbers == 2:
        print("the roman equivalent is II.")
    elif numbers == 3:
        print("The roman equivalent is III.")
    elif numbers == 4:
        print("The roman equivalent is IV.")
    elif numbers == 5:
        print("The roman equivalent is V.")
    elif numbers == 6:
        print("The roman equivalent is VI.")
    elif numbers == 7:
        print("The roman equivalent is VII.")
    elif numbers == 8:
        print("The roman equivalent is VIII.")
    elif numbers == 9:
        print("The roman equivalent is IX.")
    else:
        print("The roman equivalent of" + str(numbers) + " is X.")





count = 10
while count != 0:
    print(count)
    count -= 1







count = 0
for char in words1:
    count += 1

print(words1)
print(count)



number = 1
while number <= 50:

    if number % 3 == 0 and number % 5 == 0:
        print("Fizzbuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
    number += 1


for number in range(1, 51):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz") if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)




def factor(integer_fac):
    fact = 1
    for item in range(integer_fac, 1, -1):    #3 2 1
        fact *= item                     #3  6  6
    return fact

print(factor(3))
print(factor(4))
print(factor(5))
def convert(radian):
    degrees = radian * 100 * (1800 / 3.14) * 100
    return round(degrees, 2)


print(convert(8))

mixed_case = "A Song of Ice and Fire"
print(mixed_case.isupper())





mixed_case = "A Song of Ice and Fire"
print(mixed_case.isupper())
print(mixed_case.islower())
upper_case = mixed_case.upper()
print(upper_case)
lower_case = mixed_case.lower
print(lower_case)
print(mixed_case.istitle())
title_case = mixed_case.title()
print(title_case)
print(mixed_case.startswith("A"))
print(mixed_case.endswith("e"))
words = mixed_case.split()
print(words)
join = "".join(words)
print(join.isalpha())
print(join.isalnum())
print("123".isalnum())
print("4.56".isdecimal())   #false
print(" ".isspace())

the_string = "North Dakota"
print(the_string.rjust(17))
print(the_string.ljust(17, "*"))
center_plus = the_string.center(16, "+")
print(center_plus)
print(the_string.lstrip("htroN"))
print(center_plus.strip("+"))
print(center_plus.replace("North", "South"))

#string reverser




str_1 = "James Bond is 007."
def word_counter(words):
    spaces_letters = ""
    word_count = 1
    for i in words:
        if i.isalnum() or i.isspace() or i == "-" or i == "'":
            spaces_letters += i
    for j in spaces_letters:
        if j == " ":
            word_count += 1
    return word_count



multiple_datatypes = [23, 1.23, True, "numbers", [1, 2, 3]]
list_func = list("AEIOU")
print("E" in list_func)
print("a" not in list_func)


number_integer = [[0, 2], [4, 6], [8, 10], [12, 14]]
print(number_integer[0])
print(number_integer[3][1])
string_list = ["chair", "table", "desk", "lamp", "bed"]
print(string_list[-5])
print("Most people own at least {} {}s.".format(str(number_integer[0][1]), string_list[-5])) #using .format()
print("Most people own at least " + str(number_integer[0][1]) + " " + string_list[-5] + "s.") #using concatenation
float_var = [0.98, 8.76, 6.54, 4.32]
print(float_var[1:4])
print(float_var[1:3])
print(float_var[:2])
#using format
name = "Rahesha"
degree = " Coding"
job = "Architect"
experience = "one year"
print("{} majored in {}, works as an {}, and has {} years of experience.".format(name, degree, job, experience))

example = [6, 5, 4, 3, 2, 1]
example[1:4] = [3, 4, 5]
print(example)
example[4:7] = [7, 6, 5]
print(example)

arctic_animals = ["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]
del arctic_animals[4]
print(arctic_animals)
arctic_animals.remove("elephant")
arctic_animals.append("arctic fox")
arctic_animals.insert(2, "snowy owl")
arctic_animals.sort()
print(arctic_animals)
print(arctic_animals.index("reindeer"))
print(arctic_animals.pop())


import copy
ex_11 = [1, 2, 2, 3, 4]
ex_12 = copy.deepcopy(ex_11)
ex_12[3] = 4
print(ex_11)
print(ex_12)

ex_13 = ["apple",
         "Banana",
         "Pineapple",
         "Orange"]
print(ex_13)

ex_14 = 2 + 4 + 1
ex_15 = 2 + \
        4 + \
        1
print(ex_14)
print(ex_15)
print("hello " + \
      "World")

movies = {"disney": "Frozen", "paramount": "Forrest Gump", "Universal Studios": "Jurassic World", "Warner Bros": "Barbie", "Dream works": "Shrek"}
print(movies["Universal Studios"])
print("disney" in movies)
print("Warner Bros" not in movies)

list = [1, 2, 3]
dict = {1, 2, 3}
print(list == [3, 2, 1])
print(dict == {3, 2, 1})

songs = {"Queen": "Bohemian Rhapsody", "Bee Gees": "Stayin' Alive", "U2": "One", "Michael Jackson": "Billie Jean", "The Beatles": "Hey Jude", "Bob Dylan": "Like A Rolling Stone"}
songs_line = {"Queen": "Bohemian Rhapsody",
              "Bee Gees": "Stayin' Alive",
              "U2": "One",
              "Michael Jackson": "Billie Jean",
              "The Beatles": "Hey Jude",
              "Bob Dylan": "Like A Rolling Stone"}
print(len(songs_line))

print(songs_line.keys())

for key in songs_line.keys():
    print(key)

print(songs_line.values())

for value in songs_line.values():
    print(value)

for key, value in songs.items():
    print(key, value)

print(songs.items())

print(songs.get("Promise of the Real", "This key is not present in the dictionary."))

if "Promise of the Real" in songs:
    print("Promise of the Real")
else:
    print("Not in the dictionary.")

ex_1 = {}.fromkeys([1, 2, 3, 1], False)
print(ex_1)

ex_4 = {}.fromkeys("data")
print(ex_4)


just_consonant = {}.fromkeys("abcdefghijklmnopqrstuvwxyz", "consonant")

for key, value in just_consonant.items():
     if key != "a" and key != "e" and key != "i" and key != "o" and key != "u":
        print(key, value)


celebs = {"Katty Perry": "singer", "J.K.Rolling": "writer", "Barack Obama": "Politician"}
player = {"Messi": "Soccer"}
print(celebs)


copied = celebs.copy()
copied["Katty Perry"] = "writer"
print(celebs)

celebs.clear()
print(celebs)
print(copied)


internet_celebrities = {"DrDisrespect": "YouTube", "ZLaner": "Facebook", "Ninja": "Mixer"}
another_one = {"shroud": "Twitch"}

internet_celebrities.update(another_one)
copied = internet_celebrities.copy()
print(internet_celebrities)

print(copied)

print(type(internet_celebrities))


my_dict = {'a': 1, 'b': 2, 'c': 3}
keys_list = list(my_dict.keys())
print(keys_list)














