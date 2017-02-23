#!/usr/bin/env python
from svm import *
from svmutil import *

# print "python work well!\n";

train_X = [];
train_Y = [];
test_X = [];
test_Y = [];
# print "hi";
try:
	f = open("./libsvm-3.20/python/test_each.txt", "r");
except IOError:
    print "Could not open file!";
# print "hi";
for line in f:
	# print line;
	line = line.strip().split();
	line = line[10:];
	if(line[0] == 'A'):
		test_Y.append(1);
	else:
		test_Y.append(-1);
	line.pop(0);
	line = map(float, line);
	test_X.append(line);

model = svm_load_model('./libsvm-3.20/python/LTTC.model');
p_labels, p_acc, p_vals = svm_predict(test_Y, test_X, model, '-q');
print p_labels[0];

f.close();