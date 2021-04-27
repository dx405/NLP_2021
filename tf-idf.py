import json
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

# import cleaned data
with open('data.json', 'r') as file:
	file = json.load(file)

	# extract the genres and summaries
	for i in file:
		print(i)

