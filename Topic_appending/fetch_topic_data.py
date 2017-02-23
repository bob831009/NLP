#!/usr/bin/python
import MySQLdb
import os

Categorys = ['HI', 'I'];
for category in Categorys:
	db = MySQLdb.connect(host="mysql", user="bob831009", passwd="jay26958320", db="orina1123")
	cursor = db.cursor()
	if(category == 'HI'):
		cursor.execute("SELECT DISTINCT subject FROM `Corpus_HI_document`");
	else:
		cursor.execute("SELECT DISTINCT subject FROM `Corpus_I_document`");
	result = cursor.fetchall();

	Subjects = [];
	for record in result:
		record = list(record);
		Subjects.append(record[0])

	for subject in Subjects:
		# print ("==========subject:"+subject+"==============");
		os.system("python fetch_data.py %s 400 %s" % (category, subject));
		os.system("python fetch_data_pass.py %s 400 %s" % (category, subject));
		# os.system("python prediction_Ensemble.py HI");
		# os.system("python prediction_Ensemble_pass.py HI");

os.system("python fetch_data.py HIS 400");
os.system('python fetch_data.py IS 400');

'''
print "==================Average=================="
subject_average_exactly = 0;
line_num = 0;
f = open("Ensemble_Exactly.txt", "r");
for line in f:
	subject_average_exactly += float(line);
	line_num += 1;
print "HI Subject Average Precision Exactly right: %lf" % (subject_average_exactly/line_num);
os.system("rm Ensemble_Exactly.txt");

subject_average_within_1 = 0;
line_num = 0;
f = open("./Ensemble_Within_1.txt", "r");
for line in f:
	subject_average_within_1 += float(line);
	line_num += 1;
print "HI Subject Average Precision Within 1: %lf" % (subject_average_within_1/line_num);
os.system("rm ./Ensemble_Within_1.txt");

subject_average_pass = 0;
line_num = 0;
f = open("./Ensemble_Pass.txt", "r");
for line in f:
	subject_average_pass += float(line);
	line_num += 1;
print "HI Subject Average Precision about Pass: %lf" % (subject_average_pass/line_num);
os.system("rm ./Ensemble_Pass.txt");


cursor.execute("SELECT DISTINCT subject FROM `Corpus_I_document`");
result = cursor.fetchall();
I_subject = [];
for record in result:
	record = list(record);
	I_subject.append(record[0])

for subject in I_subject:
	# print ("==========subject:"+subject+"==============");
	os.system("python fetch_data.py I 300 "+subject+" > I_feature_train.txt");
	os.system("python fetch_data.py I 150 "+subject+" > I_test.txt");
	os.system("python fetch_data_pass.py I 300 "+subject+" > I_pass_feature_train.txt");
	os.system("python fetch_data_pass.py I 150 "+subject+" > I_pass_test.txt");
	os.system("python prediction_Ensemble.py I");
	os.system("python prediction_Ensemble_pass.py I");

print "==================Average=================="
subject_average_exactly = 0;
line_num = 0;
f = open("Ensemble_Exactly.txt", "r");
for line in f:
	subject_average_exactly += float(line);
	line_num += 1;
print "I Subject Average Precision Exactly right: %lf" % (subject_average_exactly/line_num);
os.system("rm Ensemble_Exactly.txt");

subject_average_within_1 = 0;
line_num = 0;
f = open("./Ensemble_Within_1.txt", "r");
for line in f:
	subject_average_within_1 += float(line);
	line_num += 1;
print "I Subject Average Precision Within 1: %lf" % (subject_average_within_1/line_num);
os.system("rm ./Ensemble_Within_1.txt");

subject_average_pass = 0;
line_num = 0;
f = open("./Ensemble_Pass.txt", "r");
for line in f:
	subject_average_pass += float(line);
	line_num += 1;
print "I Subject Average Precision about Pass: %lf" % (subject_average_pass/line_num);
os.system("rm ./Ensemble_Pass.txt");
'''