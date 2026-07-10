# Import the libraries
import anthropic
from dotenv import load_dotenv   # library used to import variables from a .env file
import os

# load_dotenv('/Users/taahaar/Documents/GitHub/PitchQuery/backend/.env')
# print("KEY:", os.getenv("ANTHROPIC_API_KEY"))

# Load the API key from an environment variable
# load_dotenv('/Users/taahaar/Documents/GitHub/PitchQuery/backend/.env')

# Load the API KEY and creates the Claude client (harcoded since .env file is experiencing reading issues)
client = anthropic.Anthropic(api_key="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")


# Function that takes the users prompt and scheme from the datasets and converts it into SQL
def generate_sql(prompt, schema):

    # Senf message to Claude and store its response
    response = client.messages.create(
        model = "claude-sonnet-4-6",
        max_tokens = 1024,  # how long a response should be

        # the system prompt. This tells the Claude client on how to behave and what do  
        system = f"""You are a SQL expert working with a SQLite database.
        IMPORTANT: Only use SQLite-compatible functions and syntax.
        Do NOT use MySQL functions like SUBSTRING_INDEX, GROUP_CONCAT with SEPARATOR, or any non-SQLite syntax.
        Return only the SQL query, no explanations.

        The database schema is:
        {schema}""",    # the schema that will be attached with the prompt

        messages = [{"role": "user", "content": prompt}]    # sends the user question to Claude
    )

    # Extract SQL from the Claude's Response
    sql_query = response.content[0].text
    sql_query = sql_query.replace("```sql", "").replace("```", "").strip()   #removes extra spaces and markdown code fences 
    return sql_query
    
    

#.  -----------------------PRACTICE CODE----------------------------
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