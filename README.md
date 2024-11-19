# Mission Management API
A Django REST API for managing missions and their associated targets. This API allows you to create, update, and manage missions, targets, and their associated properties, such as completion status and notes.
# Setup
## Prerequisites
- Python 3.8 or higher
- Django 5.1.x or higher
- Django REST Framework 3.15.x or higher
## Installation
1. Clone the repository:
```https://github.com/ati1monder/spycats_django```
2. Create a virtual environment and activate it:
```
python -m venv venv
source venv/bin/activate
```
3. Install the dependencies:
```pip install -r requirements.txt```
4. Run the development server (located in **spycats** folder)
```python manage.py runserver```
# Validations
- You cannot update the notes field of a target if the target or the mission is marked as complete.
- When a mission is marked as complete, you cannot modify any of its associated targets' notes.
- Cat breed is validated using [TheCatAPI](https://api.thecatapi.com/v1/breeds)

# API Endpoints
You can view the API endpoints through this [Postman Collection](https://www.postman.com/atimonder1/public-workspace/collection/pj0031u/mission-and-cat-api?action=share&creator=39853894).
## Key endpoints

### Cats

**GET /api/cats/**

Retrieve a list of all cats.

**GET /api/cats/{id}/**

Retrieve the details of a specific cat by ID.

**POST /api/cats/**

Create a new cat. Example request body:
```
{
  "name": "Whiskers",
  "years_of_experience": 5,
  "breed": "Bengal",
  "salary": 2000.0
}
```

**PUT /api/cat/{id}/**

Full update an existing cat. Example request body:

```
{
    "name": "WhiskersUpd",
    "years_of_experience": 3,
    "breed": "Bengal",
    "salary": 3000
}
```

**PATCH /api/cat/{id}/**

Partial update an existing cat. Example request body:

```
{
    "name": "RomanianUpdated"
}
```

**DELETE /api/cat/{id}/**

Removal an existing cat.

### Missions

**GET /api/missions/**

Retrieve a list of all missions.

**GET /api/missions/{id}/**

Retrieve the details of a specific mission by ID.

**POST /api/missions/**

Create a new mission. Example request body:
```
{
  "cat": 2,
  "complete": false,
  "targets": [
    {"name": "Target A", "country": "USA", "notes": "Top secret", "complete": false},
    {"name": "Target B", "country": "UK", "notes": "Backup", "complete": false}
  ]
}
```

**PUT /api/missions/{id}/**

Full update of an existing mission. Example request body:

```
{
  "cat": 2,
  "complete": true,
  "targets": [
    {"id": 1, "name": "Updated Target A", "country": "USA", "notes": "Updated notes", "complete": true},
    {"id": 2, "name": "Updated Target B", "country": "UK", "notes": "Updated notes", "complete": false}
  ]
}
```

**PATCH /api/missions/{id}/**

Update an existing mission. Example request body:

```
{
  "complete": true
}
```

**DELETE /api/missions/{id}/**

Removal of an existing mission.

## Targets

**PATCH /api/missions/{mission_id}/targets/{target_id}/**

Update a specific target. Example request body:
```
  {"notes": "Example text of a note"}
```
