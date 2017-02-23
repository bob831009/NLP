import numpy as np
from sklearn import svm
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier


category = ['HI', 'I', 'HIS', 'IS']
for elem in category:
	train_X = [];
	train_Y = [];
	train_path = './DataBase/' + elem + '_pass_feature_train.txt';
	f = open(train_path, 'r');
	for line in f:
		line = line.strip().split(' ');
		line = map(float, line);
		train_Y.append(line[0]);
		line.pop(0);
		train_X.append(line);

	test_X = [];
	test_Y = [];
	test_path = './DataBase/' + elem + '_pass_test.txt';
	f = open(test_path, 'r');
	for line in f:
		line = line.strip().split(' ');
		line = map(float, line);
		test_Y.append(line[0]);
		line.pop(0);
		test_X.append(line);


	clf_svm = svm.SVC();
	clf_svm.fit(train_X, train_Y);
	output_svm = clf_svm.predict(test_X);

	clf_GB = GradientBoostingClassifier()
	clf_GB.fit(train_X, train_Y);
	output_GB = clf_GB.predict(test_X);

	clf_RF = RandomForestClassifier()
	clf_RF.fit(train_X, train_Y);
	output_RF = clf_RF.predict(test_X);

	clf_Ada = AdaBoostClassifier()
	clf_Ada.fit(train_X, train_Y);
	output_Ada = clf_Ada.predict(test_X);


	output_path = './Ensemble_output/' + elem + '_ensemble_pass.txt';
	output_file = open(output_path, 'w');

	correct_pass = 0;
	correct_nopass = 0;
	error_pass = 0;
	error_nopass = 0;
	for i in range(len(output_svm)):
		tmp_output = float(output_svm[i] + output_Ada[i] + output_RF[i] + output_GB[i]) / 4;
		if(tmp_output >= 0.5):
			tmp_output = 1;
		else:
			tmp_output = 0;
		output_file.write("%f\n" % (tmp_output) );
		if(tmp_output == test_Y[i]):
			if(test_Y[i] == 0):
				correct_nopass += 1;
			else:
				correct_pass += 1;
		elif(tmp_output != test_Y[i]):
			if(test_Y[i] == 0):
				error_nopass += 1;
			else:
				error_pass += 1;

	print elem + " Precision about Pass: %lf" % (float(correct_pass + correct_nopass)/len(output_svm));
	print elem + " Percent about Correct[pass]: %lf" % (float(correct_pass)/len(output_svm));
	print elem + " Percent about Correct[no pass]: %lf" % (float(correct_nopass)/len(output_svm));
	print elem + " Percent about Wrong[origin pass]: %lf" % (float(error_pass)/len(output_svm));
	print elem + " Percent about Wrong[origin no pass]: %lf" % (float(error_nopass)/len(output_svm));

