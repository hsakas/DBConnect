import pyodbc
import pandas.io.sql as sql
import sqlalchemy

# engine = sqlalchemy.create_engine("mssql+pyodbc://192.168.1.9/DB_LYB_EXECUTION_PHASE?driver=SQL+SERVER")


class SqlConnect:
    conn = None

    def __init__(self, driver, server, database):
        self.conn = pyodbc.connect('DRIVER={'+driver+'};SERVER='+server+';DATABASE='+database)
        self.engine = sqlalchemy.create_engine("mssql+pyodbc://"+server+"/"+database+"?driver=SQL+SERVER")

    def run_query(self, query):
        return sql.read_sql(query, self.conn)

    def write_to_table(self, df, table_name, if_exists):
        df.to_sql(name=table_name, con=self.engine, if_exists=if_exists, index=False)
        # if_exists = {‘fail’, ‘replace’, ‘append’}

