import json


in_file = open("booksummaries.txt",'r',encoding='latin')
genre_map = json.load(open("genre_dict.json"))

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
        if value == "Roman à clef":
            value = "clef"
        elif value == "Künstlerroman":
            value = "Kunstlerroman"
        if genre_map[value] not in summary_dict["genres"]:
            summary_dict["genres"].append(genre_map[value])
    summary_dict["summary"] = summary[6]
    data.append(summary_dict)

j = json.dumps(data)
with open("data.json",'w', encoding= 'latin') as f:
    f.write(j)
    f.close()
        
    
    


