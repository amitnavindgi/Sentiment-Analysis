import os
import sys


#check if program is called correctly
if(len(sys.argv) < 3):
	print("USAGE : python3 senti_formatter_svm.py <input-file> <output-file>")
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
		fout.write('+1')
	else:
		fout.write('-1')

	for pair in words[1:]:
		tokens = pair.split(":")
		fout.write(' ' + str((int(tokens[0]) + 1)) + ':' + str(tokens[1]))    
	fout.write('\n')


	
