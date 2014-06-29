#!/usr/bin/python

# this is a simple script to extract all variable names from one or more
# python source files and split the variable names into chunks (e.g.,
# camelcase). It is designed to be used to analyze a bunch of your
# source code so you can add words you tend to use frequently when
# programming to dragon.

import ast as parser
import re
import sys

names = set()

for filename in sys.argv[1:]:
    print >> sys.stderr, 'Processing ', filename
    tree = parser.parse(open(filename).read())
    for node in parser.walk(tree):
        if isinstance(node, parser.Name):
            names.add(node.id)

    parts = set()
    for name in names:
        for under_word in name.split('_'):
            if not under_word:
                continue
            under_word = under_word[0].lower() + under_word[1:]
            capitals = re.findall('[A-Z]', under_word)
            for letter in capitals:
                first, under_word = under_word.split(letter, 1)
                parts.add(first.lower())
                under_word = letter + under_word
            parts.add(under_word.lower())

parts = list(parts)
parts.sort()
parts.sort(key=lambda value: len(value))
for part in parts:
    print part
