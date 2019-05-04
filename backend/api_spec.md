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

### Get all complaints of a user

GET http://localhost:5000/api/user/<id>/complaints

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
