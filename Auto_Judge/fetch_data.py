#!/usr/bin/python
import MySQLdb
import sys


db = MySQLdb.connect(host="mysql", user="bob831009", passwd="jay26958320", db="orina1123")
cursor = db.cursor()
if(sys.argv[1] == "HI"):
	tmp_str = "SELECT b.score,a.* FROM Corpus_HI_document_feature AS a INNER JOIN Corpus_HI_document AS b ON a.document_id = b.document_id ORDER BY RAND() LIMIT ";
	tmp_str = tmp_str + sys.argv[2];
	cursor.execute(tmp_str);
elif(sys.argv[1] == "I"):
	tmp_str = "SELECT b.score,a.* FROM Corpus_I_document_feature AS a INNER JOIN Corpus_I_document AS b ON a.document_id = b.document_id ORDER BY RAND() LIMIT ";
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
			sys.stdout.write("%lf " % (elem));
		else:
			if(elem == None):
				sys.stdout.write("%d:0 " % (i-1));
			else:
				sys.stdout.write("%d:%lf " % (i-1, elem));
		i += 1; 
	print "";