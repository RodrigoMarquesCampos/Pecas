
import os.path
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/pecass'
SQLALCHEMY_TRACK_MODIFICATIONS = True

#key for encript informations of formularies
SECRET_KEY = 'extremaseguranca'
