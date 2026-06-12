class Address:
    def __init__(self, street, city, zipCode):
        self.street = street
        self.city = city
        self.zipCode = zipCode

    def display(self):
        return f"{self.street}, {self.city} - {self.zipCode}"


class Student:
    def __init__(self, name, age, address, courses=None):
        self.name = name
        self._age = None   # protected attribute
        self.age = age     # setter will validate
        self.address = address  # Composition (HAS-A relationship)

        # Mutable list (important concept)
        if courses is None:
            self.courses = []
        else:
            self.courses = courses

    # Property for age (data validation)
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value <= 0 or value > 120:
            raise ValueError("Age must be between 1 and 120")
        self._age = value

    # Add course (mutable behavior)
    def add_course(self, course):
        self.courses.append(course)

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address.display()}")
        print(f"Courses: {', '.join(self.courses) if self.courses else 'None'}")


# Inheritance
class ScholarshipStudent(Student):
    def __init__(self, name, age, address, scholarshipAmount, courses=None):
        super().__init__(name, age, address, courses)
        self.scholarshipAmount = scholarshipAmount

    # Overriding display()
    def display(self):
        super().display()
        print(f"Scholarship Amount: ₹{self.scholarshipAmount}")


# ---------------- TESTING ----------------

# Create Address object (Composition)
addr = Address("Gandhi Road", "Guwahati", "781001")

# Create Student
student1 = Student("Gouriniban", 19, addr)

# Add courses (mutable behavior)
student1.add_course("Mathematics")
student1.add_course("Programming")

print("----- Student Details -----")
student1.display()

# Create ScholarshipStudent
sch_student = ScholarshipStudent("Rahul", 20, addr, 50000)

# Add courses
sch_student.add_course("AI")
sch_student.add_course("Machine Learning")

print("\n----- Scholarship Student Details -----")
sch_student.display()

# Demonstrating mutable behavior (same list persists)
print("\n----- Checking Mutable Behavior -----")
student1.add_course("Physics")
student1.display()