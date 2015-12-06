import os
import sys
import json

#check if program is called correctly
if(len(sys.argv) < 3):
	print("USAGE : python3 nblearn.py <training-file> <model-file>")
	sys.exit()

#get training file and model file form their paths
trainingfilepath = sys.argv[1]
trainingfile = open(trainingfilepath, 'r', errors='ignore')
modelfilepath = sys.argv[2]
#modelfile = open(modelfilepath, 'w')

#initiaze data structures for use
count_class = {} #total docs belonging to each class C
total_docs = 0 #total documents
total_words_in_class = {} #total words in each class C
each_class_all_words_count = {}  #total count of word w in all classes
vocab = set() #to store unique words for use in add-one smoothing

prob_each_class = {} #P(c) probabililty of each class
#prob_each_word = {} #P(wi, ck)

#start processing training file document by document
for line in trainingfile.readlines():
	#take each document line by line
	line = line.rstrip('\n')
	features = line.split(' ')
	#get the label or the class
	label = features[0]
	#total documents for each class
	count_class[label] = count_class.setdefault(label, 0) + 1
	#total documents
	total_docs = total_docs + 1
	#initialize dictionary with each label as key and dict of all words and their counts
	word_id_class_count = each_class_all_words_count.setdefault(label, {})
	#process content of each document
	for pair in features[1:]:
		#get each token of the form x:y
		token = pair.split(':')
		word_id = int(token[0])
		word_count = int(token[1])
		#add word to the vocab
		vocab.add(word_id)
		#first find the word and then increment the class it belongs to
		total_words_in_class[label] = total_words_in_class.setdefault(label, 0) + word_count
		#for each word increment its class value
		word_id_class_count[word_id] = word_id_class_count.setdefault(word_id, 0) + word_count

#calculate probability of each class P(c)
for label in count_class:
	prob_each_class[label] = count_class[label]/total_docs

#calculate probability of each word
# for word_id in each_word_each_class_count:
# 	id_labels = each_word_each_class_count[word_id]
# 	word_id_class_count = prob_each_word.setdefault(word_id, {})
# 	for label in id_labels:
# 		word_count_label = id_labels[label]
# 		prob = word_count_label/total_words_in_class[label]
# 		word_id_class_count[label] = prob




#create dictionary to store in model file for access in classifier
model = {}
model['total_docs'] = total_docs
model['prob_each_class'] = prob_each_class
model['vocab_size'] = len(vocab)
model['each_class_all_words_count'] = each_class_all_words_count
model['total_words_in_class'] = total_words_in_class
#model['prob_each_word'] = prob_each_word

print(each_class_all_words_count)

#store calculated values in model file
with open(modelfilepath, 'w') as modelfile:
	json.dump(model, modelfile)
