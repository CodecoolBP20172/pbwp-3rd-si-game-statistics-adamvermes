
# Printing functions


from reports import count_games
from reports import decide
from reports import get_latest
from reports import count_by_genre
from reports import get_line_number_by_title

print(count_games('game_stat.txt'))
print(decide('game_stat.txt', 1998))
print(get_latest('game_stat.txt'))
print(count_by_genre('game_stat.txt', 'RPG'))
print(get_line_number_by_title('game_stat.txt', 'Minecraft'))