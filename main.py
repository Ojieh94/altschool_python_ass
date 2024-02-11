# Create a FastAPI project with the following specifications:
# A Student resource. Each student will have:
# Id (int)
# Name(str)
# Age (int)
# Sex (str)
# Height (float)
# For data storage, use an in-memory storage (Python dictionary)
# Create endpoints to do the following:
# Create a Student resource
# Retrieve a Student resource (one Student and many Students)
# Update a Student resource
# Delete a Student resource

# Push your project to a public git repository and post you submission here
# Goodluck!

# NOTE: You are not required to use Pydantic type enforcement. Just basic Python.



from fastapi import FastAPI, status, HTTPException

from uuid import UUID

app = FastAPI()

students = {}

student_data = {"id": int, "name": str, "age": int, "sex": str, "height": float}

@app.get("/")
def home():
    return {"message": "Welcome to my students API. Feel free to explore further"}

@app.get("/students")
def get_students():
    return students

@app.get("/students/{id}", status_code=status.HTTP_200_OK)
def get_students_by_id(id: str):
    student = students.get(id)
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )
    
    return student

@app.post("/students", status_code=status.HTTP_201_CREATED)
def add_student(name: str, age: int, sex: str, height: float):
    new_student = student_data.copy()
    new_student["id"] = str(UUID(int=len(students) + 1))
    new_student["name"] = name
    new_student["age"] = age
    new_student["sex"] = sex
    new_student["height"] = height

    students[new_student["id"]] = new_student

    return {"message": "Student added successfully", "data": new_student}

@app.put("/students/{id}", status_code=status.HTTP_200_OK)
def update_student(id: str, name: str, age: int, sex: str, height: float):
    student = students.get(id)
    if not student:
        raise HTTPException(
             status_code=status.HTTP_404_NOT_FOUND,
             detail="Student not found")
    student["name"] = name
    student["age"] = age
    student["sex"] = sex
    student["height"] = height

    return {"message": "Student updated successfully", "data": student}


@app.delete("/students/{id}")
def delete_student(id: str):
    student = students.get(id)
    if not student:
         raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Student not found"
        )
    
    del students[id]

    return {"message": "Student deleted successfully"}
