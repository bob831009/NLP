#!/usr/bin/python
import MySQLdb
import sys
import os

if(len(sys.argv) > 3):
	subject = sys.argv[3];
	if(not os.path.isdir(os.path.join('./DataBase', sys.argv[1], sys.argv[3]))):
		os.mkdir(os.path.join('./DataBase', sys.argv[1], sys.argv[3]));
if(sys.argv[1] == "HI" or sys.argv[1] == "I" or sys.argv[1] == "HIS"):
	db = MySQLdb.connect(host="mysql", user="bob831009", passwd="jay26958320", db="orina1123");
else:
	db = MySQLdb.connect(host="mysql", user="bob831009", passwd="jay26958320", db="joanne3634");

cursor = db.cursor();
if(sys.argv[1] == "HI"):
	tmp_str = "SELECT b.score,a.* FROM Corpus_HI_document_feature AS a INNER JOIN Corpus_HI_document AS b ON a.document_id = b.document_id AND b.subject = '" + subject +"' ORDER BY RAND() LIMIT ";
	tmp_str = tmp_str + sys.argv[2];
	cursor.execute(tmp_str);
elif(sys.argv[1] == "I"):
	subject = 'IW-0801';
	tmp_str = "SELECT b.score,a.* FROM Corpus_I_document_feature AS a INNER JOIN Corpus_I_document AS b ON a.document_id = b.document_id AND b.subject = '" + subject +"' ORDER BY RAND() LIMIT ";
	tmp_str = tmp_str + sys.argv[2];
	cursor.execute(tmp_str);
elif(sys.argv[1] == "HIS"):
	tmp_str = "SELECT b.score,a.* FROM HIS_document_feature AS a INNER JOIN HIS_document AS b ON a.document_id = b.document_id ORDER BY RAND() LIMIT ";
	tmp_str = tmp_str + sys.argv[2];
	cursor.execute(tmp_str);
elif(sys.argv[1] == "IS"):
	tmp_str = "SELECT b.score,a.* FROM IS_document_feature AS a INNER JOIN IS_document AS b ON a.document_id = b.document_id ORDER BY RAND() LIMIT ";
	tmp_str = tmp_str + sys.argv[2];
	cursor.execute(tmp_str);
result = cursor.fetchall()

# for name in cursor.description:
# 	print name[0],;
# print "";
# train_output_dir = './DataBase/' + sys.argv[1] + '_feature_train.txt';
# test_output_dir = './DataBase/' + sys.argv[1] + '_test.txt';
if(len(sys.argv) > 3):
	train_output_dir = os.path.join('./DataBase', sys.argv[1], sys.argv[3], 'feature_train.csv');
	test_output_dir = os.path.join('./DataBase', sys.argv[1], sys.argv[3], 'test.csv');
else:
	train_output_dir = os.path.join('./DataBase', sys.argv[1], 'feature_train.csv');
	test_output_dir = os.path.join('./DataBase', sys.argv[1], 'test.csv');
fp_train = open(train_output_dir, 'w');
fp_test = open(test_output_dir, 'w');

train_set_size = int(sys.argv[2]) * 0.8;
test_set_size = int(sys.argv[2]) * 0.2;

Handled_set_size = 0;
for record in result:
	Handled_set_size += 1;
	record = list(record);
	if(sys.argv[1] == 'IS'):
		record.pop(4) # remove score from joanne3634
	record.pop(1); # remove id

	if(Handled_set_size < train_set_size):
		output_fp = fp_train;
	else:
		output_fp = fp_test;

	i = 0;
	for elem in record:
		if(i == 0):
			output_fp.write("%lf, " % (elem));
		else:
			if(elem == None):
				output_fp.write("0, ");
			else:
				output_fp.write("%lf, " % (elem));
		i += 1; 
	output_fp.write('\n');