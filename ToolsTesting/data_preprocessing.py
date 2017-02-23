#!/usr/bin/python
import MySQLdb
import numpy as np
from sklearn import svm
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import AdaBoostRegressor
import sys
import random

def check_and_get_data(data, file_name, index):
	if(index not in data[file_name]):
		return [0]*len(data[file_name][data[file_name].keys()[0]]);
	else:
		return data[file_name][index];

db = MySQLdb.connect(host="mysql", user="bob831009", passwd="jay26958320", db="orina1123");
cursor = db.cursor()
db_command = "SELECT b.score,a.* FROM IS_document_feature AS a INNER JOIN IS_document AS b ON a.document_id = b.document_id ORDER BY a.document_id";
cursor.execute(db_command);
result = cursor.fetchall()

ID2score = {};
ID2feature = {};
Total_data_num = len(list(result));
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

column_name = [];
db_command = "SHOW columns FROM IS_document_feature";
cursor.execute(db_command);
columns_info = cursor.fetchall()[1:];
column_name.append('document_id');
column_name.append('score');
for column_record in columns_info:
	column_name.append(column_record[0]);

# ======load data=======
data = {};

input_file_name = ['IS_results_TAALES.csv', 'IS_results_TAACO.csv'];
# input_file_name = ['I_results_TAALES.csv', 'I_results_TAACO.csv', 'I_results_TAASSC.csv'];
for index, file_name in enumerate(input_file_name):
	Handle_line = 0;
	f = open(file_name, 'r');
	data[file_name] = {};

	for line in f:
		line = line.strip().split(',');
		if(Handle_line == 0):
			line.pop(0) # remove doc_name
			if(file_name[-9:] == 'TAACO.csv'):
				line.pop(); # remove last empty column name
			column_name.extend(line);
			Handle_line += 1;
			continue;
		doc_name = line[0];
		doc_id = int(doc_name[doc_name.find('doc_')+4:doc_name.find('.txt')]);
		line.pop(0);
		line = map(float, line);
		data[file_name][doc_id] = line;
	f.close();

f = open('IS_blending_result.csv', 'w');
for index, elem in enumerate(column_name):
	if(index == len(column_name) - 1):
		f.write("%s"%(elem));
	else:
		f.write("%s,"%(elem));
f.write('\n');
for i in range(1, Total_data_num+1):
	total_input_data = [i, ID2score[i]] + ID2feature[i];
	for file_name in input_file_name:
		total_input_data += check_and_get_data(data, file_name, i);

	for index, elem in enumerate(total_input_data):
		if(index == len(column_name) - 1):
			f.write('%s'%(elem));
		else:
			f.write('%s,'%(elem));
	f.write('\n');



