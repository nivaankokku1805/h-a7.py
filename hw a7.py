import sqlite3

database = 'basketball.sqlite'
conn = sqlite3.connect(database)

print('Opened data successfully')

import pandas as pd
tables = pd.read_sql("""SELECT *
                        FROM sqlite_master
                        WHERE type='table';""", conn)

print(tables)

team = pd.read_sql("""SELECT *
                      FROM Team;""", conn)

print(team)

season = pd.read_sql("""SELECT *
                        FROM Season;""", conn)

print(season)

rcb_matches_2015 = pd.read_sql("""SELECT Match_id,Team_2 as Away_team,Toss_winner,Match_Winner
                                FROM Match
                                WHERE Team_1 = (SELECT Team_1
                                FROM Match
                                WHERE Team_1 == 2 and Season_id ==8)""",conn)

print("Matches played by Royal Challengers Bangalore in 2015:")
print(rcb_matches_2015)

rcb_wins = pd.read_sql("""SELECT *
                                FROM Match
                                WHERE Match_Winner ==2 and Season_id ==8""",conn)

print("Matches won by Royal Challengers Bangalore as Home team in 2015:")
print(rcb_wins)



match_runs = pd.read_sql("""SELECT Match_id, runs_scored as Total_runs, innings_no  
                                FROM batsman_Scored
                                WHERE Total_runs > 5 AND Match_id IN (SELECT
                                Match_id
                                FROM Match
                                WHERE Match_Winner ==2 and Season_id ==8)""",conn)

print("Matches won by Royal Challengers Bangalore as Home team in 2015:")
print(rcb_wins)



match_runs = pd.read_sql("""SELECT Match_id, runs_scored as Total_runs, innings_no                           
                                FROM batsman_Scored
                                WHERE Total_runs > 5 AND Match_id IN (SELECT
                                Match_id
                                FROM Match
                                WHERE Season_id == 8)""",conn)


print("Matches with Scored Runs Greater Than 5 in 2015:")
print(match_runs)           
