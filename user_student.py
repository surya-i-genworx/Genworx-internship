# Base class
class User:
    def __init__(self, name):
        self.name = name

    def get_role(self):
        return "Generic User"

    def greet(self):
        return f"Hello, {self.name}! You are a {self.get_role()}."


# Student class (inherits from User)
class Student(User):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id
        self.scores = {}  # dictionary to store exam_name: score

    def get_role(self):
        return "Student"

    def greet(self):
        return f"Hey {self.name} (ID: {self.student_id}), welcome back to class!"

    def add_score(self, exam_name, score):
        self.scores[exam_name] = score

    def calculate_average(self):
        if not self.scores:
            return 0.0
        return sum(self.scores.values()) / len(self.scores)

    def display_scores(self):
        return f"{self.name}'s Scores: {self.scores}"


# Staff class (inherits from User)
class Staff(User):
    def __init__(self, name, staff_id):
        super().__init__(name)
        self.staff_id = staff_id

    def get_role(self):
        return "Staff"

    def greet(self):
        return f"Hello Professor {self.name} (Staff ID: {self.staff_id})."

    def update_score(self, student, exam_name, score):
        if isinstance(student, Student):
            student.add_score(exam_name, score)
            print(f"Score updated: {student.name} scored {score} in {exam_name}")
        else:
            print("Only Student scores can be updated.")


# Run the script
if __name__ == "__main__":
    user = User("Aryan")
    student = Student("Surya", "A18407150")
    staff = Staff("Dr. Kumar", "S1002")

    print(user.greet())
    print(student.greet())
    print(staff.greet())

    print("Role of", user.name, ":", user.get_role())
    print("Role of", student.name, ":", student.get_role())
    print("Role of", staff.name, ":", staff.get_role())

    # Staff updates scores for student
    staff.update_score(student, "Math", 88)
    staff.update_score(student, "Science", 92)

    # Student checks their scores and average
    print(student.display_scores())
    print(f"{student.name}'s Average Score: {student.calculate_average():.2f}")
