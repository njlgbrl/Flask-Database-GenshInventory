class Config:
    SECRET_KEY = 'genshinventory{}1234%613869@(#^!@#(^@(*$*!@#(!@#@!%_'
    SQLALCHEMY_DATABASE_URI = 'sqlite:////home/tako/Python Workspace/Flask/CPE011Database/db/users.db'
    SQLALCHEMY_BINDS = {
        'itemPool':'sqlite:////home/tako/Python Workspace/Flask/CPE011Database/db/itempool.db'
    }
    SQLALCHEMY_TRACK_MODIFICATIONS = False