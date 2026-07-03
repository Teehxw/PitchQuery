import sqlite3

DB_PATH = '/Users/taahaar/Documents/GitHub/PitchQuery/data/worldcup.db'

def fetch_schema():

    conn = sqlite3.connect(DB_PATH)
    curr = conn.cursor()

    
    tables = curr.execute(
        "SELECT name FROM sqlite_master WHERE type ='table'"
    ).fetchall()

    schema = ""
    for table in tables:
        table_name = table[0]
        cols = curr.execute(f"PRAGMA table_info({table_name})").fetchall()
        col_names = ', '.join(col[1] for col in cols)
        schema += f"Table {table_name}: ({col_names}) \n"

    conn.close()
    return schema


def run_query(sql_str):
    conn = sqlite3.connect(DB_PATH)
    curr = conn.cursor()
    try:
        curr.execute(sql_str)
        columns = [description[0] for description in curr.description]
        rows = curr.fetchall()

        conn.close()
        return {"columns": columns, "rows": rows}
    except Exception as e:
        conn.close()
        return {"error": str(e)}
