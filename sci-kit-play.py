import sqlite3;
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB


#basic sqlite query code from a tutorial
conn = sqlite3.connect("mental_health.sqlite");

c = conn.cursor()

data = [];

c.execute("SELECT * FROM Answer")

curID = -1;

for row in c.execute("SELECT * FROM Answer ORDER BY userID"):
	
	if curID != row[2] : 
		data.append([curID])
		curID = row[2]
		for i in range(1,120):
			data[curID-1].append(-1); 
		
	data[curID-1][row[3]] = hash(row[0])
		

#make an array of answers we want to train against. 

answers = []

updatedata = []
for i, row in enumerate(data):
	if row[115] != -1:
		updatedata.append(row)
	


for row in updatedata:
	answers.append(row[115])
	row.remove(row[115])
	#for i, answer in enumerate(row):
	#	print (i , ' :', answer)

print (answers)

X = updatedata
Y = answers

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.5, random_state=0)
clf = GaussianNB()
results = clf.fit(X_train, Y_train).predict(X_test)
print("Number of mislabeled points out of a total %d points : %d" % (len(X_test), (Y_test != results).sum()))


	
	

