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

# @app.route("/jinja")
# def jinja():
#     my_name = "Neon"
#     return render_template("public/jinja.html", name=name, age=age, langs=langs, 
#     friends=friends, colors=colors, cool=cool, remote=remote, repeat=repeat, GitRemote=GitRemote, date=date,
#     html=html, suspicious=suspicious )

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

profile_users = {
    "mitsuhiko": {
        "name": "Anan Ronacher",
        "bio": "Creator of the Flask Framework",
        "twitter_handle": "@mitsuhiko",
    },
    "gvanrossum": {
        "name": "Guido Van Rossum",
        "bio": "Creator of the Python programming language",
        "twitter_handle": "@gvanrossum"
    },
    "elonmusk": {
        "name": "Elon Musk",
        "bio": "technology entrepreneur, investor, and engineer",
        "twitter_handle": "@elonmusk"
    }
}


@app.route("/profile/<username>")
def profile(username):
    profile_user = None
    if username in profile_users:
        profile_user = profile_users[username]
        print(f"{username} is already existing.")
    else:
        print(f"User is invalid")
    return render_template("public/profile.html", username=username, profile_user=profile_user)

from flask import jsonify, make_response

@app.route("/json", methods=["POST"])
def json_data():
    #validate the json data
    if request.is_json:
        req = request.get_json()
        response_body  = {
            "message": "Json Data Recieved.",
            "name": req.get("name")
        }
        print(jsonify(response_body))
        res = make_response(jsonify(response_body), 200) 
        return  res
    else:
        # return with client error(bad request)
        return "Json Data not recieved.", 400


@app.route("/guestbook")
def guestbook():
    return render_template("public/guestbook.html")


@app.route("/guestbook/create-entry", methods=["POST"])
def create_entry():
    req = request.get_json()
    print(req)
    res = make_response(jsonify(req), 200)

    return  res


@app.route("/query")
def query():

    # req = request.values
    # print(",".join(f" {k} : {v} " for k, v in req.items()))
    # return "thanks", 200    
    if request.args:
        req = request.args
        serialized = ", ".join(f"{k} : {v}" for k, v in req.items())
        return f"{serialized}", 200
    else:
        return "No query string recieved.", 200