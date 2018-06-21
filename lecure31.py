# age = int(input("How old are you?: "))
#
# # if (age >= 16) and (age <= 65):
# # if 16 <= age <= 65:
# # if 15 < age < 66:
# #     print("Have a good day at work")
#
# if (age < 16) or (age > 65):
#     print("Enjoy your free time")
# else:
#     print("Have a good day at work")
#
# x = "False"
# if x:
#     print("x is true")

# x = input("Please enter some text: ")
#
# if x:
#     print("You inputted {}".format(x))
# else:
#     print("you did not enter anything")

# print(not True)
# print(not False)

# age = int(input("Please enter your age: "))
#
# if not (age < 18):
#     print("Please put an X in the box")
# else:
#     print("Please come back in {} years".format(18 - age))


parrot = "Norwegian Blue"

letter = input("Give me a letter: ")

vowel = "aeiou"

if letter in parrot:
    if letter not in vowel:
        print("Give me a {}, Bob".format(letter))
    else:
        print("Give me an {}, Bob".format(letter))
else:
    print("I don't need that letter")