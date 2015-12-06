import random
import sys

#check if program is called correctly
if(len(sys.argv) < 3):
	print("USAGE : python3 splitter.py <input-file> <training-percentage>")
	sys.exit()

outfilename1 = "data_development.txt"
outfilename2 = "data_training.txt"
inputfile = sys.argv[1]
training_percentage = int(sys.argv[2])

with open(inputfile,'r') as f:
    lines = f.readlines()

random.shuffle(lines)
numlines = int(len(lines)*(1 - training_percentage/100))

with open(outfilename1, 'w') as f:
    f.writelines(lines[:numlines])

with open(outfilename2, 'w') as f:
    f.writelines(lines[numlines:])