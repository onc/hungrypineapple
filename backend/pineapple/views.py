import json
from flask.views import MethodView
from pony.orm import select, commit
from flask import jsonify, Response, request
from pineapple.models import Complaint, User


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
        complaint.title = data['title']
        complaint.description = data['description']
        commit()
        return jsonify(complaint.to_dict())

    def post(self, id):
        data = json.loads(request.data)
        complaint = Complaint(title=data['title'],
                              description=data['description'],
                              complainer=User.get(login=data['complainer']))
        commit()
        return jsonify(complaint.to_dict())
