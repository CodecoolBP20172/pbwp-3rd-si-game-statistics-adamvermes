def count_games(file_name):
    with open(file_name, 'r') as file:
        game_list = []
        for strings in file:
            game_list.append(strings.strip().split('\t'))
        return len(game_list)


def decide(file_name, year):
    with open(file_name, 'r') as file:
        game_list = []
        game_year_list = []
        for strings in file:
            game_list.append(strings.strip().split('\t'))
        for game_title, sold, game_year, game_genre, publisher in game_list:
            game_year_list.append(game_year)
        if str(year) in game_year_list:
            return True
        else:
            return False


def get_latest(file_name):
    game_list = []
    year_list = []
    latest_year = []
    with open(file_name) as file:
        for strings in file:
            game_list.append(strings.strip().split('\t'))
        for game_title, sold, game_year, game_genre, publisher in game_list:
            year_list.append(int(game_year))
            year_list.sort(reverse=True)
            latest_year = str(year_list[0])
        for title, sold, year, genre, publisher in game_list:
            if latest_year == year:
                return title


def count_by_genre(file_name, genre):
    game_list = []
    genre_list = []
    with open(file_name) as file:
        for strings in file:
            game_list.append(strings.strip().split('\t'))
        for game_title, sold, game_year, game_genre, publisher in game_list:
            genre_list.append(game_genre)
        return genre_list.count(genre)


def get_line_number_by_title(file_name, title):
    game_list = []
    game_title_list = []
    with open(file_name) as file:
        for strings in file:
            game_list.append(strings.strip().split('\t'))
        for game_title, sold, year, game_genre, publisher in game_list:
            game_title_list.append(game_title)
        while True:
            try:
                if title in game_title_list:
                    line = game_title_list.index(title) + 1
                    return line
                else:
                    raise ValueError
            except ValueError:
                print('Title not in list')
                break
