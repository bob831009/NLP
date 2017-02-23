from nltk.tag import StanfordPOSTagger

st = StanfordPOSTagger('models/english-bidirectional-distsim.tagger', 'stanford-postagger.jar');

for i in range(400):
	print "Handling file " + str(i);
	filepath = "./HIS_text/" + str(i) + ".txt" ;
	f = open(filepath, "r");
	result = [];
	ori_line = [];
	char_num = 0;
	for line in f:
		ori_line = line.split();
		char_num = len(line.split());
		result.extend(st.tag(map(str.lower, line.split())));
	# print line_num;
	f.close();
	filepath = "./HIS_POS/" + str(i) + ".txt" ;
	output_f = open(filepath, "w");
	tmp_char_num = 0;
	for elem in result:
		output_f.write("%s,%s " % (ori_line[tmp_char_num], elem[1]));
		tmp_char_num += 1;
	output_f.close();