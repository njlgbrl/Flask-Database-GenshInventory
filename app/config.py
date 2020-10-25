class Config:
    SECRET_KEY = 'genshinventory{}1234%613869@(#^!@#(^@(*$*!@#(!@#@!%_'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:''@localhost/flaskUsers'
    SQLALCHEMY_BINDS = {
        'itemPool':'mysql+pymysql://root:''@localhost/finalProjDB'
    }
    SQLALCHEMY_TRACK_MODIFICATIONS = False