#! usr/bin/env python

import re

Usage = """
regex.practice3.py -- version 1.0
clean up regexpractice1.fasta file
remove odd identifier and replace with 'Homo sapiens'
remove protein information and spaces
Thank you for trying.
Usage: regex.practice1.fasta > output_regex.fasta
"""

#sets input and output files
input_file = open("regex.practice1.fasta", "r")
output_file = open("output_regex.fasta", "w")

#creates counter variable RE=regular expression
RE1 = 0

#for loop that goes through the input file line by line
for line in input_file:
	match_RE1 = re.match(r'>(\d+_\d:\S+)\s', line) #match the RE1 regular expression

	if match_RE1:
		NameLine= (">Homo_sapiens:"+ match_RE1.group(1)+ '\n') #if there is a match create a new variable with the following parameters 
		output_file.write(NameLine) #write the new line to the output file (.write can only have 1 parameter) 

	else:
		output_file.write(line) #if the line does not match, print it to the output file


input_file.close() #close file 
