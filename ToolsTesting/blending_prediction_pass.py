#!/usr/bin/python
import MySQLdb
import numpy as np
from sklearn import svm
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
import sys
import random
from scipy.stats.stats import pearsonr

# ======load data=======
print('loading data...');
train_X = [];
train_Y = [];
test_X = [];
test_Y = [];
test_ID_list = [];
column_name = [];
Handle_line = 0;

f = open('IS_blending_result.csv', 'r');
for line in f:
	line = line.strip().split(',');
	if(Handle_line == 0):
		column_name = line;
		Handle_line += 1;
		continue;
	line = map(float, line);
	doc_id = int(line[0]);
	score = line[1];
	if(score >= 4):
		score = 1;
	else:
		score = 0;
	line = line[2:];

	random_num = random.random();
	if(random_num <= 0.8):
		train_X.append(line);
		train_Y.append(score);
	else:
		test_X.append(line);
		test_Y.append(score);
		test_ID_list.append(doc_id);

print('SVM model prediction');
clf_svm = svm.SVC();
clf_svm.fit(train_X, train_Y);
output_svm = clf_svm.predict(test_X);
	
print('GradientBoosting model prediction');
clf_GB = GradientBoostingClassifier()
clf_GB.fit(train_X, train_Y);
output_GB = clf_GB.predict(test_X);

print('RandomForest model prediction');
clf_RF = RandomForestClassifier()
clf_RF.fit(train_X, train_Y);
output_RF = clf_RF.predict(test_X);

print('AdaBoost model prediction');
clf_Ada = AdaBoostClassifier()
clf_Ada.fit(train_X, train_Y);
output_Ada = clf_Ada.predict(test_X);

final_output = []
True_Positive = 0;
True_Negative = 0;
False_Positive = 0;
False_Negative = 0;

for i in range(len(output_svm)):
	ensemble_output = float(output_svm[i] + output_Ada[i] + output_RF[i] + output_GB[i]) / 4;
	final_output.append(ensemble_output);
	if(ensemble_output >= 0.5):
		ensemble_output = 1;
	else:
		ensemble_output = 0;

	if(ensemble_output == test_Y[i]):
		if(test_Y[i] == 0):
			True_Positive += 1;
		else:
			True_Negative += 1;
	elif(ensemble_output != test_Y[i]):
		if(test_Y[i] == 0):
			False_Positive += 1;
		else:
			False_Negative += 1;

print("Precision about Pass: %lf" % (float(True_Positive + True_Negative)/len(output_svm)));
print("True_Positive: %lf" % (float(True_Positive) / len(output_svm)));
print("True_Negative: %lf" % (float(True_Negative) / len(output_svm)));
print("False_Positive: %lf" % (float(False_Positive) / len(output_svm)));
print("False_Negative: %lf" % (float(False_Negative) / len(output_svm)));

# =====counting correlate=====
'''
f = open('IS_correlate_pass.csv', 'w');
for i in range(len(column_name)-2):
	column_data = [];
	for j in range(len(test_ID_list)):
		column_data.append(test_X[j][i]);
	correlate_num = list(pearsonr(final_output, column_data))[0];
	f.write('%s,%f\n'%(column_name[i+2], correlate_num));
'''
