import json

genres_file = open("genres.txt", 'r', encoding="latin")
genres = genres_file.read()

genre_list = genres.split("\n\n")

genre_dict = {}
for broad_genre in genre_list:
    broad_genre_list = broad_genre.split("\n")
    broad_genre_name = broad_genre_list[0]
    genres = broad_genre_list[1:len(broad_genre)]
    genre_dict[broad_genre_name] = genres

reverse_dict = {}

for key, value in genre_dict.items():
    for genre in value:
        reverse_dict[genre.strip()] = key


j = json.dumps(reverse_dict)
with open("genre_dict.json",'w', encoding= "latin") as f:
    f.write(j)
    f.close()    
