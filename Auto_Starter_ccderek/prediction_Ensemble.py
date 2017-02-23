import numpy as np
from sklearn import svm
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import AdaBoostRegressor
import sys

category = [sys.argv[1]];
for elem in category:
	train_X = [];
	train_Y = [];
	train_path = './' + elem + '_feature_train.txt';
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


	output_path = './Ensemble_output/' + elem + '_ensemble.txt';
	output_file = open(output_path, 'w');

	err_0 = 0;
	err_1 = 0;
	err_2 = 0;
	err_3 = 0;
	over_est = 0;
	under_est = 0;
	for i in range(len(output_svm)):
		tmp_output = (output_svm[i] + output_Ada[i] + output_RF[i] + output_GB[i]) / 4;
		output_file.write("%f\n" % (tmp_output) );
		if(abs(tmp_output - test_Y[i]) <= 0.25):
			err_0 += 1;
		if(abs(tmp_output - test_Y[i]) <= 1.25):
			err_1 += 1;
		if(abs(tmp_output - test_Y[i]) <= 2.25):
			err_2 += 1;
		if(abs(tmp_output - test_Y[i]) <= 3.25):
			err_3 += 1;
		if(tmp_output >= test_Y[i]):
			over_est += 1;
		else:
			under_est += 1;

	# # print elem + " Precision Exactly right: %lf" % (float(err_0) / len(output_svm));
	# print elem + " Precision within 1 point: %lf" % (float(err_1) / len(output_svm));
	# print elem + " Precision within 2 point: %lf" % (float(err_2) / len(output_svm));
	# print elem + " Precision within 3 point: %lf" % (float(err_3) / len(output_svm));

	f = open("./Ensemble_Exactly.txt", "a");
	f.write("%lf\n" % (float(err_0) / len(output_svm)));
	f = open("./Ensemble_Within_1.txt", "a");
	f.write("%lf\n" % (float(err_1) / len(output_svm)));
	f = open("./Ensemble_Estimate.txt", 'a');
	f.write("%lf\n" % (float(over_est) / len(output_svm)));
