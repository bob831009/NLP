import MySQLdb;

db = MySQLdb.connect(host="mysql", user="bob831009", passwd="jay26958320", db="bob831009");
cursor = db.cursor();

for i in range(400):
	file_path = "./HIS_POS/" + str(i) + ".txt";
	f = open(file_path, "r");
	print "Handling " + str(i) + ".txt";
	for line in f:
		Word = line.strip().split(" ");
		for elem in Word:
			# print "Handling " + elem;
			word = (elem.split(","))[0];
			tag = (elem.split(","))[1];
			add_HISPOS = ("INSERT INTO HIS_StanfordPOS"
						  "(document_id, word, tag)"
						  "values (%s, %s, %s)");
			data_HISPOS = (str(i), word, tag);
			cursor.execute(add_HISPOS, data_HISPOS);
			db.commit();
db.close();