from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# In-memory storage for student data
students = {}
current_id = 1

# GET /students: Retrieve all students
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(list(students.values())), 200

# GET /students/{id}: Retrieve a student by ID
@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = students.get(student_id)
    if student is None:
        abort(404, description="Student not found")
    return jsonify(student), 200

# POST /students: Add a new student
@app.route('/students', methods=['POST'])
def create_student():
    global current_id
    if not request.json or 'name' not in request.json or 'grade' not in request.json or 'email' not in request.json:
        abort(400, description="Invalid data")
    
    new_student = {
        'id': current_id,
        'name': request.json['name'],
        'grade': request.json['grade'],
        'email': request.json['email']
    }
    
    students[current_id] = new_student
    current_id += 1
    return jsonify(new_student), 201

# PUT /students/{id}: Update an existing student by ID
@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    student = students.get(student_id)
    if student is None:
        abort(404, description="Student not found")
    
    if not request.json:
        abort(400, description="Invalid data")
    
    student['name'] = request.json.get('name', student['name'])
    student['grade'] = request.json.get('grade', student['grade'])
    student['email'] = request.json.get('email', student['email'])
    
    return jsonify(student), 200

# DELETE /students/{id}: Delete a student by ID
@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    if student_id not in students:
        abort(404, description="Student not found")
    
    del students[student_id]
    return jsonify({"message": "Student deleted successfully"}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
