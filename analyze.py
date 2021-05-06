from collections import Counter
import matplotlib.pyplot as plt
import re
import pandas as pd

with open('label_results.txt', 'r') as f:
	data = f.readlines()

full, partial, no = 0, 0,0

for i in data:
	i = i.split('\t')
	pred = i[0].split(':')[-1]
	actual = i[1].split(':')[-1]

	# clean predicted values
	pred = pred.split(',')
	pred = [re.sub("[^A-Za-z ]", "", x) for x in pred]

	# clean actual values
	actual = actual.split(',')
	actual = [re.sub("[^A-Za-z ]", "", x) for x in actual]

	if pred == actual:
		full += 1

	else:

		for i in pred:
			if i in actual and len(i) > 1:
				partial += 1
				break
			else:
				no += 1
				break

print(f'Full match: {full} \t Partial match: {partial} \t No match: {no}')
