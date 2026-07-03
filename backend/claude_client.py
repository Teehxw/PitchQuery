import anthropic
from dotenv import load_dotenv
import os

# Load the API key from an environment variable
load_dotenv()
client = anthropic.Anthropic(api_key = os.getenv("ANTHROPIC_API_KEY"))

# rememer the conversation
#conversation =[]

# while True:
#     user_message = input("User: ")

#     if user_message.lower() == "exit":
#         print("Chat ended. Goodbye!")
#         break

#     # Add user message to the conversation
#     conversation.append({"role": "user", "content": user_message})

#     response = client.messages.create(
#        model = "claude-sonnet-4-6",
#        max_tokens= 1024,
#        messages = conversation
#    )

#     bot_message = response.content[0].text
#     print(f"Claude: {bot_message}")

#     # Add Chatbots response to the conversation
#     conversation.append({"role": "assistant", "content": bot_message})


def generate_sql(prompt, schema):

    response = client.messages.create(
        model = "claude-sonnet-4-6",
        max_tokens = 1024,
        system = f"""You are a SQL expert working with a SQLite database.
        IMPORTANT: Only use SQLite-compatible functions and syntax.
        Do NOT use MySQL functions like SUBSTRING_INDEX, GROUP_CONCAT with SEPARATOR, or any non-SQLite syntax.
        Return only the SQL query, no explanations.

        The database schema is:
        {schema}""",
        messages = [{"role": "user", "content": prompt}]
    )

    sql_query = response.content[0].text
    sql_query = sql_query.replace("```sql", "").replace("```", "").strip()
    return sql_query
    
    





