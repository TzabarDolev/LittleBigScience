import json

"this file is for the creation of the json file"
dict = {}
time = '14:02'
songs_dir = r"music"
dict['time'] = time
dict['songs_dir'] = songs_dir

with open('data.json', 'w') as fp:
    json.dump(dict, fp)

