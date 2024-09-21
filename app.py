from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    final_grade = None
    if request.method == "POST":
        try:
            attendance = float(request.form["attendance"]) * 0.1
            recitation = float(request.form["recitation"]) * 0.4
            quiz = float(request.form["quiz"]) * 0.3
            requirements = float(request.form["requirements"]) * 0.3
            prelim_exam = float(request.form["prelim_exam"]) * 0.6

            performance_task = recitation + quiz + requirements
            overall_performance = performance_task * 0.3
            final_grade = round(attendance + overall_performance + prelim_exam, 2)
        except ValueError:
            final_grade = "Invalid input. Please enter numbers only."

    return render_template("index.html", final_grade=final_grade)

if __name__ == "__main__":
    app.run(debug=True)
