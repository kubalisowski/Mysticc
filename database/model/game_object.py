from _db import db

class GameObject(db):
    __tablename__ = 'object'

    id      = db.Column(db.Integer, primary_key=True)
    x       = db.Column(db.Integer)
    y       = db.Column(db.Integer)
    width   = db.Column(db.Integer)
    height  = db.Column(db.Integer)
    frameX  = db.Column(db.Integer)
    frameY  = db.Column(db.Integer)
    speed   = db.Column(db.Integer)
    moving  = db.Column(db.Boolean)
    img_src = db.Column(db.Integer)
    img_src = db.Column(db.Integer)
    
    username = db.Column(db.String(80), unique=True, nullable=False)

    def json(self):
        return {'id': self.id,'username': self.username, 'email': self.email}