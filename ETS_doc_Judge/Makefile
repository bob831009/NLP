all:
	make fetch_train fetch_test

fetch_train:
	python fetch_data.py 6000 > ETS_train.txt

fetch_test:
	python fetch_data.py 1000 > ETS_test.txt

clean:
	rm ETS_*.txt

run:
	python predict_Ensemble.py