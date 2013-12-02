#!/usr/bin/python

from random import choice
from words import words

left = set(((-1, -1), (-1, 0), (-1, 1)))
right = set(((1, -1), (1, 0), (1, 1)))
top = set(((-1, -1), (0, -1), (1, -1)))
bottom = set(((-1, 1), (0, 1), (1, 1)))

consonants = "BBCCDDFFGGHHHJKLLMMNNNPPQRRRSSSTTTVVWWXZ"
vowels = "AAAEEEIIIOOOUUYY"

the_grid = []

side = 7

for x in range(side):
    the_grid.append([])
    for y in range(side):
        if (side * y + x) % 2 == 0:
            the_grid[x].append(choice(vowels))
        else:
            the_grid[x].append(choice(consonants))

found = set()
def traverse(rwords, word, coord, previous):
    x = coord[0]
    y = coord[1]
    word += the_grid[x][y]
    previous.append((x, y))
    wordlen = len(word)
    temp = [n for n in rwords if n[:wordlen] == word and len(n) >= wordlen]
    if word in temp:
        found.add(word)
    adjacent = left | right | top | bottom
    if x == 0:
        adjacent -= left
    if x == side - 1:
        adjacent -= right
    if y == 0:
        adjacent -= top
    if y == side - 1:
        adjacent -= bottom
    if len(temp) > 0:
        for coords in adjacent:
            newcoord = (x + coords[0], y + coords[1])
            if newcoord not in previous:
                traverse(temp, word[:], newcoord[:], previous[:])

for x in range(side):
    for y in range(side):
        main = [word for word in words if word[0] == the_grid[x][y]]
        traverse(main[:], "", (x, y), [])

for line in the_grid:
    print(line)
print(found)
print(len(found))
