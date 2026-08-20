#turn Wednesday's filter logic into a function filter_by_views(posts, min_views) that returns the filtered list
Dicts = [
    {"title": "Dictionary 1", "author": "Habeeb", "views": 100}, 
    {"title": "Dictionary 2", "author": "Habeeb1", "views": 200},
    {"title": "Dictionary 3", "author": "Habeeb2", "views": 99},
    {"title": "Dictionary 4", "author": "Habeeb3", "views": 103},
    {"title": "Dictionary 5", "author": "Habeeb4", "views": 50}
    ]
    
def filter_by_views(posts, min_views):
    result = []
    for post in posts:
        if(post["views"] > min_views):
            result.append(post)
    return result

filtered = filter_by_views(Dicts, 100)
#print(filtered)
for post in filtered:
    print(post)