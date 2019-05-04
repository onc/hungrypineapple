from pony.orm import Required, Set, Optional, PrimaryKey, Database, db_session
from flask_login import UserMixin

db = Database()
db.bind(provider='sqlite', filename='db.sqlite', create_db=True)


class User(db.Entity, UserMixin):
    id = PrimaryKey(int, auto=True)
    login = Required(str, unique=True)
    password = Required(str)
    complaints = Set('Complaint')


class Complaint(db.Entity):
    id = PrimaryKey(int, auto=True)
    title = Required(str)
    description = Required(str)
    complainer = Required('User')

    @db_session
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'complainer': self.complainer.login,
        }


db.generate_mapping(create_tables=True)
db.drop_all_tables(with_all_data=True)
db.create_tables()
