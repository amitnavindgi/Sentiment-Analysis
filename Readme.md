-------------------------------------------
	Instructions to run the classifiers
-------------------------------------------



1. NAIVE BAYES CLASSIFIER
--------------------------

For Email Classification

	-	Run the emails_formatter.py to generate training data in project data format. Make sure
		the vocab file enron.vocab is in the same running directory
		
		command : python3 emails_formatter.py <training-directory> <output-file-name> <mode>
		<training-directory> - directory containing raw email files
		<output-file-name> - desired output file name which is training file
		<mode> - training or testing
		
		example : python3 emails_formatter.py enron/ emails_training_data.txt training
	
	-	Run the splitter program to split the training data into 75% training and 25% development
		Change the percentages for different cases

		command : python3 splitter.py <input-file> <training-percentage>
		<input-file> - training file generated from above step which needs to be divided
		<training-percentage> - the percentage of data to be used for training

		example : python3 splitter.py emails_training_data.txt 75

		This generates two output files data_training.txt for training and data_development.txt for 
		development

	-	Run the nblearn.py using the above generated data_training.txt for every case to generate corresponding
		model file.

		command : python3 nblearn.py <training-file> <model-file>
		<training-file> - training file generated from above step
		<model-file> - name of the model file desired

		example : python3 nblearn.py data_training.txt model.txt

	-	Run the nbclassify.py using the model file generated in above step and also the test file for each 		case to get the final predictions

		command : python3 nblearn.py <model-file> <test-file> <mode>
		<model-file> - model file generated from nblearn.py
		<test-file> - test file to test the classifer. It can be the data_development.txt from step 2 above or actual test data
		<mode> - training or testing

		example : python3 nbclassify.py model.txt data_development.txt training

	-	Run stats.py to calculate F-score

		command : python3 stats.py <out-file> <actual-file>
		<out-file> - output from the classifier dumped into a file
		<actual-file> - the development/test file used for nbclassify.py

		example : python3 stats.py output.txt data_development.txt

For Sentiment Analysis

	-	Run sentiment_formatter.py to convert integers to labels POSITIVE or NEGATIVE

		command : python3 sentiment_formatter.py <input-file> <output-file>
		<input-file> : the labeled data already in project data format
		<output-file> : desired new output file name with labels POSITIVE and NEGATIVE

		example : python3 sentiment_formatter.py labeledBow.feat senti_labeled_training.txt

	-	Follow all the other steps just as done above in email classification





2. SUPPORT VECTOR MACHINES
---------------------------

For Email Classification

	-	Run email_formatter_svm.py to generate the labeled input with +1 for SPAM and -1 for HAM

		command : python3 email_formatter.py <input-dir> <output-file>
		<input-dir> - directory containing files of emails
		<output-file> - desired name of output file

		example : python3 email_formatter.py enron/ email_training_labeled_data.txt

		Run email_testing_formatter_svm.py to generate similar file for testing data in same way as above

	-	Use splitter.py in the same way as in the case of Naive Bayes to form data_training.txt to be used for 	   svm_learn and data_development.txt for classification

	-	Run svm_learn using the below command to generate the model file

		./svm_learn <training-file> <model-file>
		<training-file> : 75% data in first case and 25% in second run i.e data_training.txt from above step
		<model-file> : name of model desired to be generated

	-	Run svm_classify using below command to generate output file from classifier

		./svm_classify <example_file> <model_file> <output_file>
		<example_file> : data_development.txt file generated by splitter.py
		<model_file> : model file generated by svm_learn
		<output_file> : name of output file desired where values >0 and <0 are stored

	-	Run post_process_svm.py to replace values >0 by POSITIVE_CLASS and NEGATIVE_CLASS otherwise

		python3 post_process_svm.py <INPUT_FILE> <POSITIVE_CLASS> <NEGATIVE_CLASS>
		<INPUT_FILE> : output form classifer above
		<POSITIVE_CLASS> : SPAM or POSITIVE
		<NEGATIVE_CLASS> : HAM or NEGATIVE

	-	Run dev_data_labels_converter_svm.py tp convert +1 and -1's from development data to class labels for 		comparison in fscore.py

		python3 dev_data_labels_converter.py <development_file> <output-file>
		<development_file> : dev data file generated from splitter.py
		<output-file> : output file name desired

	-	Run fscore.py using output from above step and the output of post_process_svm.py
		Run fscore in same as you would for naive bayes as mentioned above


