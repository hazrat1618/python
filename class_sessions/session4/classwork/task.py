
students = {
    1:{"first_name": "John", "last_name": "Doe", "dob": "01/01/2000"},
    2:{"first_name": "Alex", "last_name": "Poatan", "dob": "02/02/2000"},
    3:{"first_name": "Steve", "last_name": "Robin", "dob": "01/03/2000"},

}

for key, value in students.items():
    print(f"Hello I'm {value['first_name']} {value['last_name']}. I was born in {value['dob']}.")
    print(f"I'm the student number{key}")
