#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Crossword Solver Program"""

__author__ = "Jennifer Schneider"

import re

# YOUR HELPER FUNCTION GOES HERE

def find_word(word_input, word_list):
    changed_word = word_input.replace(' ', '.')
    regexed_word = re.compile(changed_word)
    for word in word_list:
        if len(word_input) == len(word):
            if re.match(regexed_word, word):
                print(word)

def main():
    words = []
    with open('dictionary.txt') as f:
        words = f.read().split()

    test_word = input(
        'Please enter a word to solve.\nUse spaces to signify unknown letters: ').lower()

    
    # raise NotImplementedError('Please complete this')
    find_word(test_word, words)

if __name__ == '__main__':
    main()
