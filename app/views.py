from app import app
from flask import render_template
from flask import request, redirect

from datetime import datetime 

@app.route("/")
def index():
    return render_template("public/index.html")

@app.route("/about")
def about():
    return render_template("public/about.html") 

#string
name = "Tom" 
# Integer
age = 30 
#lists
langs = ['python', 'java', 'Bash', 'Ruby'] 
 # Dictionary
friends = {
    "Tom" : 20,
    "Jerry" : 30,
    "Neon" : 38,
    "Percy" : 48,
    "Amy" : 27
}
#tuples
colors = ("Red", "Blue") 

# Boolean
cool = False

# Classe
class GitRemote:
    def __init__(self, name, description, domain):
        self.name = name
        self.description = description
        self.domain = domain
    def pull(self):
        return f"Pulling repo {self.name}"
    def clone(self, repo):
        return f"cloing the {repo}"


remote = GitRemote(
    name = "Learning Flask",
    description = "Learn the Flask python web framework",
    domain = "https://github.com/rasanjaya85/flask-microservice.git"
)

#function
def repeat(x, qty=1):
    return x * qty

# date 
date = datetime.utcnow()

#html
html = "<h1>This is HTML </h1>"

#suspicious
suspicious = "<script>alert('Never trust the user input.!')</script>"

@app.route("/jinja")
def jinja():
    my_name = "Neon"
    return render_template("public/jinja.html", name=name, age=age, langs=langs, 
    friends=friends, colors=colors, cool=cool, remote=remote, repeat=repeat, GitRemote=GitRemote, date=date,
    html=html, suspicious=suspicious )

@app.template_filter("clean_date")
def clean_date(date):
    return date.strftime("%d %b %y")


@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        missing = []
        for key, value in request.form.items():
            if value == "":
                missing.append(key)

        if missing:
            feedback = f"Missing field for {', '.join(missing) }" 
            return render_template("public/sign_up.html", feedback=feedback)
        else:
            username = request.form["username"]
            email = request.form["email"]
            password = request.form["password"]
            print(f"{username}, {email}, {password}")

        return redirect(request.url)
    return render_template("public/sign_up.html")

