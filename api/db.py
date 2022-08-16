import os
from psycopg_pool import ConnectionPool

user = os.environ["PGUSER"]
password=os.environ["PGPASSWORD"]
db = os.environ["PGDATABASE"]
host = os.environ["PGHOST"]

url = f'postgresql://{user}:{password}@{host}/{db}'
pool = ConnectionPool(conninfo=url)

class UserQueries:
    def get_all_categories(self, page, num_results=100):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                query = """
                    SELECT id, title, canon
                    FROM categories
                """
                query += f"OFFSET {page*100}"
                if num_results and type(num_results) == int:
                    query += f"LIMIT {num_results+ (page*100)}"
                cur.execute(query)

                results = []
                for row in cur.fetchall():
                    record = {}
                    for i, column in enumerate(cur.description): #[(0, {"name": "id"}), (1,{"name": "title"}), (2, {"name": "canon"})]
                        record[column.name] = row[i]
                    results.append(record)

                return results