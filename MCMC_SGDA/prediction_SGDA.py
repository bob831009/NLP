import sys
import subprocess

def Do_Calculation(file_name1, file_name2, range_num):
	f1 = open(file_name1);
	f2 = open(file_name2);

	Correct_num = 0;
	Total_num = 0;
	while(True):
		line1 = f1.readline();
		line2 = f2.readline();
		if(len(line1) == 0 and len(line2) == 0):
			break;

		line1 = line1.strip().split();
		line2 = line2.strip().split();
		if (abs(float(line1[0]) - float(line2[0]) ) <= range_num):
			Correct_num += 1;
		Total_num +=1;

	f1.close();
	f2.close();
	return float(Correct_num)*100/Total_num;

def Do_Pass_Calculation(file_name1, file_name2):
	f1 = open(file_name1);
	f2 = open(file_name2);

	Correct_num = 0;
	Total_num = 0;

	Correct_pass = 0;
	Correct_nopass = 0;
	Wrong_pass = 0;
	Wrong_nopass = 0;
	while(True):
		line1 = f1.readline();
		line2 = f2.readline();
		if(len(line1) == 0 and len(line2) == 0):
			break;

		line1 = line1.strip().split();
		line2 = line2.strip().split();
		if(float(line2[0]) > 0.5):
			prediction = 1;
		else:
			prediction = 0;

		if (float(line1[0]) == float(prediction)):
			Correct_num += 1;
			if(float(line1[0]) == 1):
				Correct_pass += 1;
			elif(float(line1[0]) == 0):
				Correct_nopass += 1;
		else:
			if(float(line1[0]) == 1):
				Wrong_pass += 1;
			elif(float(line1[0]) == 0):
				Wrong_nopass += 1;
		Total_num +=1;

	f1.close();
	f2.close();

	Total_precision = float(Correct_num)*100/Total_num;
	Correct_pass_percent = float(Correct_pass)*100/Total_num;
	Correct_nopass_percent = float(Correct_nopass)*100/Total_num;
	Wrong_pass_percent = float(Wrong_pass)*100/Total_num;
	Wrong_nopass_percent = float(Wrong_nopass)*100/Total_num;
	return [Total_precision, Correct_pass_percent, Correct_nopass_percent, Wrong_pass_percent, Wrong_nopass_percent];

cmd = './libfm-1.42.src/bin/libFM -task r -train ./HI_feature_train.txt -test ./HI_test.txt -iter 1000 -method sgda -learn_rate 0.01 -init_stdev 0.1 -validation HI_feature_val.txt -out HI_prediction.txt'
retcode = subprocess.call(cmd, shell=True);

cmd = './libfm-1.42.src/bin/libFM -task r -train ./I_feature_train.txt -test ./I_test.txt -iter 1000 -method sgda -learn_rate 0.01 -init_stdev 0.1 -validation I_feature_val.txt -out I_prediction.txt'
retcode = subprocess.call(cmd, shell=True);

cmd = './libfm-1.42.src/bin/libFM -task r -train ./HIS_feature_train.txt -test ./HIS_test.txt -iter 1000 -method sgda -learn_rate 0.01 -init_stdev 0.1 -validation HIS_feature_val.txt -out HIS_prediction.txt'
retcode = subprocess.call(cmd, shell=True);

cmd = './libfm-1.42.src/bin/libFM -task r -train ./IS_feature_train.txt -test ./IS_test.txt -iter 1000 -method sgda -learn_rate 0.01 -init_stdev 0.1 -validation IS_feature_val.txt -out IS_prediction.txt'
retcode = subprocess.call(cmd, shell=True);

cmd = './libfm-1.42.src/bin/libFM -task c -train ./HI_pass_feature_train.txt -test ./HI_pass_test.txt -iter 1000 -method sgda -learn_rate 0.01 -init_stdev 0.1 -validation HI_pass_feature_val.txt -out HI_pass_prediction.txt'
retcode = subprocess.call(cmd, shell=True);

cmd = './libfm-1.42.src/bin/libFM -task c -train ./I_pass_feature_train.txt -test ./I_pass_test.txt -iter 1000 -method sgda -learn_rate 0.01 -init_stdev 0.1 -validation I_pass_feature_val.txt -out I_pass_prediction.txt'
retcode = subprocess.call(cmd, shell=True);

cmd = './libfm-1.42.src/bin/libFM -task c -train ./HIS_pass_feature_train.txt -test ./HIS_pass_test.txt -iter 1000 -method sgda -learn_rate 0.01 -init_stdev 0.1 -validation HIS_pass_feature_val.txt -out HIS_pass_prediction.txt'
retcode = subprocess.call(cmd, shell=True);

cmd = './libfm-1.42.src/bin/libFM -task c -train ./IS_pass_feature_train.txt -test ./IS_pass_test.txt -iter 1000 -method sgda -learn_rate 0.01 -init_stdev 0.1 -validation IS_pass_feature_val.txt -out IS_pass_prediction.txt'
retcode = subprocess.call(cmd, shell=True);

