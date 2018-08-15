import random


def goal_word(min_length=5, filename="poop.txt"):
    with open(filename) as wordbook:
        words = (line.rstrip('\n') for line in wordbook)
        

print(goal_word(7))
