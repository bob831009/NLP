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
	python fetch_data.py HIS 300 > HIS_feature_train.txt
	python fetch_data.py IS 300 > IS_feature_train.txt
	python fetch_data.py HI 300 > HI_feature_train.txt
	python fetch_data.py I 300 > I_feature_train.txt
fetch_valid:
	python fetch_data.py HIS 100 > HIS_feature_val.txt
	python fetch_data.py IS 100 > IS_feature_val.txt
	python fetch_data.py HI 100 > HI_feature_val.txt
	python fetch_data.py I 100 > I_feature_val.txt
fetch_test:
	python fetch_data.py HIS 150 > HIS_test.txt
	python fetch_data.py IS 150 > IS_test.txt
	python fetch_data.py HI 150 > HI_test.txt
	python fetch_data.py I 150 > I_test.txt
fetch_train_pass:
	python fetch_data_pass.py HIS 300 > HIS_pass_feature_train.txt
	python fetch_data_pass.py IS 300 > IS_pass_feature_train.txt
	python fetch_data_pass.py HI 300 > HI_pass_feature_train.txt
	python fetch_data_pass.py I 300 > I_pass_feature_train.txt
fetch_valid_pass:
	python fetch_data_pass.py HIS 100 > HIS_pass_feature_val.txt
	python fetch_data_pass.py IS 100 > IS_pass_feature_val.txt
	python fetch_data_pass.py HI 100 > HI_pass_feature_val.txt
	python fetch_data_pass.py I 100 > I_pass_feature_val.txt
fetch_test_pass:
	python fetch_data_pass.py HIS 150 > HIS_pass_test.txt
	python fetch_data_pass.py IS 150 > IS_pass_test.txt
	python fetch_data_pass.py HI 150 > HI_pass_test.txt
	python fetch_data_pass.py I 150 > I_pass_test.txt