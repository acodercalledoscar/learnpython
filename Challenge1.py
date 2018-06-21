name = input("What is your name?: ")
age = int(input("How old are you {}?: ".format(name)))

if 18 <= age < 31:
    print("Welcome to your holiday " + name + "!!")
elif age < 18:
    print("Sorry " + name + ", please come back after {} years".format(18 - age))
else:
    print("Sorry " + name + ", holidays are only available below 31 years of age")
