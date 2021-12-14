from app import app
from flask import render_template


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
cool = True 

# Classe
class GitRemote:
    def __init__(self, name, description, domain):
        self.name = name
        self.description = description
        self.domain = domain

    def clone(self, repo):
        return f"cloing the {repo}"


remote = GitRemote(
    name = "Learning Flask"
    description = "Learn the Flask python web framework"
    domain = "https://github.com/
)

@app.route("/jinja")
def jinja():
    my_name = "Neon"
    return render_template("public/jinja.html", my_name=my_name)