#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Crossword Solver Program"""

__author__ = "Jennifer Schneider"

import re

# YOUR HELPER FUNCTION GOES HERE


def crossword_solver(word_input, list):
    changed_word = word_input.replace(' ', '.')
    crossword_words = re.compile(changed_word)
    for word in list:
        if len(word_input) == len(word):
            if re.match(crossword_words, word):
                print(word)


def main():
    crosswords = []
    with open('dictionary.txt') as f:
        crosswords = f.read().split()

    word_to_test = input(
        'Please enter a word to solve.\nUse spaces'
        'to signify unknown letters: ').lower()
# random comment
# # raise NotImplementedError('Please complete this')
    crossword_solver(word_to_test, crosswords)


if __name__ == '__main__':
    main()
