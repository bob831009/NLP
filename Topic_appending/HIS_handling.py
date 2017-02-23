import MySQLdb
import sys
import os

def recalculate_word_level(doc, wordlist):
	level = [0] * 7;
	word_count = {};
	for word in doc.strip().split(' '):
		if word in wordlist:
			level[wordlist[word]-1] += 1;
		else:
			level[6] += 1;

		if word in word_count:
			word_count[word] += 1;
		else:
			word_count[word] = 1;

	return level, word_count;

db = MySQLdb.connect(host="mysql", user="bob831009", passwd="jay26958320", db="orina1123");
cursor = db.cursor();
SQL_command = "SELECT b.score,b.content,a.*,c.* FROM HIS_document_feature AS a INNER JOIN HIS_document AS b ON a.document_id = b.document_id INNER JOIN HIS_document_LCA AS c ON c.document_id = b.document_id ORDER BY a.document_id";
cursor.execute(SQL_command);
Data = cursor.fetchall()

SQL_command_wordlist = 'SELECT * FROM wordlist_level'
cursor.execute(SQL_command_wordlist);
wordlist_data = cursor.fetchall();

SQL_command_getColumnName = "SELECT column_name FROM information_schema.columns WHERE table_name='HIS_document_feature';"
cursor.execute(SQL_command_getColumnName);
HIS_doc_column_name = cursor.fetchall();

SQL_command_getColumnName = "SELECT column_name FROM information_schema.columns WHERE table_name='HIS_document_LCA';"
cursor.execute(SQL_command_getColumnName);
HIS_LCA_doc_column_name = cursor.fetchall();

column_name = ['score'];
for elem in HIS_doc_column_name[6:25] + HIS_doc_column_name[32:] + HIS_LCA_doc_column_name[2:]:
	column_name.append(elem[0]);

wordlist = {};
for word_record in wordlist_data:
	wordlist[word_record[1]] = int(word_record[3]);

fp = open('new_HIS.csv', 'w');

# =======output name========
for elem in column_name:
	fp.write('%s,' % elem);
fp.write('\n');

# =======output data========
for data in Data:
	data = list(data);
	level, word_count = recalculate_word_level(data[1], wordlist);
	data.pop(2); # remove id
	data.pop(1); # remove content

	for i in range(6, 20, 2):
		data[i] = level[(i-6)/2];
		data[i+1] = (float(level[(i-6)/2]) / sum(level)) * 100;

	data[20] = level[4] + level[5] + level[6]
	data[21] = (float(level[4] + level[5] + level[6]) / sum(level)) * 100;

	data[22] = sum(word_count.values());
	data[23] = len(word_count.keys());
	data[24] = float(data[23]) / data[22];

	new_data = data[:1] + data[6:25] + data[32:45] + data[47:];

	for elem in new_data:
		if(elem == None):
			fp.write('0,');
		else:
			fp.write('%lf,' % (elem));
	fp.write('\n');