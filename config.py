import os

var = os.getenv('HEROKU')

if var:
    pass
else:
    file_path = os.path.abspath(os.getcwd()) + "\database.db"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + file_path
    ERROR_404_HELP = False