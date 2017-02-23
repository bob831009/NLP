#!/usr/bin/python
import MySQLdb
import numpy as np
from sklearn import svm
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import AdaBoostRegressor
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
clf_svm = svm.SVR();
clf_svm.fit(train_X, train_Y);
output_svm = clf_svm.predict(test_X);
	
print('GradientBoosting model prediction');
clf_GB = GradientBoostingRegressor()
clf_GB.fit(train_X, train_Y);
output_GB = clf_GB.predict(test_X);

print('RandomForest model prediction');
clf_RF = RandomForestRegressor()
clf_RF.fit(train_X, train_Y);
output_RF = clf_RF.predict(test_X);

print('AdaBoost model prediction');
clf_Ada = AdaBoostRegressor()
clf_Ada.fit(train_X, train_Y);
output_Ada = clf_Ada.predict(test_X);

final_output = []
err_0 = 0;
err_1 = 0;
err_2 = 0;
err_3 = 0;
for i in range(len(output_svm)):
	ensemble_output = float(output_svm[i] + output_Ada[i] + output_RF[i] + output_GB[i]) / 4;
	final_output.append(ensemble_output);
	if(abs(ensemble_output - test_Y[i]) <= 0.25):
		err_0 += 1;
	if(abs(ensemble_output - test_Y[i]) <= 1.25):
		err_1 += 1;
	if(abs(ensemble_output - test_Y[i]) <= 2.25):
		err_2 += 1;
	if(abs(ensemble_output - test_Y[i]) <= 3.25):
		err_3 += 1;

print("Precision Exactly right: %lf" % (float(err_0) / len(output_svm)));
print("Precision within 1 point: %lf" % (float(err_1) / len(output_svm)));
print("Precision within 2 point: %lf" % (float(err_2) / len(output_svm)));
print("Precision within 3 point: %lf" % (float(err_3) / len(output_svm)));


# =====counting correlate=====
'''
f = open('IS_correlate.csv', 'w');
for i in range(len(column_name)-2):
	column_data = [];
	for j in range(len(test_ID_list)):
		column_data.append(test_X[j][i]);
	correlate_num = pearsonr(column_data, final_output);
	f.write('%s,%f\n'%(column_name[i+2], correlate_num[0]));
'''