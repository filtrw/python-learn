"""
Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и
выводит на стандартный вывод сводную таблицу результатов всех матчей.

За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

Формат ввода следующий:
В первой строке указано целое число n — количество завершенных игр.
После этого идет nn строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой

Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков
Конкретный пример ввода-вывода приведён ниже.
Порядок вывода команд произвольный.

Sample Input:
3
Спартак;9;Зенит;10
Локомотив;12;Зенит;3
Спартак;8;Локомотив;15


Sample Output:
Спартак:2 0 0 2 0
Зенит:2 1 0 1 3
Локомотив:2 2 0 0 6
"""

game_number = int(input())
games = []
team_names = []
team_results = []

for game in range(game_number):
    games.append([some_value for some_value in input().split(";")])
    if games[game][0] not in team_names:
        team_names.append(games[game][0])
        team_results.append([games[game][0], 0, 0, 0, 0, 0])

    if games[game][2] not in team_names:
        team_names.append(games[game][2])
        team_results.append([games[game][2], 0, 0, 0, 0, 0])
    second_team_index = team_names.index(games[game][2])
    first_team_index = team_names.index(games[game][0])

    """update summary table with all results"""
    """game"""
    team_results[first_team_index][1] += 1
    team_results[second_team_index][1] += 1
    """defeat"""
    if int(games[game][1]) == int(games[game][3]):
        team_results[first_team_index][3] += 1
        team_results[first_team_index][5] += 1
        team_results[second_team_index][3] += 1
        team_results[second_team_index][5] += 1
        """win and draw and score"""
    elif int(games[game][1]) > int(games[game][3]):
        team_results[first_team_index][2] += 1
        team_results[first_team_index][5] += 3
        team_results[second_team_index][4] += 1
    else:
        team_results[second_team_index][2] += 1
        team_results[second_team_index][5] += 3
        team_results[first_team_index][4] += 1

for team in range(len(team_results)):
    print(team_results[team][0], end=":")
    for position in range(1, len(team_results[team])):
        print(team_results[team][position], end=" ")
    print()
