import os
import sys

#check if program is called correctly
if(len(sys.argv) < 3):
	print("USAGE : python3 email_formatter.py <input-dir> <output-file>")
	sys.exit()


trainingdatapath = sys.argv[1]
outputfilepath = sys.argv[2]
output = open(outputfilepath, 'w')

vocabfilepath = 'enron.vocab'
vocab = {}
word_count = {}

#prepare a dictionary using email.vocab
with open(vocabfilepath, "r", encoding="latin1") as file:
	id = 0
	for word in file:
		id = id + 1
		vocab[word.rstrip()] = id
#print(vocab)


for root, directories, filenames in os.walk(trainingdatapath):
	for filename in sorted(filenames): 
		#print(os.path.join(root,filename))
		if("spam" in filename):
			output.write('+1')
		elif("ham" in filename):
			output.write('-1')
		
		filepath = os.path.join(root, filename)
		with open(filepath, "r", encoding="latin1") as file:
			dictionary = {}
			for line in file:
				line = line.split()
				for word in line:
					word_id = vocab[word]
					dictionary[word_id] = dictionary.setdefault(word_id, 0) + 1
			
			for id in sorted(dictionary):
				output.write(' ' + str(id) + ':' + str(dictionary[id]))
			
			output.write('\n')