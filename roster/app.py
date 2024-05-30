from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)

# Use the DATABASE_URI from the .env file
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
db = SQLAlchemy(app)

class Dodger(db.Model):
    __tablename__ = 'dodgers'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    avg = db.Column(db.Numeric)
    hr = db.Column(db.Integer)
    rbi = db.Column(db.Integer)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dodgers', methods=['GET'])
def get_dodgers():
    players = Dodger.query.all()
    return jsonify([{
        'id': player.id,
        'first_name': player.first_name,
        'last_name': player.last_name,
        'avg': float(player.avg),
        'hr': player.hr,
        'rbi': player.rbi
    } for player in players])

if __name__ == '__main__':
    app.run(debug=True)
