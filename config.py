import os

class Config:
    SECRET_KEY=os.environ.get('SECRET_KEY') or '1234'
    MAIL_SERVER ='smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    pass

class DevConfig(Config):

     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://evans:meme@localhost/pitch'
     DEBUG = True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig

}
