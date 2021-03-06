import json
import datetime
from flask.views import MethodView
from pony.orm import select, commit
from flask import jsonify, Response, request
from pineapple.models import Complaint, User, Label, City, Vote, \
    ComplaintFeedback, OpenCallFeedback, OpenCall



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


class OpenCallFeedbackView(MethodView):
    def post(self, user_id, o_id):
        opencall = OpenCall.get(id=o_id)
        if not opencall:
            return Response(status=404)

        user = User.get(id=user_id)
        if not user:
            return Response(status=404)

        data = json.loads(request.data)
        text = data['text']

        feedback = OpenCallFeedback(user=user,
                                    opencall=opencall,
                                    text=text)
        commit()

        return jsonify(feedback.to_dict())


class ComplaintFeedbackView(MethodView):
    def post(self, user_id, c_id):
        complaint = Complaint.get(id=c_id)
        if not complaint:
            return Response(status=404)

        user = User.get(id=user_id)
        if not user:
            return Response(status=404)

        data = json.loads(request.data)
        text = data['text']

        feedback = ComplaintFeedback(user=user,
                                     complaint=complaint,
                                     text=text)
        commit()

        return jsonify(feedback.to_dict())


class LabelComplaintsView(MethodView):
    def get(self, id):
        label = Label.get(id=id)
        if not label:
            return Response(status=404)

        complaints = Complaint.select(lambda c: label in c.labels)
        return jsonify(list(c.to_dict() for c in complaints))


class CityView(MethodView):
    def get(self):
        cities = select(p for p in City)[:]
        return jsonify(list(c.to_dict() for c in cities))


class LoggedInUserComplaintView(MethodView):
    def get(self, user_id):
        user = User.get(id=user_id)
        if not user:
            return Response(status=404)

        upvotes = select(c for c in Complaint if user in c.votes.user and
                         True in c.votes.is_upvote)
        downvotes = select(c for c in Complaint if user in c.votes.user and
                           False in c.votes.is_upvote)
        other = Complaint.select(lambda c: c not in upvotes and
                                 c not in downvotes)

        upvote_dict = [u.to_dict_vote(True) for u in upvotes]
        downvote_dict = [u.to_dict_vote(False) for u in downvotes]
        other_dict = [u.to_dict_vote(None) for u in other]

        return jsonify(upvote_dict + downvote_dict + other_dict)


class VoteView(MethodView):
    def post(self, user_id, c_id):
        complaint = Complaint.get(id=c_id)
        if not complaint:
            return Response(status=404)

        user = User.get(id=user_id)
        if not user:
            return Response(status=404)

        data = json.loads(request.data)
        is_upvote = data['is_upvote']

        vote = Vote(user=user, complaint=complaint, is_upvote=is_upvote)
        commit()
        return jsonify(vote.to_dict())

    def delete(self, user_id, c_id):
        complaint = Complaint.get(id=c_id)
        if not complaint:
            return Response(status=404)

        user = User.get(id=user_id)
        if not user:
            return Response(status=404)

        vote = Vote.select(lambda v: v.user == user and
                           v.complaint == complaint)
        vote.delete()
        commit()

        return Response(status=200)


class ComplaintSubscriptionView(MethodView):
    def get(self, user_id):
        user = User.get(id=user_id)
        if not user:
            return Response(status=404)

        subscriptions = list(map(lambda s: s.to_dict(),
                                 user.subscribed_complaints))

        return jsonify(subscriptions)

    def post(self, user_id, c_id):
        complaint = Complaint.get(id=c_id)
        if not complaint:
            return Response(status=404)

        user = User.get(id=user_id)
        if not user:
            return Response(status=404)

        complaint.subscribed_complaints.add(user)
        commit()

        return Response(status=200)


class OpenCallSubscriptionView(MethodView):
    def get(self, user_id):
        user = User.get(id=user_id)
        if not user:
            return Response(status=404)

        subscriptions = list(map(lambda s: s.to_dict(),
                                 user.subscribed_opencalls))

        return jsonify(subscriptions)

    def post(self, user_id, c_id):
        opencall = OpenCall.get(id=c_id)
        if not opencall:
            return Response(status=404)

        user = User.get(id=user_id)
        if not user:
            return Response(status=404)

        opencall.subscribed_opencalls.add(user)
        commit()

        return Response(status=200)


class ComplaintView(MethodView):
    def get(self, id):
        if not id:
            complaints = select(p for p in Complaint)[:]
            return jsonify(list(c.to_dict_sums() for c in complaints))

        complaint = Complaint.get(id=id)
        if not complaint:
            return Response(status=404)
        return jsonify(complaint.to_dict_sums())

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
        return jsonify(complaint.to_dict_sums())

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
        return jsonify(complaint.to_dict_sums())


class OpenCallView(MethodView):
    def get(self, id):
        if not id:
            opencalls = select(p for p in OpenCall)[:]
            return jsonify(list(c.to_dict() for c in opencalls))

        opencall = OpenCall.get(id=id)
        if not opencall:
            return Response(status=404)
        return jsonify(opencall.to_dict())

    def put(self, id):
        opencall = OpenCall.get(id=id)
        if not opencall:
            return Response(status=404)

        data = json.loads(request.data)

        city = City.get(id=data['city'])
        if not city:
            return Response(status=404)

        opencall.title = data['title']
        opencall.description = data['description']
        opencall.created_at = datetime.datetime.now()
        opencall.city = city
        labels = select(l for l in Label if l.id in data['labels'])
        opencall.labels = labels

        commit()
        return jsonify(opencall.to_dict())

    def post(self, id):
        data = json.loads(request.data)
        labels = select(l for l in Label if l.id in data['labels'])
        city = City.get(id=data['city'])
        if not city:
            return Response(status=404)

        opencall = OpenCall(title=data['title'],
                            description=data['description'],
                            creator=User.get(id=data['creator']),
                            city=city,
                            labels=labels)
        commit()
        return jsonify(opencall.to_dict())
