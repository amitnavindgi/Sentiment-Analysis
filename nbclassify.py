import os
import sys
import json
import math

#check if program is called correctly
if(len(sys.argv) < 4):
	print("USAGE : python3 nblearn.py <model-file> <test-file> <mode>")
	sys.exit()

#read file paths
modelfilepath = sys.argv[1]
testfilepath = sys.argv[2]
mode = sys.argv[3]
#load model file into a dictionary
model = json.load(open(modelfilepath))

#read data from model
prob_each_class = model['prob_each_class']
each_class_all_words_count = model['each_class_all_words_count']
total_words_in_class = model['total_words_in_class'] 
total_docs = model['total_docs']
vocab_size = model['vocab_size']

with open(testfilepath, 'r') as f:
	for lines in f:
		#print(repr(line))
		max_prob = -float("inf")
		for label in each_class_all_words_count:
			class_prob = math.log(prob_each_class[label])

			line = lines.rstrip('\n').split(' ')
			if(mode == 'training'):
				label_found = line[0]
				line = line[1:]
			for pair in line:
				tokens = pair.split(':')
				word_id = tokens[0]
				word_count = each_class_all_words_count[label].get(word_id, 0)
				class_prob = class_prob + math.log((word_count + 1)/(total_words_in_class[label] + vocab_size))
			if(class_prob > max_prob):
				max_prob = class_prob
				final_label = label
		print(final_label)

		# positive_prob = 0
		# negative_prob = 0
		# line = line.rstrip('\n').split(' ')
		# for tokens in line[1:]:
		# 	tokens = tokens.split(':')
		# 	if(tokens[0] in prob_word):
		# 		positive_prob = positive_prob + math.log(prob_word[tokens[0]]['1'])
		# 	else:
		# 		positive_prob = positive_prob + math.log(1/total_words_class['1'])

		# 	if(tokens[0] in prob_word):
		# 		negative_prob = negative_prob + math.log(prob_word[tokens[0]]['0'])
		# 	else:
		# 		negative_prob =negative_prob + math.log(1/total_words_class['0'])

		# positive_prob = positive_prob + math.log(prob_class['1'])
		# negative_prob = negative_prob + math.log(prob_class['0'])
		# if(positive_prob >= negative_prob)
		# 	print(model_data['1'])
		# else
		# 	print(model_data['0'])





