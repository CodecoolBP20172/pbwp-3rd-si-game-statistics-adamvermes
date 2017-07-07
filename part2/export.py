import reports

with open('export.txt', 'w') as export_file:
    export_file.write(str(reports.get_most_played('game_stat.txt')) + '\n')
    export_file.write(str(reports.sum_sold('game_stat.txt')) + '\n')
    export_file.write(str(reports.get_selling_avg('game_stat.txt')) + '\n')
    export_file.write(str(reports.get_date_avg('game_stat.txt')) + '\n')
    export_file.write(str(reports.get_game('game_stat.txt', 'Counter-Strike')) + '\n')