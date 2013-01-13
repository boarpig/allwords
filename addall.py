#!/usr/bin/python

from words import words
import sqlite3

conn = sqlite3.connect("words.db")
c = conn.cursor()
def next_words():
    for word in words:
        yield (word,)

c.execute('''create table words (id integer primary key autoincrement, word text
        not null)''')
c.executemany("insert into words(word) values(?)", next_words())
conn.commit()
c.close()

