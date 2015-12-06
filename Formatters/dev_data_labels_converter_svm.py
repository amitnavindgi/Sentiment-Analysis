import sys

#check if program is called correctly
if(len(sys.argv) < 3):
	print("USAGE : python3 dev_data_labels_converter.py <development_file> <output-file>")
	sys.exit()


devdatapath = sys.argv[1]
fin = open(devdatapath, 'r', errors='ignore')
output_file_path = sys.argv[2]
fout = open(output_file_path,'w')

for line in fin.readlines():
	line = line.rstrip('\n')
	words = line.split(' ')
	label = int(words[0])
	if(label > 0):
		words[0] = 'HAM'
	else:
		words[0] = 'SPAM'
    
	newline = ' '.join(words)
	newline = newline + '\n'
	fout.write(newline)