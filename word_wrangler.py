"""
Student code for Word Wrangler game
"""

import urllib.request as urllib2
import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but with no duplicates.

    This function can be iterative.
    """
    list2 = list(list1)
    for word in list2:
        num = list2.count(word)
        if num > 1:
            for dummy in range(num - 1):
                list1.remove(word)
    return list1


def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    inter_sect = []
    if list1[0] < list2[0]:
        for word in list2:
            if word in list1:
                inter_sect.append(word)
    return inter_sect


# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing those elements that are in
    either list1 or list2.

    This function can be iterative.
    """
    result = []
    idx_i = 0
    idx_j = 0
    while idx_i < len(list1) and idx_j < len(list2):
        if list1[idx_i] <= list2[idx_j]:
            result.append(list1[idx_i])
            idx_i += 1
        else:
            result.append(list2[idx_j])
            idx_j += 1
    if idx_i == len(list1):
        result.extend(list2[idx_j:])

    elif idx_j == len(list2):
        result.extend(list1[idx_i:])
        
    return result


def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """

    if list1 == []:
        return []
    elif len(list1) == 1:
        return list1
    elif len(list1) == 2:
        if list1[0] <= list1[-1]:
            return [list1[0], list1[-1]]
        else:
            return [list1[-1], list1[0]]
    result =[]
    num = len(list1)
    mid = int(num/2.)
    l_list1 = list1[:mid]
    r_list1 = list1[mid:]
    l_sort = merge_sort(l_list1)
    r_sort = merge_sort(r_list1)
    result = merge(l_sort, r_sort)
    return result


# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    if word == "":
        return [""]
    elif len(word) == 1:
        return ["", word]
    elif len(word) == 2:
        return ["", word[0], word[1], word[0] + word[1], word[1] + word[0] ]
    else:
        result = []
        for str in gen_all_strings(word[1:]):
            if str == "":
                result.append(word[0])
            else:
                new_str3 = str + word[0]
                result.append(new_str3)
            if len(str) >= 1:
                for idx in range(len(str)):
                    new_str2 = str[:idx] + word[0] + str[idx:]
                    result.append(new_str2)
        result.extend(gen_all_strings(word[1:]))
        print(len(result))
        return result


# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    url = codeskulptor.file2url(filename)
    net_file = urllib2.urlopen(url)
    return net_file.readlines()



def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates,
                                     intersect, merge_sort,
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
# run()
