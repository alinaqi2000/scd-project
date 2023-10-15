import json
import os

file_name = "students_data.json"


def save_student_record(student):
    data = get_data()
    unique_key = generate_unique_key(data)
    data[unique_key] = student
    set_data(data)
    return {unique_key: student}


def get_student_record(key):
    data = get_data()
    if data.get(key):
        return data.get(key)
    else:
        return {"error": "Invalid Student ID!"}


def update_student_record(key, student):
    data = get_data()
    if data.get(key):
        data[key] = student
        set_data(data)
        return {key: student}
    else:
        return {"error": "Invalid Student ID!"}


def get_all_students_record():
    return get_data()


def delete_student_record(key):
    data = get_data()
    if data.get(key):
        data.pop(key)
        set_data(data)
        return data
    else:
        return {"error": "Invalid Student ID!"}


def generate_unique_key(data):
    key = len(data) + 1
    while data.get("student" + str(key)):
        key += 1
    return "student" + str(key)


def get_data():
    return json.loads(open(file_name, "r").read()) if os.path.isfile(file_name) and os.path.getsize(file_name) > 0 else {}


def set_data(data):
    write_file = open(file_name, "w")
    return json.dump(data, write_file, indent=6)
