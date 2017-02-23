import MySQLdb
import subprocess

db = MySQLdb.connect(host="mysql", user="bob831009", passwd="jay26958320", db="orina1123");
cursor = db.cursor();

train_X = [];
train_Y = [];

query = "SELECT content FROM HIS_document";
cursor.execute(query);
text_num = 0;
for row in cursor:
	path = "../HIS_text/" + str(text_num) + ".txt";
	f = open(path, "w");
	text_num += 1;
	f.write(list(row)[0]);

subprocess.call("python analyzeText.py ../HIS_text/36.txt ../HIS_L2SCA.txt", shell=True);


