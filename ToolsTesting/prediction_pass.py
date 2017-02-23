#!/usr/bin/python
import MySQLdb
import numpy as np
from sklearn import svm
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
import sys
import random

db = MySQLdb.connect(host="mysql", user="bob831009", passwd="jay26958320", db="orina1123");
cursor = db.cursor()
db_command = "SELECT b.score,a.* FROM Corpus_HI_document_feature AS a INNER JOIN Corpus_HI_document AS b ON a.document_id = b.document_id ORDER BY a.document_id";
cursor.execute(db_command);
result = cursor.fetchall()

ID2score = {};
ID2feature = {};
for record in result:
	record = list(record);
	document_id = int(record[1]);
	score = float(record[0]);
	record.pop(0);
	record.pop(0);
	ID2score[document_id] = score;
	for i in range(len(record)):
		if(record[i] == None):
			record[i] = 0;
	ID2feature[document_id] = map(float, record);

# ======load data=======
print('loading data...');
train_X = [];
train_Y = [];
test_X = [];
test_Y = [];
column_name = [];
Handle_line = 0;
f = open('HI_results_TAALES.csv', 'r');
for line in f:
	line = line.strip().split(',');
	if(Handle_line == 0):
		column_name = line;
		Handle_line += 1;
		continue;
	doc_name = line[0];
	doc_id = int(doc_name[doc_name.find('doc_')+4:doc_name.find('.txt')]);
	
	line.pop(0);
	line = map(float, line);
	line.extend(ID2feature[doc_id]);
	score = ID2score[doc_id];
	if(score >= 4):
		score = 1;
	else:
		score = 0;
	random_num = random.random();
	if(random_num <= 0.8):
		train_X.append(line);
		train_Y.append(score);
	else:
		test_X.append(line);
		test_Y.append(score);

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

True_Positive = 0;
True_Negative = 0;
False_Positive = 0;
False_Negative = 0;

for i in range(len(output_svm)):
	ensemble_output = float(output_svm[i] + output_Ada[i] + output_RF[i] + output_GB[i]) / 4;
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
