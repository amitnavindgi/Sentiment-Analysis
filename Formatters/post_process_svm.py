import sys

if(len(sys.argv) != 4):
    print('Format -> python3 post_process_svm.py <INPUT_FILE> <POSITIVE_CLASS> <NEGATIVE_CLASS>')
    sys.exit()

input_file = sys.argv[1]
pos = sys.argv[2]
neg = sys.argv[3]

with open(input_file) as f:
    for line in f:
        value = float(line.rstrip('\n'))
        if(value > 0):
            print(pos)
        else:
            print(neg)