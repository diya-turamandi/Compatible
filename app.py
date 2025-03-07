from pymongo import MongoClient
from flask import Flask, render_template, flash, url_for
from calc import compCompatibility


app = Flask(__name__, template_folder='templates')


client = MongoClient(
    'mongodb+srv://Aditya:1234$@cluster0.rl4qm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
)


db = client["Pyaar_Collection"]
name_collection = db["users"]


@app.route('/')
def index():
    return render_template("pyaar.html")


@app.route('/calc', methods=["POST"])
def calculate():
    # name1 and name2 will take from form
    name1 = ""
    name2 = ""

    try:
        comp = compCompatibility(name1, name2)

    except ValueError:
        flash("Oops!! Make sure you spell the Names correctly with no special characters!!", "error")
        return render_template("pyar.html")



if __name__ == "__main__":
    app.run(debug=True)
