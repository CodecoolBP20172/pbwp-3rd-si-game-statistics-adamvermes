
# Printing functions

from reports import count_games
from reports import decide
from reports import get_latest
print(count_games('game_stat.txt'))
print(decide('game_stat.txt', 1998))
print(get_latest('game_stat.txt'))
