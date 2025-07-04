from fastapi import FastAPI, HTTPException
from models import Student

app = FastAPI()

# In-memory "database"
students = {}

@app.get("/")
def read_root():
    return {"message": "Welcome to Student API"}

@app.post("/students/", response_model=Student)
def create_student(student: Student):
    if student.id in students:
        raise HTTPException(status_code=400, detail="Student already exists")
    students[student.id] = student
    return student

@app.get("/students/{student_id}", response_model=Student)
def get_student(student_id: int):
    student = students.get(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.get("/students/", response_model=list[Student])
def get_all_students():
    return list(students.values())

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    del students[student_id]
    return {"message": f"Student {student_id} deleted"}
