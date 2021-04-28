import json
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

def main():

	stopwords = ["one", "two", "also", "novel", "story", "life","find", "new", "home","book",
                     "first", "man","woman", "back", "day", "time", "father","take","away","old", 
                     "return", "see", "tell", "begin", "god", "go", "death", "ship","young",
                     "make", "family", "end", "come", "human", "world", "escape", "try", "becomes",
                     "later", "friend", "would", "love", "people", "work",
                     "attempt", "meet", "however", "help", "way", "year", "men",
                     "another", "become", "next", "son", "three", "give", "house",
                     "set", "attack", "town", "name", "kill", "order", "call", "turn",
                     "must", "even", "child", "plan", "get", "use",
                     "leave", "n't", "place"]

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
				summ = [x for x in i['summary'].split() if x not in stopwords]
				summ = ' '.join(summ)
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






