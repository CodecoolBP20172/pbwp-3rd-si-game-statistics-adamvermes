# Export functions
import reports

with open('export.txt', 'w') as export_file:
    export_file.write(str(reports.count_games('game_stat.txt')) + '\n')
    export_file.write(str(reports.decide('game_stat.txt', 1998)) + '\n')
    export_file.write(str(reports.get_latest('game_stat.txt')) + '\n')
    export_file.write(str(reports.count_by_genre('game_stat.txt', 'RPG')) + '\n')
    export_file.write(str(reports.get_line_number_by_title('game_stat.txt', 'Minecraft')) + '\n')
