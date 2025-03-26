# Write your solution here
def find_movies(database: list, search_term: str):

    my_list = []

    for movie in database:
        if search_term.lower() in movie["name"].lower():
            my_list.append(movie)

    return my_list
