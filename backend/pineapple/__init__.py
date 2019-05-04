import json
from os import path
from flask import Flask, jsonify, request
from flask.views import MethodView
from flask_login import LoginManager, login_required
from pony.flask import Pony
from pony.orm import db_session, select
from pineapple.models import Complaint, User, db

app = Flask(__name__)
app.config.update(DEBUG=True)


class ComplaintView(MethodView):
    def get(self, id):
        if not id:
            complaints = select(p for p in Complaint)[:]
            return jsonify(list(c.to_dict() for c in complaints))

        complaint = Complaint.get(id=id)
        return jsonify(complaint.to_dict())


app.add_url_rule('/api/complaint',
                 defaults={'id': None},
                 view_func=ComplaintView.as_view('complaint'))
app.add_url_rule('/api/complaint/<id>',
                 view_func=ComplaintView.as_view('complaints'))


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

    # going through the list of brands
    for record in data['Complaint']:
        Complaint(title=record['title'],
                  description=record['description'],
                  complainer=User.get(id=record['complainer']))


seed_database(path.join(app.root_path, '..', 'db_seed.json'))
