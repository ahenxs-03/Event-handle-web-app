class Config:
    DEBUG=True
    Test=False
    SQLALCHEMY_DATABASE_URI = "sqlite:///mydatabase.db"
    SECRET_KEY = "super_secret"
    SESSION_REFRESH_EACH_REQUEST = False
    SESSION_COOKIE_SECURE = True
    SESSION_PERMANENT = True


