from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql://user:password@db:5432/counter')
db = SQLAlchemy(app)

class Visit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer, default=0)

@app.route('/')
def index():
    visit = Visit.query.first()
    if not visit:
        visit = Visit(count=1)
        db.session.add(visit)
    else:
        visit.count += 1
    db.session.commit()
    return f'<h1>Посещений: {visit.count}</h1>'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)
