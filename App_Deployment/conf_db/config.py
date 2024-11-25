from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

DRIVER_SQL = "mysql+mysqlconnector"
USERNAME = "yahya"
PASSWORD = "yahya"
HOST = "mysql_instance"
DATABASE = "users"
PORT = "3306"

print(f"Username: {USERNAME}, Host: {HOST}, Port: {PORT}, Database: {DATABASE}")

engine = create_engine(f"{DRIVER_SQL}://yahya:yahya@mysql_instance:3306/users")