print "=================================="
print "=        According Score         ="
print "=================================="
print "HI Precision Exactly right: %lf" % (Do_Calculation("HI_test.txt", "HI_prediction.txt", 0.25));
print "HI Precision within 1 point: %lf" % (Do_Calculation("HI_test.txt", "HI_prediction.txt", 1.25));
print "HI Precision within 2 point: %lf" % (Do_Calculation("HI_test.txt", "HI_prediction.txt",2.25));
print "HI Precision within 3 point: %lf" % (Do_Calculation("HI_test.txt", "HI_prediction.txt", 3.25));
print "==================================";
print "I Precision Exactly right: %lf" % (Do_Calculation("I_test.txt", "I_prediction.txt", 0.25));
print "I Precision within 1 point: %lf" % (Do_Calculation("I_test.txt", "I_prediction.txt", 1.25));
print "I Precision within 2 point: %lf" % (Do_Calculation("I_test.txt", "I_prediction.txt", 2.25));
print "I Precision within 3 point: %lf" % (Do_Calculation("I_test.txt", "I_prediction.txt", 3.25));
print "==================================";
print "HIS Precision Exactly right: %lf" % (Do_Calculation("HIS_test.txt", "HIS_prediction.txt", 0.25));
print "HIS Precision within 1 point: %lf" % (Do_Calculation("HIS_test.txt", "HIS_prediction.txt", 1.25));
print "HIS Precision within 2 point: %lf" % (Do_Calculation("HIS_test.txt", "HIS_prediction.txt", 2.25));
print "HIS Precision within 3 point: %lf" % (Do_Calculation("HIS_test.txt", "HIS_prediction.txt", 3.25));
print "==================================";
print "IS Precision Exactly right: %lf" % (Do_Calculation("IS_test.txt", "IS_prediction.txt", 0.25));
print "IS Precision within 1 point: %lf" % (Do_Calculation("IS_test.txt", "IS_prediction.txt", 1.25));
print "IS Precision within 2 point: %lf" % (Do_Calculation("IS_test.txt", "IS_prediction.txt", 2.25));
print "IS Precision within 3 point: %lf" % (Do_Calculation("IS_test.txt", "IS_prediction.txt", 3.25));
print "==================================";

print "\n\n\n\n";
print "=================================="
print "=        According PASS          ="
print "=================================="
[Total_precision, Correct_pass_percent, Correct_nopass_percent, Wrong_pass_percent, Wrong_nopass_percent] = Do_Pass_Calculation("HI_pass_test.txt", "HI_pass_prediction.txt");
print "HI Precision about Pass: %lf" % (Total_precision);
print "HI Percent about Correct[pass]: %lf" % (Correct_pass_percent);
print "HI Percent about Correct[no pass]: %lf" % (Correct_nopass_percent);
print "HI Percent about Wrong[origin pass]: %lf" % (Wrong_pass_percent);
print "HI Percent about Wrong[origin no pass]: %lf" % (Wrong_nopass_percent);
print "===============================================";
[Total_precision, Correct_pass_percent, Correct_nopass_percent, Wrong_pass_percent, Wrong_nopass_percent] = Do_Pass_Calculation("I_pass_test.txt", "I_pass_prediction.txt");
print "I Precision about Pass: %lf" % (Total_precision);
print "I Percent about Correct[pass]: %lf" % (Correct_pass_percent);
print "I Percent about Correct[no pass]: %lf" % (Correct_nopass_percent);
print "I Percent about Wrong[origin pass]: %lf" % (Wrong_pass_percent);
print "I Percent about Wrong[origin no pass]: %lf" % (Wrong_nopass_percent);
print "===============================================";
[Total_precision, Correct_pass_percent, Correct_nopass_percent, Wrong_pass_percent, Wrong_nopass_percent] = Do_Pass_Calculation("HIS_pass_test.txt", "HIS_pass_prediction.txt");
print "HIS Precision about Pass: %lf" % (Total_precision);
print "HIS Percent about Correct[pass]: %lf" % (Correct_pass_percent);
print "HIS Percent about Correct[no pass]: %lf" % (Correct_nopass_percent);
print "HIS Percent about Wrong[origin pass]: %lf" % (Wrong_pass_percent);
print "HIS Percent about Wrong[origin no pass]: %lf" % (Wrong_nopass_percent);
print "===============================================";
[Total_precision, Correct_pass_percent, Correct_nopass_percent, Wrong_pass_percent, Wrong_nopass_percent] = Do_Pass_Calculation("IS_pass_test.txt", "IS_pass_prediction.txt");
print "IS Precision about Pass: %lf" % (Total_precision);
print "IS Percent about Correct[pass]: %lf" % (Correct_pass_percent);
print "IS Percent about Correct[no pass]: %lf" % (Correct_nopass_percent);
print "IS Percent about Wrong[origin pass]: %lf" % (Wrong_pass_percent);
print "IS Percent about Wrong[origin no pass]: %lf" % (Wrong_nopass_percent);
print "===============================================";


