import sqlite3
import pandas as pd
import os

# Used pandas instead of actually writing Table by table in sql to save writing lines of codes for manually entering the tables
# Instead used pandas to just read in the csv file and make a table for each compnent

# Create a combined database for the server to conect to
conn = sqlite3.connect("../data/worldcup.db")

# Read each CSV and store as a table 
df1 = pd.read_csv('/Users/taahaar/Documents/GitHub/PitchQuery/data/WorldCups.csv')
df1.to_sql("world_cups", conn, if_exists= "replace", index = False)
print("Loaded WorldCups")

df2 = pd.read_csv('/Users/taahaar/Documents/GitHub/PitchQuery/data/WorldCupPlayers.csv')
df2.to_sql("WC_players", conn, if_exists= "replace", index= False)
print("Loaded WCplayers")

df3 = pd.read_csv('/Users/taahaar/Documents/GitHub/PitchQuery/data/WorldCupMatches.csv')
df3.to_sql("WC_matches", conn, if_exists = "replace", index = False)
print("Loaded WCmatches")

df4 = pd.read_csv('/Users/taahaar/Documents/GitHub/PitchQuery/data/WorldCupGoals.csv', encoding="latin-1") # for special characters
df4.to_sql("WC_goals", conn, if_exists= "replace", index = False)
print("Loaded WCgoals")

conn.close()




