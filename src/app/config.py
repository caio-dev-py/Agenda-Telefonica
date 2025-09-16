import os 
from dotenv import load_dotenv

load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # CONFIGURANDO A SECRET_KEY 
    SECRET_KEY = os.getenv("SECRET_KEY")
    
    # CONFIGURANDO SQLALCHEMY
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(basedir, "database.db")}'
    SQLACHEMY_TRACK_MODIFICATIONS = False