import json
import datetime
from flask.views import MethodView
from pony.orm import select, commit
from flask import jsonify, Response, request
from pineapple.models import Complaint, User, Label, City


class UserView(MethodView):
    def get(self, id):
        user = User.get(id=id)
        if not user:
            return Response(status=404)

        return jsonify(user.to_dict())


class LabelView(MethodView):
    def get(self, id):
        if not id:
            labels = select(p for p in Label)[:]
            return jsonify(list(c.to_dict() for c in labels))

        label = Label.get(id=id)
        if not label:
            return Response(status=404)
        return jsonify(label.to_dict())


class CityComplaintsView(MethodView):
    def get(self, id):
        city = City.get(id=id)
        if not city:
            return Response(status=404)

        complaints = Complaint.select(lambda c: c.city == city)
        return jsonify(list(c.to_dict() for c in complaints))


class UserComplaintsView(MethodView):
    def get(self, id):
        user = User.get(id=id)
        if not user:
            return Response(status=404)

        complaints = Complaint.select(lambda c: c.complainer == user)
        return jsonify(list(c.to_dict() for c in complaints))


class LabelComplaintsView(MethodView):
    def get(self, id):
        label = Label.get(id=id)
        if not label:
            return Response(status=404)

        complaints = Complaint.select(lambda c: label in c.labels)
        return jsonify(list(c.to_dict() for c in complaints))


class ComplaintView(MethodView):
    def get(self, id):
        if not id:
            complaints = select(p for p in Complaint)[:]
            return jsonify(list(c.to_dict() for c in complaints))

        complaint = Complaint.get(id=id)
        if not complaint:
            return Response(status=404)
        return jsonify(complaint.to_dict())

    def put(self, id):
        complaint = Complaint.get(id=id)
        if not complaint:
            return Response(status=404)

        data = json.loads(request.data)

        city = City.get(id=data['city'])
        if not city:
            return Response(status=404)

        complaint.title = data['title']
        complaint.description = data['description']
        complaint.created_at = datetime.datetime.now()
        complaint.city = city
        labels = select(l for l in Label if l.id in data['labels'])
        complaint.labels = labels

        commit()
        return jsonify(complaint.to_dict())

    def post(self, id):
        data = json.loads(request.data)
        labels = select(l for l in Label if l.id in data['labels'])
        city = City.get(id=data['city'])
        if not city:
            return Response(status=404)

        complaint = Complaint(title=data['title'],
                              description=data['description'],
                              complainer=User.get(id=data['complainer']),
                              city=city,
                              labels=labels)
        commit()
        return jsonify(complaint.to_dict())
