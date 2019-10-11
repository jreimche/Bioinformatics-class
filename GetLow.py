#! /usr/bin/env python3
"""
this code will a sentence from user input, turn it all to lowercase letters and remove the spaces and count the length
"""

sentence = input("Enter a sentence here ")
sentence = sentence.lower().replace(" ", "")

SenLength = len(sentence)

print ("The sentence is %d long" % SenLength)


