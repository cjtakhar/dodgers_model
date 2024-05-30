import pandas as pd
from app import app, db, Dodger

# Load data from CSV file
data = pd.read_csv('dodgers.csv')
players = data.to_dict(orient='records')

# Drop the table if it exists and recreate it
with app.app_context():
    # Drop all tables
    db.drop_all()
    # Create all tables
    db.create_all()

    # Populate database with data
    for player in players:
        new_player = Dodger(
            first_name=player['first_name'],
            last_name=player['last_name'],
            avg=player['avg'],
            hr=player['hr'],
            rbi=player['rbi']
        )
        db.session.add(new_player)
    db.session.commit()

print("Database rebuilt and data imported successfully.")
