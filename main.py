from pyscript import document

def calculate_gwa(event=None):
    student_info = document.getElementById("student_info")
    summary_div = document.getElementById("summary")
    output_div = document.getElementById("output")

    student_info.innerHTML = ""
    summary_div.innerHTML = ""
    output_div.innerHTML = ""
    student_info.classList.remove("show")
    summary_div.classList.remove("show")
    output_div.classList.remove("show")

    subjects = [
        "Science", "Math", "English", "Filipino", "Social Studies",
        "TLE", "ICT", "LT", "Values Education", "PE", "Music"
    ]
    units = [5, 5, 5, 3, 3, 2, 2, 2, 1, 1, 1]

    first = document.getElementById("first_name").value.strip()
    last = document.getElementById("last_name").value.strip()

    grade_ids = [
        "science", "math", "english", "filipino", "social_studies",
        "tle", "ict", "lt", "values_ed", "pe", "music"
    ]
    values = [document.getElementById(i).value.strip() for i in grade_ids]

    if not first or not last or any(v == "" for v in values):
        output_div.innerHTML = "<span style='color:red;'>Please input your name and all grades before calculating.</span>"
        output_div.classList.add("show")
        return

    try:
        grades = []
        for v in values:
            num = float(v)
            if num < 0 or num > 100:
                output_div.innerHTML = "<span style='color:red;'>Grades must be between 0 and 100.</span>"
                output_div.classList.add("show")
                return
            grades.append(num)
    except ValueError:
        output_div.innerHTML = "<span style='color:red;'>Make sure all grades are numbers.</span>"
        output_div.classList.add("show")
        return

    weighted_sum = sum(g * u for g, u in zip(grades, units))
    total_units = sum(units)
    gwa = weighted_sum / total_units

    summary = "<br>".join(f"{sub}: {g:.0f}" for sub, g in zip(subjects, grades))
    student_info.innerHTML = f"<b>Name:</b> {first} {last}"
    summary_div.innerHTML = f"<b>Grades Summary:</b><br>{summary}"
    output_div.innerHTML = f"<b>General Weighted Average:</b> {gwa:.2f}"

    student_info.classList.add("show")
    summary_div.classList.add("show")
    output_div.classList.add("show")
