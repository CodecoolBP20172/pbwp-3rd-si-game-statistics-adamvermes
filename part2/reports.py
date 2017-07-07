
# Report functions

# What is the title of the most played game (i.e. sold the most copies)?
# Expected name of the function: get_most_played(file_name)
# Expected output of the function: (string)
# Other expectation:  if there is more than one, then return the first from the file


def get_most_played(file_name):
    game_list = []
    games_sold_list = []
    games_sold_list_float = []
    max_list = []
    with open(file_name) as file:
        for strings in file:
            game_list.append(strings.strip().split('\t'))
        for game_title, games_sold, game_year, game_genre, game_publisher in game_list:
            games_sold_list.append(games_sold)
        for numbers in games_sold_list:
            games_sold_list_float.append(float(numbers))
            max_list = max(games_sold_list_float)
            max_list = int(max_list)
            max_list = str(max_list)
        for game_title, games_sold, game_year, game_genre, game_publisher in game_list:
            if max_list == games_sold:
                return game_title


# How many copies have been sold total?
# Expected name of the function: sum_sold(file_name)
# Expected output of the function: (number)

def sum_sold(file_name):
    game_list = []
    games_sold_list = []
    games_sold_list_float = []
    games_sold_list_total = []
    with open(file_name) as file:
        for strings in file:
            game_list.append(strings.strip().split('\t'))
        for game_title, games_sold, game_year, game_genre, game_publisher in game_list:
            games_sold_list.append(games_sold)
        for numbers in games_sold_list:
            games_sold_list_float.append(float(numbers))
        games_sold_list_total = sum(games_sold_list_float)
        return games_sold_list_total

# What is the average selling?
# Expected name of the function: get_selling_avg(file_name)
# Expected output of the function: (number)


def get_selling_avg(file_name):
    game_list = []
    games_sold_list = []
    games_sold_list_float = []
    games_sold_list_total = []
    avg = []
    with open(file_name) as file:
        for strings in file:
            game_list.append(strings.strip().split('\t'))
        for game_title, games_sold, game_year, game_genre, game_publisher in game_list:
            games_sold_list.append(games_sold)
        for numbers in games_sold_list:
            games_sold_list_float.append(float(numbers))
        games_sold_list_total = sum(games_sold_list_float)
        avg = games_sold_list_total / len(game_list)
        return avg


# How many characters long is the longest title?
# Expected name of the function: count_longest_title(file_name)
# Expected output of the function: (number)


def count_longest_title(file_name):
    game_list = []
    games_len_list = []
    games_lengths = []
    games_lengths_max = []
    with open(file_name) as file:
        for strings in file:
            game_list.append(strings.strip().split('\t'))
        for game_title, games_sold, game_year, game_genre, game_publisher in game_list:
            games_len_list.append(game_title)
        for titles in games_len_list:
            games_lengths.append(len(titles))
            games_lengths_max = max(games_lengths)
        return games_lengths_max


# What is the average of the release dates?
# Expected name of the function: get_date_avg(file_name)
# Expected output of the function: average year (number)
# Other expectation: the return value must be the rounded up average

def get_date_avg(file_name):
    