# DBConnect
A Small DataBase connection wrapper for Pandas

## DBConnect is a small wrapper for ease of using SQL and Pandas.

Here are some simple steps to start using the library.

1. Load library
from dbconnect.connect import SqlConnect

2. Create a sql instance with all the input parameters
driver = "driver_name" e.g "SQL SERVER"
server = "server_name" e.g "123.65.9"
database = "db_name" 

db = SqlConnect(driver, server, database)

2. Read from Table:
 
query = "SELECT * FROM table_name"
df = db.run_query(query)

3. Write to any table
 
if_exists : possible values {‘fail’, ‘replace’, ‘append’}

Here df is pandas Dataframe

db.write_to_table(df, table_name, 'append')

