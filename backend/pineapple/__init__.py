import json
from os import path
from flask import Flask, jsonify, request
from flask_login import LoginManager, login_required
from pony.flask import Pony
from pony.orm import db_session, select
from pineapple.models import Complaint, User, db, Label
from pineapple.views import ComplaintView, UserView, UserComplaintsView, \
    LabelComplaintsView, LabelView

app = Flask(__name__)
app.config.update(DEBUG=True)


app.add_url_rule('/api/user/<id>',
                 view_func=UserView.as_view('user'))

app.add_url_rule('/api/user/<id>/complaints',
                 view_func=UserComplaintsView.as_view('userComplaints'))

app.add_url_rule('/api/label/<id>/complaint',
                 view_func=LabelComplaintsView.as_view('labelComplaints'))

app.add_url_rule('/api/complaint',
                 defaults={'id': None},
                 view_func=ComplaintView.as_view('complaint'))
app.add_url_rule('/api/complaint/<id>',
                 view_func=ComplaintView.as_view('complaints'))

app.add_url_rule('/api/label',
                 defaults={'id': None},
                 view_func=LabelView.as_view('label'))
app.add_url_rule('/api/label/<id>',
                 view_func=LabelView.as_view('labels'))

Pony(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return db.User.get(id=user_id)


@db_session
def seed_database(dump_filename):
    # reading the json file
    data = json.load(open(dump_filename, 'r'))

    # going through the list of customers
    for record in data['User']:
        User(id=record['id'],
             login=record['login'],
             password=record['password'])

    for record in data['Label']:
        Label(id=record['id'],
              name=record['name'])

    # going through the list of brands
    for record in data['Complaint']:
        labels = select(l for l in Label if l.id in record['labels'])
        Complaint(title=record['title'],
                  description=record['description'],
                  complainer=User.get(id=record['complainer']),
                  labels=labels)


seed_database(path.join(app.root_path, '..', 'db_seed.json'))
