import os
import sys


#check if program is called correctly
if(len(sys.argv) < 3):
	print("USAGE : python3 sentiment_formatter.py <input-file> <output-file>")
	sys.exit()


labeled_data_path = sys.argv[1]
fin = open(labeled_data_path, 'r', errors='ignore')
output_file_path = sys.argv[2]
fout = open(output_file_path,'w')

for line in fin.readlines():
	line = line.rstrip('\n')
	words = line.split(' ')
	label = int(words[0])
	if(label >= 7):
		words[0] = 'POSITIVE'
	else:
		words[0] = 'NEGATIVE'
	newline = ' '.join(words)
	newline = newline + '\n'
	fout.write(newline)


	