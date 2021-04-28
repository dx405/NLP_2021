import json
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

def td_idf():
	# label encoder
	le = LabelEncoder()

	# import cleaned data
	with open('data.json', 'r') as file:
		file = json.load(file)

		# label encode the genre types
		types = []
		summaries = []
		for i in file:
			
			# organize for multiple genres
			for j in i['genres']:
				
				types.append(j)
				summaries.append(i['summary'])


	# map genres to label encoding
	types = list(types)
	types_encoded = le.fit_transform(np.array(types))
	# return type print(types[num])

	# count occurences of words per summary
	count_vect = CountVectorizer()
	x_counts = count_vect.fit_transform(summaries)

	# find term frequencies
	tf_transform = TfidfTransformer().fit(x_counts)
	x_tf = tf_transform.transform(x_counts)

	# return label and data
	return types_encoded, x_tf






