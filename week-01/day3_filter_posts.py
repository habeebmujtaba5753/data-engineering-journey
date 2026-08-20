#copy Tuesday's list in, loop through it, print only posts where views > 100
Dicts = [
    {"title": "Dictionary 1", "author": "Habeeb", "views": 100}, 
    {"title": "Dictionary 2", "author": "Habeeb1", "views": 200},
    {"title": "Dictionary 3", "author": "Habeeb2", "views": 99},
    {"title": "Dictionary 4", "author": "Habeeb3", "views": 103},
    {"title": "Dictionary 5", "author": "Habeeb4", "views": 50}
    ]
    
for Dict in Dicts:
    if(Dict["views"] > 100):
        print(Dict)