For Sentiment Analysis

	-	Run senti_formatter_svm.py to generate the labeled input with +1 for SPAM and -1 for HAM

		command : python3 senti_formatter.py <input-file> <output-file>
		<input-file> - file containing sentiment data in project data format
		<output-file> - desired name of output file

		example : python3 senti_formatter.py enron/ senti_training_labeled_data.txt

		Run senti_testing_formatter.py to generate similar file for testing data in same way as above 
		where increment the feature by 1 for all words in the data

	-	Split the training data generated above for two parts of the solution using splitter.py as described 	 for emails

	-	Run svm_learn and svm_classify in similar fashion to emails

	-	Run final_formatter_senti.py to convert values > and < 0 to labels

	-	Run fscore.y to calculate final scores just as in case of emails.



3. MAXIMUM ENTROPY MODELING
-----------------------------


For Email Classification

	-	Run email_formatter_mega.py to generate data in form required by 
		megaM for training data

		command : python3 email_formatter_mega.py <input-dir> <output-file>

		The arguments are same as ones provided to SVM. Refer above.

	-	Run splitter.py in similar fashion as discussed above for SVM

	-	Run dev_data_converter_mega.py on development file used in classification to convert numbers (0 and 1)
		to their corresponding classes(HAM/SPAM)

		command : python3 dev_data_converter_mega.py <development_file> <output-file>
		arguments are same as used previously

	-	Run megaM, get model file, use this for classifier and get fscore.

		megam <model-type> <input-file>
		commands are same as in the prious technique

For Sentiment analysis

	-	Follow same steps above except use the below files in this case



--------------------------------------------------------
RESULTS
--------------------------------------------------------

Part 1. FSCORES in case of 75% training data and 25% development data

	A. Email classification

			i)  Naive Bayes Classifier

				precision = {'HAM': 0.9770540340488527, 'SPAM': 0.9964899964899965}
				recall = {'HAM': 0.9962264150943396, 'SPAM': 0.9786280592899}
				fscore = {'HAM': 0.9865470852017937, 'SPAM': 0.9874782608695652}

			ii) SVM

				precision = {'HAM': 0.926829268292683, 'SPAM': 0.992399565689468}
				recall = {'HAM': 0.9919385796545106, 'SPAM': 0.9307535641547862}
				fscore = {'HAM': 0.9582792508807714, 'SPAM': 0.9605885444035733}

			iii) MegaM

	B. Sentiment Analysis

			i)  Naive Bayes Classifier

				precision = {'NEGATIVE': 0.8975594091201028, 'POSITIVE': 0.8115433673469388}
				recall = {'NEGATIVE': 0.825457767277023, 'POSITIVE': 0.8886173184357542}
				fscore = {'NEGATIVE': 0.8600000000000001, 'POSITIVE': 0.8483333333333333}

			ii) SVM

				precision = {'POSITIVE': 0.8791881443298969, 'NEGATIVE': 0.845518118245391}
				recall = {'POSITIVE': 0.8488335925349922, 'NEGATIVE': 0.8764415156507414}
				fscore = {'POSITIVE': 0.8637442633328057, 'NEGATIVE': 0.8607021517553793}


			iii) MegaM

Part 2. FSCORES in case of 25% training data and 75% development data


	A. Email classification

			i)  Naive Bayes Classifier

				precision = {'SPAM': 0.9933102377254808, 'HAM': 0.9716252113016179}
				recall = {'SPAM': 0.9725146198830409, 'HAM': 0.9930889793903492}
				fscore = {'HAM': 0.9822398535245651, 'SPAM': 0.9828024348442763}

			ii) SVM

				precision = {'HAM': 0.9888440541182055, 'SPAM': 0.8949799440865444}
				recall = {'HAM': 0.9060461070030448, 'SPAM': 0.9873943945286309}
				fscore = {'HAM': 0.9456361366473726, 'SPAM': 0.9389186432032646}
			
			iii) MegaM



	B. Sentiment Analysis

			i)  Naive Bayes Classifier

				precision = {'POSITIVE': 0.8050341296928327, 'NEGATIVE': 0.8889481544698101}
				recall = {'POSITIVE': 0.8787984631505414, 'NEGATIVE': 0.8200964472000787}
				fscore = {'POSITIVE': 0.8403005844698024, 'NEGATIVE': 0.8531353980035834}


			ii) SVM

				precision = {'POSITIVE': 0.8583768795990189, 'NEGATIVE': 0.8221487250613464}
				recall = {'POSITIVE': 0.8284273363524084, 'NEGATIVE': 0.8529997786141245}
				fscore = {'POSITIVE': 0.8431362279369402, 'NEGATIVE': 0.8372901613516598}


			iii) MegaM


