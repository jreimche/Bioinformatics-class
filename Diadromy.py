#! usr/bin/env python

"""
script goes through the Bloom_etal_2018_Reduced_Dataset
It prints out species and diadromy status
It prints out the total log body size for all individuals
"""

#set the dataset as InFileName variable
InFileName = 'Bloom_etal_2018_Reduced_Dataset.csv'

#open the file for reading
InFile = open(InFileName, 'r')

#create a LineNumber variable
LineNumber = 0
TotalBodySize = 0.0
#print(LineNumber)
#print(TotalBodySize)

#create loop that prints out species and diamdromy status
for Line in InFile:
	#if else statement- if the linenumber is 0 then it is the header and we want to print speices and diadromy, if linenumber is not zero then it has meaninfgul data, create an element list separated by commas (csv) and print the info in the 0 and 3 element positions
	if LineNumber == 0:
		print("Species, Diadromy")
	else:
		Line = Line.strip('\n')
		ElementList = Line.split(',')
		OutPutString = "%s, %s" %(ElementList[0], ElementList[3])
		print(OutPutString)
		TotalBodySize = TotalBodySize + float(ElementList[1])
	LineNumber = LineNumber + 1

#print TotalBodySize
print(TotalBodySize)

#close file
InFile.close() 
