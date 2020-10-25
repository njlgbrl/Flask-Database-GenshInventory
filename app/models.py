from app import dbase

class products(dbase.Model):
    __bind_key__ = 'itemPool'
    __tablename__ = 'products'
    id = dbase.Column('productID', dbase.Integer, primary_key=True)
    itemName = dbase.Column('itemName', dbase.String(45), nullable=True)
    itemDesc = dbase.Column('itemDesc', dbase.Text(4294000000), nullable=True)
    rarity = dbase.Column(dbase.Integer, nullable=True)
    type = dbase.Column(dbase.String(45), nullable=True)
    wares = dbase.relationship('wares', backref='products', lazy=True)

    def __init__(self, name, desc, rarity, type):
        self.itemName = name
        self.itemDesc = desc
        self.rarity = rarity
        self.type = type

class merchants(dbase.Model):
    __bind_key__ = 'itemPool'
    __tablename__ = 'merchants'
    id = dbase.Column('merchantID', dbase.Integer, primary_key=True)
    name = dbase.Column(dbase.String(45), nullable=True)
    type = dbase.Column(dbase.String(45), nullable=True)
    location = dbase.Column(dbase.String(45), nullable=True)
    wares = dbase.relationship('wares', backref='merchants', lazy=True, cascade='all, delete')

    def __init__(self, name, type, location):
        self.name = name
        self.type = type
        self.location = location

class wares(dbase.Model):
    __bind_key__ = 'itemPool'
    __tablename__ = 'wares'
    ID = dbase.Column(dbase.Integer, primary_key=True)
    merchantID = dbase.Column(dbase.Integer, dbase.ForeignKey('merchants.merchantID'), nullable=False)
    productID = dbase.Column(dbase.Integer, dbase.ForeignKey('products.productID'), nullable=False)
    stock = dbase.Column(dbase.Integer)
    price = dbase.Column(dbase.Integer)

    def __init__(self, mID, pID, stock, price):
        self.merchantID = mID
        self.productID = pID
        self.stock = stock
        self.price = price