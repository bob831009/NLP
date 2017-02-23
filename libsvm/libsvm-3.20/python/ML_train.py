#!/usr/bin/env python
from svm import *
from svmutil import *

train_X = [];
train_Y = [];
test_X = [];
test_Y = [];

f = open("./libsvm-3.20/python/train.txt", "r");

for line in f:
	line = line.strip().split();
	line = line[10:];
	if(line[0] == 'A'):
		train_Y.append(1);
	else:
		train_Y.append(-1);
	line.pop(0);
	line = map(float, line);
	train_X.append(line);

problem = svm_problem(train_Y, train_X);

tmp_param = '-t 1 -c 1 -g 1 -r 1 -d 2 -q';
param = svm_parameter(tmp_param);
model = svm_train(problem, param);
svm_save_model('./libsvm-3.20/python/LTTC.model', model);