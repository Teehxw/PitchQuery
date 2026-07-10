import sqlite3

DB_PATH = '/Users/taahaar/Documents/GitHub/PitchQuery/data/worldcup.db' # the path to the db file

# Extract the table and column names from the database
def fetch_schema():

    # Connect to the database
    conn = sqlite3.connect(DB_PATH)
    curr = conn.cursor()    #cursor is the object used to run SQL commands

    # fetch all the tables in the database
    tables = curr.execute(
        "SELECT name FROM sqlite_master WHERE type ='table'"    #sqlite_master is a special internal SQLite table that stores all database information 
    ).fetchall()


    schema = "" #empty string where the schema will be built
    for table in tables:    # Loop through all the tables
        table_name = table[0]   # each table is stored in a tuple so we have to extract the first element

        cols = curr.execute(f"PRAGMA table_info({table_name})").fetchall()  # PRAGMA is a SQLite command that tells you the column names, types and other information. Returns a tuple
        col_names = ', '.join(col[1] for col in cols)   # This builds a string of column names. col[1] gets the column name from the tuple and join 
        
        # Build the schema 
        schema += f"Table {table_name}: ({col_names}) \n"

    conn.close()
    return schema   # Gets sent to Claude

# Runs the sql query from Claude against the database
def run_query(sql_str):
    # Connect to the database again
    conn = sqlite3.connect(DB_PATH)
    curr = conn.cursor()

    # Check for errors. If an error raise an exception 
    try:
        curr.execute(sql_str)   #execute the string
        columns = [column_info[0] for column_info in curr.description]  #gets the names of the columns returned by the query. Description holds information about the columns that are resulted by the SQL query
        rows = curr.fetchall()  # gets all result rows 

        conn.close()
        return {"columns": columns, "rows": rows}   # Returns the columns and rows (like a dictionary)
    except Exception as e:
        conn.close()
        return {"error": str(e)}
