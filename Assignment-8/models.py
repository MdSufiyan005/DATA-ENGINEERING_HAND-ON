from connection import connect_to_db

db = connect_to_db()
doctors = db['doctors']

def add_doctor(name, specialization, phone, email):
    doctor = {
        "name":name,
        "specialization":specialization,
        "phone":phone,
        "email":email
    }
    result = doctors.insert_one(doctor)
    print(f"Doctor add with ID: {result.inserted_id}")

def list_doctors():
    data = list(doctors.find({},{"_id":0}))
    return data

def update_doctor(name, field, new_value):
    result = doctors.update_one({"name":name},{"$set":{field:new_value}})
    print("Doctor updated !")

def delete_doctor(name):
    result = doctors.delete_one({"name":name})
    print("Doctor deleted")
    