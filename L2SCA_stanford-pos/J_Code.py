#!/usr/bin/python
#coding=utf-8
from sklearn.svm import SVC
from sklearn.svm import NuSVC
#from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import ShuffleSplit
from sklearn.cross_validation import cross_val_score
from sklearn.grid_search import GridSearchCV
import MySQLdb
import numpy as np

#db connect
db = MySQLdb.connect(host="mysql", user="jjery2243542", passwd="fZmhdf7bp5OeDvs1NBPt8JaG5PEgpXQY", db="orina1123")
cursor = db.cursor()
sql = "SELECT * FROM HIS_document_LCA"
cursor.execute(sql)
data = [list(x)[2:] for x in cursor.fetchall()]
for i in range(2, 5):
    sql = "SELECT COUNT(id) FROM HIS_ngram WHERE len=" + str(i) + " GROUP BY document_id"
    cursor.execute(sql)
    total_num = cursor.fetchall()
    sql = "SELECT COUNT(id) FROM HIS_ngram WHERE len=" + str(i) + " AND `coca-n_cnt` > 0 GROUP BY document_id"
    cursor.execute(sql)
    coca_num = cursor.fetchall()
    for idx in range(len(coca_num)):
        data[idx].append(float(coca_num[idx][0]) / total_num[idx][0]) 
data = np.array(data)
sql = "SELECT score FROM HIS_document"
cursor.execute(sql)
score = np.array([int(x[0]) for x in cursor.fetchall()])
svc_params = {
    'C':np.logspace(-1, 2, 8),
    'gamma':np.logspace(-4, 0, 10),
}
#完全正確率
gs_svc = GridSearchCV(SVC(), svc_params, cv=5)
gs_svc.fit(data, score)
print gs_svc.best_params_, gs_svc.best_score_

#差一分算對
svc = SVC(kernel='rbf', C=10, gamma=0.0001)
cv = ShuffleSplit(len(data), n_iter=10, test_size=0.1, random_state=0)
test_scores = cross_val_score(svc, data, score, cv=cv, n_jobs=2)
print max(test_scores)

#過與不過
gs_svc = GridSearchCV(SVC(), svc_params, cv=10)
gs_svc.fit(data, np.array([1 if x >=4 else 0 for x in score]))
print gs_svc.best_params_, gs_svc.best_score_