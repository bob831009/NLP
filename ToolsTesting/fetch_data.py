#!/usr/bin/python
import MySQLdb
import sys

db = MySQLdb.connect(host="mysql", user="bob831009", passwd="jay26958320", db="orina1123");
cursor = db.cursor()
db_command = "SELECT document_id, content FROM HIS_document ORDER BY document_id";
cursor.execute(db_command);
result = cursor.fetchall()

for record in result:
	record = list(record);
	document_name = "doc_%s.txt" % (record[0]);
	content = record[1];
	f = open("./document_HIS/%s" % (document_name), 'w');
	f.write(content);

	f.close();