#! usr/bin/env python

import re

input_file = open("regex.practice1.fasta", "r")
output_file = open("output_regex.fasta", "w")
RE1 = 0
RE2 = 0

for line in input_file:
	match_RE1 = re.match(r'>(\d+_\d:\S+)\s', line)
	#match_RE2 = re.match(r'{.*?"}', line)

	if match_RE1:
		#RE1 = match_RE1.group(1)
		NameLine= (">Homo_sapiens:"+ match_RE1.group(1)+ '\n')
		output_file.write(NameLine)

	#elif match_RE2:
		#RE2 = match_RE2.group(2)
		#re.sub("RE2", "")

	else:
		output_file.write(line)


input_file.close()
