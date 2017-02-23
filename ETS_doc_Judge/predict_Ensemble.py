import numpy as np
from sklearn import svm
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import AdaBoostRegressor
import sys

category = ['ETS'];
for elem in category:
	train_X = [];
	train_Y = [];
	train_path = './' + elem + '_train.txt';
	f = open(train_path, 'r');
	for line in f:
		line = line.strip().split(' ');
		line = map(float, line);
		train_Y.append(line[0]);
		line.pop(0);
		train_X.append(line);

	test_X = [];
	test_Y = [];
	test_path = './' + elem + '_test.txt';
	f = open(test_path, 'r');
	for line in f:
		line = line.strip().split(' ');
		line = map(float, line);
		test_Y.append(line[0]);
		line.pop(0);
		test_X.append(line);


	clf_svm = svm.SVR();
	clf_svm.fit(train_X, train_Y);
	output_svm = clf_svm.predict(test_X);

	clf_GB = GradientBoostingRegressor()
	clf_GB.fit(train_X, train_Y);
	output_GB = clf_GB.predict(test_X);

	clf_RF = RandomForestRegressor()
	clf_RF.fit(train_X, train_Y);
	output_RF = clf_RF.predict(test_X);

	clf_Ada = AdaBoostRegressor()
	clf_Ada.fit(train_X, train_Y);
	output_Ada = clf_Ada.predict(test_X);


	output_path = './' + elem + '_ensemble_output.txt';
	output_file = open(output_path, 'w');

	error = [0, 0, 0];
	correct = [0, 0, 0];
	for i in range(len(output_svm)):
		tmp_output = (output_svm[i] + output_Ada[i] + output_RF[i] + output_GB[i]) / 4;
		output_file.write("%f\n" % (tmp_output) );
		if(abs(tmp_output - test_Y[i]) <= 0.5):
			correct[int(test_Y[i]) - 1] += 1;
		else:
			error[int(test_Y[i]) - 1] += 1;

	print "Precision Exactly right: %lf" % (float(sum(correct)) / len(output_svm));
	print "Precision Exactly right (high): %lf" % (float(correct[2]) / len(output_svm));
	print "Precision Exactly right (medium): %lf" % (float(correct[1]) / len(output_svm));
	print "Precision Exactly right (low): %lf" % (float(correct[0]) / len(output_svm));