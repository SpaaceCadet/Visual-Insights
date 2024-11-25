from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

DRIVER_SQL = os.getenv("DRIVER_SQL")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
DATABASE = os.getenv("DATABASE")
PORT =os.getenv("PORT_MYSQL_SERVER")
engine = create_engine(f"{DRIVER_SQL}://{USERNAME}:@{HOST}:{PORT}/{DATABASE}")
