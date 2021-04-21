import json
from nltk import word_tokenize
from nltk.corpus import stopwords
data = json.load(open("data.json"))

bags = []
for summary in data:
    tokens = word_tokenize(summary["summary"])
    bag = {}
    for token in tokens:
        if token.lower() in stopwords.words('english'):
            continue
        if token in bag:
            bag[token] += 1
        else:
            bag[token] = 1

    print(summary["title"])
    bags.append([summary["genres"],bag])

j = json.dumps(bags)
with open("word_frequencies.json",'w') as f:
    f.write(j)
    f.close()
        


