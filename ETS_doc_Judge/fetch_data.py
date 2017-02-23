#!/usr/bin/python
import MySQLdb
import sys


db = MySQLdb.connect(host="mysql", user="bob831009", passwd="jay26958320", db="ccderek")
cursor = db.cursor()
query_str = "SELECT b.Level,a.* FROM ETS_document_feature_LC AS a INNER JOIN ETS_document AS b ON a.document_id = b.document_id ORDER BY RAND() LIMIT ";
query_str = query_str + sys.argv[1];
cursor.execute(query_str);
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
			if(elem == 'high'):
				sys.stdout.write("1 ");
			elif(elem == 'medium'):
				sys.stdout.write("2 ");
			elif(elem == 'low'):
				sys.stdout.write("3 ");
			else:
				print("error score!");
				exit(0);
		else:
			if(elem == None):
				sys.stdout.write("0 ");
			else:
				sys.stdout.write("%lf " % (elem));
		i += 1; 
	print "";