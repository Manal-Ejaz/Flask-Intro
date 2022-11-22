from flask import Flask, render_template,url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os



app = Flask(__name__) #reference name


basedir = os.path.abspath(os.path.dirname(__file__))

#app.config['SQLAlCHEMY_DATABASE_URI']='sqlite:///test.db' #where my database is located
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'test.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app) #database initializing



class Todo(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    content=db.Column(db.String(200),nullable=False)
    completed=db.Column(db.Integer,default=0)
    date_created=db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>'%self.id

@app.route('/')

def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)