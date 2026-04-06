from pyscript import document, display

class StudentManager:
    def __init__(self):
        self.students = []

    # ADD STUDENT METHOD
    def addStudent(self, e):
        name = document.getElementById("name").value.strip()
        section = document.getElementById("section").value.strip()
        fsub = document.getElementById("fsub").value.strip()

        output = document.getElementById("output")

        # Validation
        if not name or not section or not fsub:
            output.innerHTML = "<div class='alert alert-danger'>Please fill all fields.</div>"
            return

        student = {
            "name": name,
            "section": section,
            "fsub": fsub
        }

        self.students.append(student)

        output.innerHTML = "<div class='alert alert-success'>Classmate added successfully!</div>"

        # Clear inputs
        document.getElementById("name").value = ""
        document.getElementById("section").value = ""
        document.getElementById("fsub").value = ""

    # SHOW STUDENTS METHOD
    def showStudents(self, e):
        output = document.getElementById("output")

        if len(self.students) == 0:
            output.innerHTML = "<div class='alert alert-warning'>No classmates yet.</div>"
            return

        html = "<h5>Student List</h5><hr>"

        for i, student in enumerate(self.students):
            html += f"""
            <div class="card mb-2 p-2">
                <strong>Classmate {i+1}</strong><br>
                Name: {student['name']}<br>
                Section: {student['section']}<br>
                Favourite Subject: {student['fsub']}
            </div>
            """

        output.innerHTML = html


# Create ONE object
manager = StudentManager()

# Wrapper functions for py-click
def addStudent(e):
    manager.addStudent(e)

def showStudents(e):
    manager.showStudents(e)
