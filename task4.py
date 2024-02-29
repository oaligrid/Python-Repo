#Personal Property of Owais Ali
# Given an input string, count occurrences of all characters within a string (e.g. pythonnohtyppy -> p:3, y:3, t:2, h:2, o:2, n:2).
from collections import defaultdict


def count_characters(s):
    char_count = defaultdict(int)
    for char in s:
        char_count[char] += 1
    return char_count

if __name__ == "__main__":
    s = input("Enter a string: ")
    char_count = count_characters(s)
    for char, count in char_count.items():
        print(f"{char}:{count}", end="")
        if char != list(char_count.keys())[-1]:
            print(", ", end="")
    print()

