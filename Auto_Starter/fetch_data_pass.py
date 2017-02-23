#!/usr/bin/python
import MySQLdb
import sys

if(len(sys.argv) > 3):
	subject = sys.argv[3];
if(sys.argv[1] == "HI" or sys.argv[1] == "I" or sys.argv[1] == "HIS"):
	db = MySQLdb.connect(host="mysql", user="bob831009", passwd="jay26958320", db="orina1123");
else:
	db = MySQLdb.connect(host="mysql", user="bob831009", passwd="jay26958320", db="joanne3634");

cursor = db.cursor();
if(sys.argv[1] == "HI"):
	subject = 'HW-0801';
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


for record in result:
	record = list(record);
	record.pop(1);
	i = 0;
	for elem in record:
		if(i == 0):
			# transform to pass or not
			# ===================
			if(elem >= 4):
				elem = 1;
			else:
				elem = 0;
			# ===================
			sys.stdout.write("%lf " % (elem));
		else:
			if(elem == None):
				sys.stdout.write("0 ");
			else:
				sys.stdout.write("%lf " % (elem));
		i += 1; 
	print "";