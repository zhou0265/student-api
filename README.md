
### Rest api for Question 1

# Student API

This is a simple RESTful API built with Python and Flask that supports basic CRUD operations (Create, Read, Update, Delete) for a Student entity. Each student has an ID, Name, Grade, and Email.

## Features

- **GET /students**: Retrieve a list of all students.
- **GET /students/{id}**: Retrieve details of a student by ID.
- **POST /students**: Add a new student.
- **PUT /students/{id}**: Update an existing student by ID.
- **DELETE /students/{id}**: Delete a student by ID.

## Getting Started

### Prerequisites

- **Python 3.10: Make sure Python is installed on your machine.
- **pip**: Python package manager, which usually comes with Python.

### 1. Create a New Directory for this project:

```bash
mkdir rest-api-8916-mid
cd rest-api-8916-mid
```


### 2. Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```
### 3. Install Flask :

```bash
pip install Flask

```
### 4. Create a requirements.txt file to save dependencies:

```bash
pip freeze > requirements.txt
```

### 5. Create app.py file


### 6. Run locally
```bash
python app.py
```

### Create a GitHub Repository and Push the Code

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/zhou0265/rest-api-8916-mid.git
git push -u origin main
```

### Next step 
Deploy the API to Azure Web App Service

