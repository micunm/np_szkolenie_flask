import os

current_dir = os.path.abspath(os.path.dirname(__file__))

MAIL_USERNAME = os.environ.get('MAIL_USERNAME')


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(current_dir, '..', 'test.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.mail.yahoo.com'
    MAIL_PORT = '587'
    MAIL_USE_TLS = True
    MAIL_USERNAME = MAIL_USERNAME
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = f"ML Runner <{MAIL_USERNAME}>"