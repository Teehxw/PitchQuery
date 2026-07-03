import db
import claude_client


prompt = ["Which country has won the most World Cups?","Who scored the most goals in World Cup history?","List the top 5 players with the most appearances in World Cup matches.","What is the average number of goals scored per match in World Cup history?","Which player has the highest goal-to-game ratio in World Cup history?","List all the World Cup winners along with the year they won.","Who was the top scorer in the 2018 World Cup?","Which country has hosted the most World Cups?","What is the total number of goals scored in all World Cup tournaments combined?","List all players who have scored hat-tricks in World Cup history."]

schema = db.fetch_schema()

for q in prompt:
    print(f"Prompt: {q}")
    sql_query = claude_client.generate_sql(q, schema)
    print(f"Generated SQL Query: {sql_query}")
    execution_result = db.run_query(sql_query)
    print(f"Execution Result: {execution_result}")
# sql_query = claude_client.generate_sql(prompt, schema)

# print(f"Generated SQL Query: {sql_query}")

# execution_result = db.run_query(sql_query)

# print(f"Execution Result: {execution_result}")