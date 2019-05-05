import json
import datetime
from os import path
from flask import Flask, jsonify, request
from flask_login import LoginManager, login_required
from pony.flask import Pony
from pony.orm import db_session, select
from pineapple.models import Complaint, User, db, Label, City, Vote, OpenCall
from pineapple.views import ComplaintView, UserView, UserComplaintsView, \
    LabelComplaintsView, LabelView, CityComplaintsView, \
    LoggedInUserComplaintView, VoteView, ComplaintFeedbackView, CityView, \
    ComplaintSubscriptionView, OpenCallFeedbackView, OpenCallView, \
    OpenCallSubscriptionView

app = Flask(__name__)
app.config.update(DEBUG=True)

# User related
app.add_url_rule('/api/user/<id>',
                 view_func=UserView.as_view('user'))

app.add_url_rule('/api/user/<user_id>/complaint/subscriptions',
                 view_func=ComplaintSubscriptionView.as_view('comp_subscriptions'))

app.add_url_rule('/api/user/<user_id>/complaint/<c_id>/subscribe',
                 view_func=ComplaintSubscriptionView.as_view('comp_subscribe'))

app.add_url_rule('/api/user/<user_id>/opencall/subscriptions',
                 view_func=OpenCallSubscriptionView.as_view('open_subscriptions'))

app.add_url_rule('/api/user/<user_id>/opencall/<c_id>/subscribe',
                 view_func=OpenCallSubscriptionView.as_view('open_subscribe'))


app.add_url_rule('/api/user/<user_id>/complaint',
                 view_func=LoggedInUserComplaintView.as_view('loggedInUser'))

app.add_url_rule('/api/user/<user_id>/complaint/<c_id>/vote',
                 view_func=VoteView.as_view('vote'))

app.add_url_rule('/api/user/<user_id>/complaint/<c_id>/feedback',
                 view_func=ComplaintFeedbackView.as_view('complaintFeedback'))

app.add_url_rule('/api/user/<user_id>/opencall/<o_id>/feedback',
                 view_func=OpenCallFeedbackView.as_view('openCallFeedback'))

# label related
app.add_url_rule('/api/label/<id>/complaint',
                 view_func=LabelComplaintsView.as_view('labelComplaints'))


app.add_url_rule('/api/city',
                 view_func=CityView.as_view('city'))

app.add_url_rule('/api/label',
                 defaults={'id': None},
                 view_func=LabelView.as_view('label'))
app.add_url_rule('/api/label/<id>',
                 view_func=LabelView.as_view('labels'))


app.add_url_rule('/api/city/<id>/complaint',
                 view_func=CityComplaintsView.as_view('cityComplaints'))

# opencall
app.add_url_rule('/api/opencall',
                 defaults={'id': None},
                 view_func=OpenCallView.as_view('opencalls'))
app.add_url_rule('/api/opencall/<id>',
                 view_func=OpenCallView.as_view('opencall'))

# complaint views
app.add_url_rule('/api/complaint',
                 defaults={'id': None},
                 view_func=ComplaintView.as_view('complaints'))
app.add_url_rule('/api/complaint/<id>',
                 view_func=ComplaintView.as_view('complaint'))


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

    for record in data['City']:
        City(id=record['id'],
             name=record['name'])

    for record in data['Complaint']:
        labels = select(l for l in Label if l.id in record['labels'])
        city = City.get(id=record['city'])
        subscribers = select(u for u in User if u.id in record['subscribers'])
        Complaint(title=record['title'],
                  description=record['description'],
                  complainer=User.get(id=record['complainer']),
                  city=city,
                  subscribers=subscribers,
                  labels=labels)

    for record in data['OpenCall']:
        labels = select(l for l in Label if l.id in record['labels'])
        city = City.get(id=record['city'])
        subscribers = select(u for u in User if u.id in record['subscribers'])
        OpenCall(title=record['title'],
                 description=record['description'],
                 creator=User.get(id=record['creator']),
                 city=city,
                 subscribers=subscribers,
                 labels=labels)

    for record in data['Vote']:
        Vote(user=User.get(id=record['user']),
             complaint=Complaint.get(id=record['complaint']),
             is_upvote=record['is_upvote'])


seed_database(path.join(app.root_path, '..', 'db_seed.json'))
