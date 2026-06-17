from flask import Flask, render_template, request

app = Flask(__name__)

jobs = {
    "python": ["Python Developer", "Data Analyst"],
    "html": ["Frontend Developer"],
    "css": ["Frontend Developer"],
    "javascript": ["Frontend Developer", "Web Developer"],
    "sql": ["Database Administrator", "Data Analyst"],
    "react": ["React Developer"],
    "pandas": ["Data Analyst"],
    "numpy": ["Machine Learning Intern"]
}


@app.route("/")
def home():
    return render_template("index1.html")


@app.route("/recommend", methods=["POST"])
def recommend():

    skills = request.form["skills"].lower()

    skill_list = skills.split(",")

    recommended_jobs = []

    for skill in skill_list:

        skill = skill.strip()

        if skill in jobs:

            for job in jobs[skill]:

                if job not in recommended_jobs:
                    recommended_jobs.append(job)

    return render_template(
        "index1.html",
        jobs=recommended_jobs
    )


if __name__ == "__main__":
    app.run(debug=True)