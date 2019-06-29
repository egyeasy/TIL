# 1. csv, nested-list(중첩된 리스트) version

student1 = [
    ['id', 'name', 'phone', 'address'],
    [1, '강동주', '01023456789', '서울'],
    [2, '임동영', '01023233232', '서울']
]


# 2. json(nosql), dictionary version

student2 = [
    {'id': 1, 'name': '강동주', 'phone': '01023456789', 'address': '서울'},
    {'id': 2, 'name': '임동영', 'phone': '01023233232', 'address': '서울'},
]


# 3. object version

class Student:
    def __init__(self, id_num, name, phone, address):
        self.id_num = id_num
        self.name = name
        self.phone = phone
        self.address = address

student3 = [
    Student(1, '강동주', '01023456789', '서울'),
    Student(2, '임동영', '01023233232', '서울')
]

# Object Relational Mapping

# Create
Student.new()

# Read
Student.get()

# Update
Student.update()

# Delete
Student.destroy()