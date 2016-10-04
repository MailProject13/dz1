import random

import pandas as pd


def add_teams():
    teams_list = list()
    
    new_team = input('Введите название команды: ')    
    while new_team != '':
        teams_list.append(new_team)
        new_team = input('Введите название команды: ')
        
    return teams_list


def match_table_form(teams_list):
    match_table = pd.DataFrame(columns=teams_list)
    
    for name in teams_list:
        match_table.loc[name] = [random.randint(0,10) for i in range(len(teams_list))]
        match_table.loc[name][name] = 0
    
    return match_table


def result_table_form(match_table):
    columns = ['Место', 'Побед', 'Поражений', 'Ничьи', 'Голы', 'Пропущено', 'Очки']
    teams_list = match_table.index.values
    comp_table = pd.DataFrame(columns=columns, index=teams_list)
    comp_table = comp_table.fillna(0)
    
    for i in range(len(teams_list)):
        team1 = teams_list[i]
        
        for j in range(i+1, len(teams_list)):
            team2 = teams_list[j]
            
            comp_table.loc[team1]['Голы'] += match_table.loc[team1][team2]
            comp_table.loc[team1]['Пропущено'] += match_table.loc[team2][team1]
            
            comp_table.loc[team2]['Голы'] += match_table.loc[team2][team1]
            comp_table.loc[team2]['Пропущено'] += match_table.loc[team1][team2]
            
            if match_table.loc[team1][team2] > match_table.loc[team2][team1]:
                comp_table.loc[team1]['Побед'] += 1
                comp_table.loc[team1]['Очки'] += 3                
                comp_table.loc[team2]['Поражений'] += 1
                
            elif match_table.loc[team1][team2] == match_table.loc[team2][team1]:
                comp_table.loc[team1]['Ничьи'] += 1
                comp_table.loc[team1]['Очки'] += 1
                comp_table.loc[team2]['Ничьи'] += 1
                comp_table.loc[team2]['Очки'] += 1
                
            else:
                comp_table.loc[team2]['Побед'] += 1
                comp_table.loc[team2]['Очки'] += 3                
                comp_table.loc[team1]['Поражений'] += 1
            
    comp_table.sort_values('Очки', ascending=False, inplace=True)
    
    prev_team_score = 0
    pos = 0

    for name in comp_table.index.values:
        if prev_team_score != comp_table.loc[name]['Очки']:
            pos += 1

        comp_table.loc[name]['Место'] = pos
        prev_team_score = comp_table.loc[name]['Очки']
    
    return comp_table


def get_match_res(team1, team2):
    team1_score = match_table.loc[team1][team2]
    team2_score = match_table.loc[team2][team1]
    
    return ":".join([str(team1_score), str(team2_score)])


def main():
    teams_list = add_teams()
    match_table = match_table_form(teams_list)
    comp_table = result_table_form(match_table)
    
    print comp_table
    

main()
