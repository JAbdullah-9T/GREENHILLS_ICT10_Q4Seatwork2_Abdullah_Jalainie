from pyscript import document, display

students = []

# ADD STUDENT FUNCTION
def addStudent(e):
    name = document.getElementById("name").value
    section = document.getElementById("section").value
    fsub = document.getElementById("fsub").value

    student = {
        "name": name,
        "section": section,
        "fsub": fsub
    }

    students.append(student)

    output = document.getElementById("output")
    output.innerHTML = "<p>Classmate added successfully!</p>"


# SHOW STUDENTS FUNCTION
def showStudents(e):
    output = document.getElementById("output")
    output.innerHTML = "<h5>Student List</h5><br>"

    if len(students) == 0:
        display("No classmates yet.", target="output")
        return

    for i, student in enumerate(students):
        display(f"--- Classmate {i+1} ---", target="output")
        display(f"Name: {student['name']}", target="output")
        display(f"Section: {student['section']}", target="output")
        display(f"Favourite Subject: {student['fsub']}", target="output")
        display("----------------------", target="output")