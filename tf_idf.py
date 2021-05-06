import json
import numpy as np
from sklearn.preprocessing import LabelEncoder, MultiLabelBinarizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

def main():

	# label encoder
	le = LabelEncoder()

	# multilabel
	mlb = MultiLabelBinarizer()

	# import cleaned data
	with open('data.json', 'r') as file:
		file = json.load(file)

		# label encode the genre types
		types = []
		summaries = []
		for i in file:
			
			# organize for multiple genres
			types.append(i['genres'])
			summaries.append(i['summary'])

	# map genres to label encoding
	types_encoded = mlb.fit_transform(types)
	# return type print(types[num])

	# count occurences of words per summary
	count_vect = CountVectorizer()
	x_counts = count_vect.fit_transform(summaries)

	# find term frequencies
	tf_transform = TfidfTransformer().fit(x_counts)
	x_tf = tf_transform.transform(x_counts)

	# return label and data
	return types_encoded, x_tf, mlb






