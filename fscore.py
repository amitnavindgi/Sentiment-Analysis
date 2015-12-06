import os
import sys
import math

#check if program is called correctly
if(len(sys.argv) < 3):
	print("USAGE : python3 stats.py <out-file> <test-file>")
	sys.exit()

predictedfilepath = sys.argv[1]
actualfilepath = sys.argv[2]

actualfile = open(actualfilepath)
predictedfile = open(predictedfilepath)

correctly_classified = {}
total_actual_classes = {}
total_predicted_classes = {}

predicted_list = (line.strip() for line in predictedfile)

for predicted_label in predicted_list:
	line = actualfile.readline()
	words = line.rstrip('\n').split(' ')
	actual_label = words[0]
	if(predicted_label == actual_label):
		correctly_classified[predicted_label] = correctly_classified.get(predicted_label, 0) + 1
	total_predicted_classes[predicted_label] = total_predicted_classes.get(predicted_label, 0) + 1
	total_actual_classes[actual_label] = total_actual_classes.get(actual_label, 0) + 1


precision = dict((class_name, count/total_actual_classes[class_name]) for class_name, count in correctly_classified.items())
recall = dict((class_name, count/total_predicted_classes[class_name]) for class_name, count in correctly_classified.items())
fscore = dict((class_name, (2*prec*recall[class_name])/(prec+recall[class_name])) for class_name, prec in precision.items())


print("recall = " + repr(recall))
print("precision = " + repr(precision))
print("fscore = " + repr(fscore))





