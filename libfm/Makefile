all:
	make fetch_train fetch_valid fetch_test fetch_train_pass fetch_valid_pass fetch_test_pass
create_file:
	mkdir HIS IS HI I
remove:
	rm -f *.txt
	rm -r ./HIS/ ./IS/ ./HI/ ./I/
orangize:
	mv HIS_*.txt ./HIS/
	mv IS_*.txt ./IS/
	mv HI_*.txt ./HI/
	mv I_*.txt ./I/
fetch_train:
	python fetch_data.py HIS 100 > HIS_feature_train.txt
	python fetch_data.py IS 100 > IS_feature_train.txt
	python fetch_data.py HI 100 > HI_feature_train.txt
	python fetch_data.py I 100 > I_feature_train.txt
fetch_valid:
	python fetch_data.py HIS 20 > HIS_feature_val.txt
	python fetch_data.py IS 20 > IS_feature_val.txt
	python fetch_data.py HI 20 > HI_feature_val.txt
	python fetch_data.py I 20 > I_feature_val.txt
fetch_test:
	python fetch_data.py HIS 50 > HIS_test.txt
	python fetch_data.py IS 50 > IS_test.txt
	python fetch_data.py HI 50 > HI_test.txt
	python fetch_data.py I 50 > I_test.txt
fetch_train_pass:
	python fetch_data_pass.py HIS 100 > HIS_pass_feature_train.txt
	python fetch_data_pass.py IS 100 > IS_pass_feature_train.txt
	python fetch_data_pass.py HI 100 > HI_pass_feature_train.txt
	python fetch_data_pass.py I 100 > I_pass_feature_train.txt
fetch_valid_pass:
	python fetch_data_pass.py HIS 20 > HIS_pass_feature_val.txt
	python fetch_data_pass.py IS 20 > IS_pass_feature_val.txt
	python fetch_data_pass.py HI 20 > HI_pass_feature_val.txt
	python fetch_data_pass.py I 20 > I_pass_feature_val.txt
fetch_test_pass:
	python fetch_data_pass.py HIS 50 > HIS_pass_test.txt
	python fetch_data_pass.py IS 50 > IS_pass_test.txt
	python fetch_data_pass.py HI 50 > HI_pass_test.txt
	python fetch_data_pass.py I 50 > I_pass_test.txt