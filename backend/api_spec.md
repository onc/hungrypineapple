# API Spec

## Users

### Get one user

GET http://localhost:5000/api/user/<id>

Response:
```
{
  "login": "onze"
}
```

## Labels

### Get all labels

GET http://localhost:5000/api/label

Response:
```
[
  {
    "id": 1,
    "name": "foo"
  },
  {
    "id": 2,
    "name": "bar"
  }
]
```

### Get one label

GET http://localhost:5000/api/label/<id>

Response:
```
{
  "id": 1,
  "name": "foo"
}
```

## Complaints

### Get all complaints

GET http://localhost:5000/api/complaint

Response:
```
[
  {
    "complainer": "onze",
    "description": "Your are doing bad",
    "id": 1,
    "labels": [
      {
        "id": 2,
        "name": "bar"
      },
      {
        "id": 1,
        "name": "foo"
      }
    ],
    "title": "My adsfkhas;fhja;sdfa complaint"
  },
  {
    "complainer": "onze",
    "description": "Your are doing bad",
    "id": 2,
    "labels": [
      {
        "id": 2,
        "name": "bar"
      }
    ],
    "title": "My second complaint"
  }
]
```

### Create complaints

POST http://localhost:5000/api/complaint

```
{
  "complainer": 1,
  "description": "sdafja;dfha;ds",
  "title": "My third complaint",
	"labels": [1]
}
```

Response:
```
{
  "complainer": 1,
  "description": "sdafja;dfha;ds",
  "created_at": "2019-05-04T16:30:51.412409",
  "id": 4,
  "labels": [
    {
      "id": 1,
      "name": "foo"
    }
  ],
  "title": "My third complaint"
}
```

### Update complaint

PUT http://localhost:5000/api/complaint/<id>

```
{
  "complainer": 1,
  "description": "Your are doing bad",
  "title": "My adsfkhas;fhja;sdfa complaint",
	"labels": [1]
}
```

Response:
```
{
  "complainer": 1,
  "description": "Your are doing bad",
  "created_at": "2019-05-04T16:30:51.412409",
  "id": 1,
  "labels": [
    {
      "id": 1,
      "name": "foo"
    }
  ],
  "title": "My adsfkhas;fhja;sdfa complaint"
}
```

### Get all complaints a user created

GET http://localhost:5000/api/user/<id>/complaint

Response:
```
[
  {
    "complainer": 1,
    "description": "Your are doing bad",
    "created_at": "2019-05-04T16:30:51.412409",
    "id": 1,
    "labels": [
      {
        "id": 1,
        "name": "foo"
      }
    ],
    "title": "My adsfkhas;fhja;sdfa complaint"
  },
  ...
```

### Get the list of complaints for a user (with his up and downvotes)

GET http://localhost:5000/api/user/1/complaint

Response:

```
[
  {
    "city": {
      "id": 2,
      "name": "Brno"
    },
    "complainer": 1,
    "created_at": "2019-05-04T20:16:34.866781",
    "description": "Your are doing bad",
    "id": 2,
    "is_upvote": true,
    "labels": [
      {
        "id": 2,
        "name": "bar"
      }
    ],
    "state": "OPEN",
    "title": "My second complaint"
  },
  {
    "city": {
      "id": 2,
      "name": "Brno"
    },
    "complainer": 1,
    "created_at": "2019-05-04T20:16:34.868801",
    "description": "bar",
    "id": 3,
    "is_upvote": true,
    "labels": [
      {
        "id": 1,
        "name": "foo"
      },
      {
        "id": 2,
        "name": "bar"
      }
    ],
    "state": "OPEN",
    "title": "foo"
  },
  {
    "city": {
      "id": 1,
      "name": "Prague"
    },
    "complainer": 1,
    "created_at": "2019-05-04T20:16:34.860265",
    "description": "Your are doing bad",
    "id": 1,
    "is_upvote": false,
    "labels": [
      {
        "id": 1,
        "name": "foo"
      }
    ],
    "state": "OPEN",
    "title": "My first complaint"
  }
]
```

### Get all complaints with a label

GET http://localhost:5000/api/label/<id>/complaint

Response:
```
[
  {
    "complainer": 1,
    "description": "Your are doing bad",
    "created_at": "2019-05-04T16:30:51.412409",
    "id": 1,
    "labels": [
      {
        "id": 1,
        "name": "foo"
      }
    ],
    "title": "My adsfkhas;fhja;sdfa complaint"
  },
  ...
```

## Feedback

### Leave feedback

http://localhost:5000/api/user/<user_id>/complaint/<id>/feedback

```
{
	"text": "some feedback"
}
```

Response:
```
{
  "complaint": 1,
  "created_at": "2019-05-04T21:00:40.688630",
  "id": 1,
  "text": "some feedback",
  "user": 1
}
```

## Voting

### Give a vote

POST /api/user/<user_id>/complaint/<c_id>/vote

```
{
	"is_upvote": true
}
```

Response:

```
{
  "complaint": 3,
  "is_upvote": true,
  "user": 1
}
```

### Delete a vote

DELETE /api/user/<user_id>/complaint/<c_id>/vote

Response:

HTTP 200, OK
