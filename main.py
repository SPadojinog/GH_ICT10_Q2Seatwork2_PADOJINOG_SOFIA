# Student Grade Calculator
from pyscript import display, document

def student_grade_calculator(e):
    result_element = document.getElementById('grade_result')
    result_element.innerHTML = ""

    # Student Info
    firstname = document.getElementById('student_firstname').value.strip()
    lastname = document.getElementById('student_lastname').value.strip()
    fullname = f"{firstname} {lastname}".strip()

    # Subject Grades
    SCI = float(document.getElementById('SCI').value)
    ENG = float(document.getElementById('ENG').value)
    MATH = float(document.getElementById('MATH').value)
    ICT = float(document.getElementById('ICT').value)
    PE = float(document.getElementById('PE').value)
    FIL = float(document.getElementById('FIL').value)

    # Subjects and Units
    Subjects = ['Science', 'Math', 'English', 'Information Communication Technology', 'Physical Education', 'Filipino']
    Units = (5, 5, 5, 2, 1, 3)

    # Subject Units
    SCIA = SCI * 5
    ENGA = ENG * 5
    MATHA = MATH * 5
    ICTA = ICT * 2
    PEA = PE * 1
    FILA = FIL * 3

    total_units = 5 + 5 + 5 + 2 + 1 + 3

    # Weighted Average
    average = (SCIA + ENGA + MATHA + ICTA + PEA + FILA) / total_units

    # Summary Display
    summary = f"""
    👤 <b>Name:</b> {fullname}<br><br>

    📘 <b>Subject Grades:</b><br>
    🧪 Science = {SCI}<br>
    🗣️ English = {ENG}<br>
    ➗ Math = {MATH}<br>
    💻 ICT = {ICT}<br>
    🤸 PE = {PE}<br>
    🇵🇭 Filipino = {FIL}<br><br>

    💯 <b>General Weighted Average:</b> {average:.2f}
    """

    result_element.innerHTML = summary
