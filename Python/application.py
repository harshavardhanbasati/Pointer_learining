from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['POSTGRESQL_DATABASE_URL'] = 'postgresql://root:1234@localhost/exp'
db = SQLAlchemy(app)
class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(200))
    def __repr__(self):
        return f"{self.name}-{self.description}"
@app.route('/')
def index():
    return 'Hello!'
@app.route('/drinks')
def get_drinks():
    return{"drinks":"drink data"}
