#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def words_count():
    file_name = input("Enter the name of the file:")
    f = open(file_name, 'r')
    word_list = f.read().split()
    f.close()
    occurs_dict = {}
    for word in word_list:
        occurs_dict[word] = occurs_dict.get(word,0) + 1
    print("File %s has %d words (%d are unique)" \
            % (file_name, len(word_list), len(occurs_dict)))
    print(occurs_dict)

if __name__ == '__main__':
    words_count()
else:
    print(__name__)

