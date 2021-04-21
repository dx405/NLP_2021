import json


in_file = open("booksummaries.txt",'r',encoding='utf-8')
corpus = in_file.read()
summaries = corpus.split("\n")

summaries_lists = []
for summary in summaries:
    summary_list = summary.split("\t")
    summaries_lists.append(summary_list)

data = []
for summary in summaries_lists:
    if(len(summary)!=7):
        continue
    summary_dict = {}
    summary_dict["title"] = summary[2]
    summary_dict["author"] = summary[3]
    summary_dict["genres"] = []
    if(summary[5] == ""):
        continue
    genre_dict = eval(summary[5])
    for key,value in genre_dict.items():
        summary_dict["genres"].append(value)
    summary_dict["summary"] = summary[6]
    data.append(summary_dict)

j = json.dumps(data)
with open("data.json",'w') as f:
    f.write(j)
    f.close()
        
    
    


