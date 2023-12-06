import dash_bootstrap_components as dbc
import dash
# User management initialization
import os
from flask_login import LoginManager, UserMixin
from Models_db.users_mgt import db, Users as base
from dotenv import load_dotenv

load_dotenv()


USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
DATABASE = os.getenv("DATABASE")
PORT =os.getenv("PORT_MYSQL_SERVER")

external_js = ['https://raw.githubusercontent.com/SpaaceCadet/code_css/main/index.js',
               'https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js']

external_stylesheets = ['https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.2/css/all.min.css',
                        dbc.themes.BOOTSTRAP]
################Instatiate dash app###########################################

app = dash.Dash(__name__, meta_tags=[
        {
            'charset': 'utf-8',
        },
        {
            'name': 'viewport',
            'content': 'width=device-width, initial-scale=1, shrink-to-fit=no'
        }
    ],external_scripts=external_js,
                external_stylesheets=external_stylesheets)

server = app.server
app.config.suppress_callback_exceptions = True



server.config.update(
    SECRET_KEY=os.urandom(12),
    SQLALCHEMY_DATABASE_URI=f'mysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)
"""
DRIVER_SQL = os.getenv("DRIVER_SQL")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
DATABASE = os.getenv("DATABASE")
DRIVER = os.getenv("DRIVER")
TRUST = os.getenv("TRUST")


params = urllib.parse.quote_plus(f"DRIVER={DRIVER};SERVER={HOST};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}")

# initialization

server.config['SECRET_KEY'] = 'supersecret'
server.config['SQLALCHEMY_DATABASE_URI'] = f"{DRIVER_SQL}:///?odbc_connect=%s" % params
server.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
"""






db.init_app(server)

# Setup the LoginManager for the server
login_manager = LoginManager()
login_manager.init_app(server)
login_manager.login_view = '/login'
# Create User class with UserMixin
class Users(UserMixin, base):
    pass


# callback to reload the user object
@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

"""
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='users'
)"""



