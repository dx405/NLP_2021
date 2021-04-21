import json
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re
lemmatizer = WordNetLemmatizer()
other_stopwords = ["one", "two", "also", "novel", "story", "life","find", "new", "home","book",
                     "first", "man","woman", "back", "day", "time", "father","take","away","old", 
                     "return", "see", "tell", "begin", "god", "go", "death", "ship","young",
                     "make", "family", "end", "come", "human", "world", "escape", "try", "becomes",
                     "later", "friend", "would", "love", "people", "work",
                     "attempt", "meet", "however", "help", "way", "year", "men",
                     "another", "become", "next", "son", "three", "give", "house",
                     "set", "attack", "town", "name", "kill", "order", "call", "turn",
                     "must", "even", "child", "plan", "get", "use",
                     "leave", "n't", "place"]
data = json.load(open("data.json"))

tokens_list = []
word_count = {}
for summary in data:
    tokens = word_tokenize(summary["summary"])
    clean_tokens = []
    for token in tokens:
        lemma = lemmatizer.lemmatize(token)
        if token[0].isupper():
            continue
        if token.lower() in stopwords.words('english'):
            continue
        if lemma.lower() in other_stopwords:
            continue
        if bool(re.match(r"[.,()?!\"\'-;'&]|``",token)):
            continue
        clean_tokens.append(lemma)
    tokens_list.append(clean_tokens)
    for token in clean_tokens:
        if token in word_count:
            word_count[token] += 1
        else:
            word_count[token] = 1

word_list = []
for key,value in word_count.items():
    word_list.append([key, value])

def sortfunc(x):
    return x[1]

word_list.sort(reverse = True, key=sortfunc)

top_words = [word[0] for word in word_list[:100]]


bags = []
for i in range(len(tokens_list)):
    tokens = tokens_list[i]
    bag = {}
    for token in tokens:
        if token not in top_words:
            continue
        if token in bag:
            bag[token] += 1
        else:
            bag[token] = 1

    bags.append([data[i]["genres"],bag])

j = json.dumps(bags)
with open("word_frequencies.json",'w') as f:
    f.write(j)
    f.close()

for word in top_words:
    print(word + " " + str(word_count[word]))
        


