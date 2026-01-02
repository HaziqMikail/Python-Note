from fastapi import FastAPI, HTTPException, Path #? Import FastAPI and Path for path parameters
from typing import Optional as optional #? Import Optional for optional query parameters for type hinting
from pydantic import BaseModel #? Import BaseModel for data validation and serialization

app = FastAPI() #? Initialize FastAPI application

# to run the server: uvicorn NoteApi:app --reload

#? endpoint to check if the API is running
#? exp: amazon/create-product

#TODO   main HTTP methods: 
#? GET - to retrieve data
#? POST - to create data
#? PUT - to update data
#? DELETE - to delete data


#? ----------------------------------------------------------------
#TODO    STATUS CODES & EXCEPTIONS REFERENCE
#? ----------------------------------------------------------------
#? Success Categories:
#? 200 OK           -> Default for GET, PUT, DELETE. Everything worked.
#? 201 Created      -> Best for POST. A new resource was successfully created.
#? 204 No Content   -> Success, but returning no data (common for DELETE).

#? Client Error Categories (The User's fault):
#? 400 Bad Request  -> Logic error (e.g., Student already exists).
#? 401 Unauthorized -> User is not logged in.
#? 403 Forbidden    -> User is logged in but lacks permission.
#? 404 Not Found    -> The specific ID/Resource does not exist.
#? 422 Unprocessable Entity -> Validation error (Pydantic caught this).

#? Server Error Categories (Your code's fault):
#? 500 Internal Server Error -> Your Python code crashed/has a bug.



#? --------------------------------------------------
#? Dictionary to act as in-memory database
#? --------------------------------------------------

students = {
    1: {"name": "John Doe", "age": 20, "course": "Computer Science"},
    2: {"name": "Jane Smith", "age": 22, "course": "Mathematics"},
    3: {"name": "Alice Johnson", "age": 19, "course": "Physics"},
}


#? ----------------------------------------------------------------
#? PYDANTIC MODELS (Data Validation)
#? ----------------------------------------------------------------

class Student(BaseModel): #? Define a Pydantic model for Student to validate request body data
    name: str
    age: int
    course: str

class UpdateStudent(BaseModel): #? Make it optional because in update we may not want to update all fields
    name: optional[str] = None
    age: optional[int] = None
    course: optional[str] = None



#? --------------------------------
#? path parameter example
#? --------------------------------

@app.get("/") #? Root endpoint
def index():
    return {"message": "Welcome to the Note API!"}


@app.get("/students/{student_id}") #? Endpoint with path parameter {student_id} to get student by ID
                                   #? Path(...) makes the parameter required, with additional validation options,description,gt,lt
def get_student(student_id: int = Path(..., description="The ID of the student to retrieve", gt=0,lt=100)): 
    if student_id not in students:          #? Check if student_id exists in the dictionary
        raise HTTPException(status_code=404, detail="Student not found") #? Return error if not found
    return students[student_id]


#TODO - Search student by name and min age
@app.get("/search-students/") 
def search(course: optional[str] = None, min_age: int = 0):         #? Endpoint with optional query parameters to search students by course and minimum age
    results = [s for s in students.values() if s["age"] >= min_age] #? Filter students by minimum age
    if course:
        results = [s for s in results if s["course"] == course]     #? Further filter by course if provided
    return results


#? --------------------------------
#? query parameter example 
#? --------------------------------

@app.get("/get_student_byname/{student_id}") #? Endpoint with query parameter to get student by name
def get_student_by_name(*,student_id : int, name: optional[str] = None, test : int): #?'*' makes default parameters keyword-only so that they cannot be passed positionally
    for s_id in students:                                     #?(name: optional[str] = None, test : int) means name is optional and can be None, test is required 
        if students[s_id]["name"] == name:   #? Check if the student's name matches the query parameter
            return {"student_id": s_id}      #? Return the student ID if found
    return {"error": "Student not found"} 


#? -----------------------------------
#? request body example (POST method)
#? -----------------------------------

@app.post("/create-students/{student_id}", response_model=Student)   #? endpoint to create a new student with given student_id, response_model to validate response data
def create_student(student_id: int, student: Student):               #? student_id from path, student from request body validated against Student model
    if student_id in students:                                       #? Check if student_id already exists
        return {"error": "Student ID already exists"}                #? Return error if exists

    students[student_id] = student.model_dump()          #? Add the new student to the dictionary, convert Pydantic model to dict
    return students[student_id]                          #? Return the newly created student data


#? --------------------------------
#? request body example (PUT method)
#? --------------------------------

@app.put("/update-student/{student_id}")                     #? Endpoint to update an existing student with given student_id
def update_student(student_id: int, student: UpdateStudent): #? student_id from path, student from request body validated against Student model
    if student_id not in students:                           #? Check if student_id exists
        return {"error": "Student not found"}                #? Return error if not found

    if student.name is not None:                           #? Keep existing value if no new value is provided
        students[student_id]["name"] = student.name        #? is this not set, unchanged data set to null instead of previous value

    if student.age is not None:                         
        students[student_id]["age"] = student.age

    if student.course is not None:                      
        students[student_id]["course"] = student.course

    return students[student_id]                         #? Return the updated student data


#? advanced PUT method with query parameter
@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found") #? Return error if not found

        #* Three steps to update only provided fields
        #* 1. Get the existing data using the student_id
    existing_student_data = students[student_id]   

        #* 2. Convert the incoming model to a dict, but exclude fields that were not sent (None)
    update_data = student.model_dump(exclude_unset=True) 
    
        #* 3. Merge the new data into the old dictionary
    existing_student_data.update(update_data)  
    return existing_student_data


#? --------------------------------
#? DELETE method example
#? --------------------------------

@app.delete("/delete-student/{student_id}")          #? Endpoint to delete a student with given student_id
def delete_student(student_id: int):                 #? student_id from path
    if student_id not in students:                    #? Check if student_id exists
        return {"error": "Student not found"}         #? Return error if not found

    del students[student_id]                          #? Delete the student from the dictionary
    return {"message": "Student deleted successfully"}#? Return success message





















































