#!/usr/bin/python

from random import choice
from words import words

left = set(((-1, -1), (-1, 0), (-1, 1)))
right = set(((1, -1), (1, 0), (1, 1)))
top = set(((-1, -1), (0, -1), (1, -1)))
bottom = set(((-1, 1), (0, 1), (1, 1)))

consonants = "BBCCDDFFGGHHHJKLLMMNNNPPQRRRSSSTTTVVWWXZ"
vowels = "AAAEEEIIIOOOUUYY"

the_grid = [[], [], [], [], [], [], []]

for x in range(7):
    for y in range(7):
        if (7 * y + x) % 2 == 0:
            the_grid[x].append(choice(vowels))
        else:
            the_grid[x].append(choice(consonants))

found = set()
def traverse(rwords, word, coord, previous):
    x = coord[0]
    y = coord[1]
    word += the_grid[x][y]
    previous.append((x, y))
    if word in rwords:
        found.add(word)
    adjacent = left | right | top | bottom
    if x == 0:
        adjacent -= left
    if x == 6:
        adjacent -= right
    if y == 0:
        adjacent -= top
    if y == 6:
        adjacent -= bottom
    temp = [x for x in rwords if x[:len(word)] == word and len(x) >= len(word)]
    if len(temp) > 0:
        for coords in adjacent:
            newcoord = (x + coords[0], y + coords[1])
            if newcoord not in previous:
                traverse(temp[:], word[:], newcoord[:], previous[:])

for x in range(7):
    for y in range(7):
        main = [word for word in words if word[0] == the_grid[x][y]]
        traverse(main[:], "", (x, y), [])

for line in the_grid:
    print(line)
print(found)
print(len(found))
