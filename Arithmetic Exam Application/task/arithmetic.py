# write your code here
import random


class player:
    def __init__(self):
        self.correct = 0

def calculate(first, operator, second):
    if operator == "+":
        return first + second
    elif operator == "*":
        return first * second
    elif operator == "-":
        return first - second

description = ""
def randomtaskone():
    randnum_one = random.randint(2, 9)
    randnum_two = random.randint(2, 9)
    operator = ["+", "-", "*"]
    randop = operator[random.randint(0, 2)]
    print("{} {} {}".format(randnum_one, randop, randnum_two))
    return calculate(randnum_one, randop, randnum_two)
def randomtasktwo():
    randnum = random.randint(11, 29)
    print(randnum)
    return randnum * randnum
def inputchecker():
    while True:
        try:
            user = int(input())
            return user
        except ValueError:
            print("Incorrect format.")

def levelchecker():
    while True:
        try:
            print("Which level do you want? Enter a number:")
            print("1 - simple operations with numbers 2-9")
            print("2 - integral squares of 11-29")
            user = int(input())
            if user <= 2 and user >= 1:
                return user
                break
            else:
                print("Incorrect format.")
        except ValueError:
            print("Incorrect format.")

def game(level):
    if level == 1:
        for i in range(0,5):
            task = randomtaskone()
            use = inputchecker()
            if task == use:
                playerOne.correct += 1
                print("Right!")
            else:
                print("Wrong!")
    elif level == 2:
        for i in range(0,5):
            task = randomtasktwo()
            use = inputchecker()
            if task == use:
                playerOne.correct += 1
                print("Right!")
            else:
                print("Wrong!")
playerOne = player()
level = levelchecker()
if level == 1:
    description = "integral squares 11-29"
else:
    description = "simple operations with numbers 2-9"

game(level)
print("Your mark is {}/5. Would you like to save the result? Enter yes or no.".format(playerOne.correct))
save = input().lower()[0]
if save == "y":
    print("What is your name?")
    name = input()
    print('''The results are saved in "results.txt"''')
    file = open("results.txt", 'a', encoding='utf-8')
    file.write("{}: {}/5 in level {} ({})".format(name,playerOne.correct,level,description))
    file.close()