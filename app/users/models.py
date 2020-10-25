from flask_login import UserMixin
from app import dbase, loginManager

class userInfo(UserMixin, dbase.Model):
    id = dbase.Column(dbase.Integer, primary_key = True)
    email = dbase.Column(dbase.String(50))
    username = dbase.Column(dbase.String(50), unique = True)
    password = dbase.Column(dbase.String(100))

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password

@loginManager.user_loader
def loadUser(userID):
    return userInfo.query.get(int(userID))