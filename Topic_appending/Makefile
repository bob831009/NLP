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

fetch_data:
	python fetch_data.py HIS 400
	python fetch_data.py IS 400
	python fetch_data.py HI 400
	python fetch_data.py I 400

fetch_data_pass:
	python fetch_data_pass.py HIS 400
	python fetch_data_pass.py IS 400
	python fetch_data_pass.py HI 400
	python fetch_data_pass.py I 400