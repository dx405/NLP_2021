import json
import numpy as np
import tf_idf
import sys
from sklearn.linear_model import LinearRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder

def setup_data():

	# Label Encoder
	le = LabelEncoder()

	data = json.load(open('word_frequencies.json'))
	# set up data
	genre, words = [], []

	for i in data:
		# iterate through genres
		for genres in i[0]:
			genre.append(genres)
			words.append(list(i[1].keys()))
	
	# convert to numpy arrays
	words = np.zeros([len(words), len(max(words, key= lambda x: len(x)))])
	# array of sequence error with words
	genre = le.fit_transform(np.array(genre))

	return words, genre

def run_model(data):

	# Label Encoder
	le = LabelEncoder()

	# if data is frequency
	if data[-1] == 'frequency':

		X, Y = setup_data()

	if data[-1] == 'tf-idf':

		Y, X = tf_idf.main()

	# split into training and testing 
	x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=.20)

	# train linear regression model
	reg = LinearRegression().fit(x_train, y_train)

	# performing prediction on dataset
	y_pred = reg.predict(x_test)


	# return classification report
	print(classification_report(y_test, y_pred))


run_model(sys.argv)
