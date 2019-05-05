from pony.orm import Required, Set, Optional, PrimaryKey, Database, \
    db_session, composite_key, select, count
from flask_login import UserMixin
import datetime

db = Database()
db.bind(provider='sqlite', filename='db.sqlite', create_db=True)


class City(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str, unique=True)
    complaints = Set('Complaint')
    opencalls = Set('OpenCall')
    users = Set('User')

    @db_session
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Label(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str, unique=True)
    complaint = Set('Complaint')
    opencalls = Set('OpenCall')

    @db_session
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }


class ComplaintFeedback(db.Entity):
    id = PrimaryKey(int, auto=True)
    text = Required(str)
    user = Required('User')
    complaint = Required('Complaint')
    created_at = Required(datetime.datetime,
                          default=datetime.datetime.utcnow)

    @db_session
    def to_dict(self):
        return {
            'id': self.id,
            'user': self.user.id,
            'complaint': self.complaint.id,
            'text': self.text,
            'created_at': self.created_at.isoformat()
        }


class OpenCallFeedback(db.Entity):
    id = PrimaryKey(int, auto=True)
    text = Required(str)
    user = Required('User')
    opencall = Required('OpenCall')
    created_at = Required(datetime.datetime,
                          default=datetime.datetime.utcnow)

    @db_session
    def to_dict(self):
        return {
            'id': self.id,
            'user': self.user.id,
            'opencall': self.opencall.id,
            'text': self.text,
            'created_at': self.created_at.isoformat()
        }


class Vote(db.Entity):
    id = PrimaryKey(int, auto=True)
    user = Required('User')
    complaint = Required('Complaint')
    is_upvote = Required(bool)
    composite_key(user, complaint)

    @db_session
    def to_dict(self):
        return {
            'user': self.user.id,
            'complaint': self.complaint.id,
            'is_upvote': self.is_upvote
        }


class User(db.Entity, UserMixin):
    id = PrimaryKey(int, auto=True)
    login = Required(str, unique=True)
    city = Optional('City')
    password = Required(str)
    # 0 = citizen, 1 = townhall, 2 = moderator
    role = Required(int, default=0)
    complaints = Set('Complaint', reverse="complainer")
    opencalls = Set('OpenCall', reverse="creator")
    votes = Set('Vote')
    complaint_feedbacks = Set('ComplaintFeedback')
    opencall_feedbacks = Set('OpenCallFeedback')
    subscribed_complaints = Set('Complaint', reverse="subscribers")
    subscribed_opencalls = Set('OpenCall', reverse="subscribers")

    @db_session
    def to_dict(self):
        return {
            'id': self.id,
            'login': self.login,
            'complaint_subscriptions': list(map(lambda s: s.id,
                                                self.subscribed_complaints)),
            'opencall_subscriptions': list(map(lambda s: s.id,
                                               self.subscribed_opencalls))
        }


class Complaint(db.Entity):
    id = PrimaryKey(int, auto=True)
    title = Required(str)
    state = Required(str, default='OPEN')
    approved = Required(bool, default=False)
    description = Required(str)
    created_at = Required(datetime.datetime,
                          default=datetime.datetime.utcnow)
    complainer = Required('User')
    city = Required('City')
    labels = Set('Label')
    votes = Set('Vote')
    feedbacks = Set('ComplaintFeedback')
    subscribers = Set('User', reverse="subscribed_complaints")

    @db_session
    def to_dict_vote(self, vote):
        upvotes = select(count(c.votes)
                         for c in Complaint
                         if True in c.votes.is_upvote and
                         c.id == self.id).first()
        
        downvotes = select(count(c.votes)
                           for c in Complaint
                           if False in c.votes.is_upvote and
                           c.id == self.id).first()

        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'state': self.state,
            'approved': self.approved,
            'city': self.city.to_dict(),
            'complainer': self.complainer.id,
            'created_at': self.created_at.isoformat(),
            'is_upvote': vote,
            'upvotes': upvotes,
            'downvotes': downvotes,
            'feedback': list(map(lambda f: {
                'feedback_id': f.id,
                'text': f.text,
                'user': f.user.id,
                'created_at': f.created_at.isoformat()
            }, self.feedbacks)),
            'labels': list(map(lambda x: x.to_dict(), self.labels))
        }

    @db_session
    def to_dict_sums(self):
        upvotes = select(count(c.votes)
                         for c in Complaint
                         if True in c.votes.is_upvote and
                         c.id == self.id).first()

        downvotes = select(count(c.votes)
                           for c in Complaint
                           if False in c.votes.is_upvote and
                           c.id == self.id).first()

        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'state': self.state,
            'approved': self.approved,
            'city': self.city.to_dict(),
            'complainer': self.complainer.id,
            'created_at': self.created_at.isoformat(),
            'upvotes': upvotes,
            'downvotes': downvotes,
            'feedback': list(map(lambda f: {
                'feedback_id': f.id,
                'text': f.text,
                'user': f.user.id,
                'created_at': self.created_at.isoformat()
            }, self.feedbacks)),
            'labels': list(map(lambda x: x.to_dict(), self.labels))
        }


class OpenCall(db.Entity):
    id = PrimaryKey(int, auto=True)
    title = Required(str)
    state = Required(str, default='OPEN')
    description = Required(str)
    created_at = Required(datetime.datetime,
                          default=datetime.datetime.utcnow)
    creator = Required('User')
    city = Required('City')
    labels = Set('Label')
    feedbacks = Set('OpenCallFeedback')
    subscribers = Set('User', reverse="subscribed_opencalls")

    @db_session
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'state': self.state,
            'city': self.city.to_dict(),
            'creator': self.creator.id,
            'created_at': self.created_at.isoformat(),
            'feedback': list(map(lambda f: {
                'feedback_id': f.id,
                'text': f.text,
                'user': f.user.id,
                'created_at': f.created_at.isoformat()
            }, self.feedbacks)),
            'labels': list(map(lambda x: x.to_dict(), self.labels))
        }


db.generate_mapping(create_tables=True)
db.drop_all_tables(with_all_data=True)
db.create_tables()
