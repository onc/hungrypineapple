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

    @db_session
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Feedback(db.Entity):
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
    password = Required(str)
    complaints = Set('Complaint')
    votes = Set('Vote')
    feedbacks = Set('Feedback')

    @db_session
    def to_dict(self):
        return {
            'login': self.login
        }


class Complaint(db.Entity):
    id = PrimaryKey(int, auto=True)
    title = Required(str)
    state = Required(str, default='OPEN')
    description = Required(str)
    created_at = Required(datetime.datetime,
                          default=datetime.datetime.utcnow)
    complainer = Required('User')
    city = Required('City')
    labels = Set('Label')
    votes = Set('Vote')
    feedbacks = Set('Feedback')

    @db_session
    def to_dict_vote(self, vote):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'state': self.state,
            'city': self.city.to_dict(),
            'complainer': self.complainer.id,
            'created_at': self.created_at.isoformat(),
            'is_upvote': vote,
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
                         if c.votes.is_upvote and c.id == self.id).first()

        downvotes = select(count(c.votes)
                           for c in Complaint
                           if not c.votes.is_upvote and c.id == self.id).first()

        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'state': self.state,
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


db.generate_mapping(create_tables=True)
db.drop_all_tables(with_all_data=True)
db.create_tables()
