#!/usr/bin/python
import MySQLdb
import numpy as np
from sklearn import svm
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import AdaBoostRegressor
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
	random_num = random.random();
	if(random_num <= 0.8):
		train_X.append(line);
		train_Y.append(ID2score[doc_id]);
	else:
		test_X.append(line);
		test_Y.append(ID2score[doc_id]);

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


err_0 = 0;
err_1 = 0;
err_2 = 0;
err_3 = 0;
for i in range(len(output_svm)):
	ensemble_output = float(output_svm[i] + output_Ada[i] + output_RF[i] + output_GB[i]) / 4;

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

