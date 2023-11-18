import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()
db_user = os.environ["DB_USER"]
db_pass = os.environ["DB_PASSWORD"]
db_name = os.environ["DB_DATABASE"]
db_host = os.environ["DB_HOST"]
db_port = os.environ["DB_PORT"]


def fetch_data_from_db():
    conn = psycopg2.connect(user=db_user, password=db_pass, database=db_name, host=db_host,
                            port=db_port)
    cur = conn.cursor()
    cur.execute(
        # f"SELECT * FROM pedestrians_track ORDER BY start_time ASC LIMIT 10"
        f"SELECT time_bucket('15 minutes', start_time) AS bucket_start_time,ped_id,spots,aliases FROM pedestrians_track;"
    )
    data = cur.fetchall()
    conn.commit()
    return data
