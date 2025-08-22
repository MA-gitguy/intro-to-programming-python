## IMPORTS GO HERE

## END OF IMPORTS

### YOUR CODE FOR get_types_counts() FUNCTION GOES HERE ###
from ast import While


def get_types_counts(x):
    types = get_types(x)
    types_count_dict = {}
    for type in types:
        types_count_dict[type] = len(x[type])

    return types_count_dict
#### End OF MARKER


### YOUR CODE FOR get_types() FUNCTION GOES HERE ###
def get_types(x):
    return list(x.keys())
#### End OF MARKER


### YOUR CODE FOR get_author_count() FUNCTION GOES HERE ###
def get_author_count(x, auth_name, meta_data=[]):
    author_count = 0
    if not meta_data:
        meta_data = get_types(x)
    # for item in meta_data.items():
    for i in meta_data:
        for j in x[i]:
            if j["author"]["username"] == auth_name:
                author_count += 1

    return author_count
#### End OF MARKER





if __name__ == '__main__':
    d = {
            "articles": [{
                "slug": "how-to-train-your-mule",
                "title": "How to train your mule",
                "description": "Ever wonder how?",
                "body": "It takes a Jacobian",
                "tagList": ["mules", "training"],
                "createdAt": "2016-02-18T03:22:56.637Z",
                "updatedAt": "2016-02-18T03:48:35.824Z",
                "favoritesCount": 0,
                "author": {
                  "username": "jake",
                  "bio": "I work at statefarm",
                  "following": False
                }
            }, {
                "slug": "and another article",
                "body": "I'm getting bored",
                "tagList": ["bored", "article"],
                "createdAt": "2016-02-18T03:22:56.637Z",
                "updatedAt": "2016-02-18T03:48:35.824Z",
                "favoritesCount": 20,
                "author": {
                  "username": "cap",
                  "following": True
                }
            }],
            "tweets": [{
                "body": "See my article on training mules.",
                "author": {
                  "username": "jake"
                }
            }]
        }

    print(get_types(d))
    print(get_types_counts(d))
    print(get_author_count(d, 'cap'))
    print(get_author_count(d, 'jake', ['articles', 'tweets']))
