from pymongo import MongoClient
from flask import Flask, render_template, flash, url_for, request, session, redirect, jsonify
from calc import compCompatibility


app = Flask(__name__, template_folder='templates')

app.secret_key = "mfl"


client = MongoClient(
    'mongodb+srv://Aditya:1234$@cluster0.rl4qm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
)


db = client["Pyaar_Collection"]
name_collection = db["users"]


@app.route('/')
def index():
    return render_template("pyaar.html")


@app.route('/lovemeter', methods=["GET", "POST"])
def lovemeter():
    percentage = request.args.get('perc')

    if request.method == "POST":
        name1 = request.form.get('name1')
        name2 = request.form.get('name2')
        return redirect(url_for('calculate', name1=name1, name2=name2, ftype="name"))
    
    return render_template("lovemeter.html", perc=percentage)



@app.route('/astromath', methods=["GET", "POST"])
def astromath():
    percentage = request.args.get('perc')
    if request.method == "POST":
        data = request.get_json()
        sign1 = data.get('your_sign')
        sign2 = data.get('partner_sign')
        # print(sign1, sign2)
        return redirect(url_for('calculate', name1=sign1, name2=sign2, ftype="sign"))


    return render_template("astromath.html")



@app.route('/calc')
def calculate():
    # name1 and name2 will take from form
    name1 = request.args.get('name1')  # Get from query parameters
    name2 = request.args.get('name2')
    ftype = request.args.get('ftype')
    
    if not name1 or not name2:
        flash("Please enter both names!", "error")
        return redirect(url_for('lovemeter'))
    
    try:
        percentage = compCompatibility(name1, name2)
        if ftype == 'name':
            name_collection.insert_one({"Name1": name1,
                                        "Name2": name2,
                                        "Percentage": percentage})
            return redirect(url_for('lovemeter', perc=percentage))
        
        if ftype == 'sign':
            name_collection.insert_one({"Sign1": name1,
                                        "Sign2": name2,
                                        "Percentage": percentage})
            return jsonify({"percentage": percentage})



    except ValueError:
        flash("Oops!! Make sure you spell the Names correctly with no special characters!!", "error")
        return redirect(url_for('lovemeter'))



if __name__ == "__main__":
    app.run(debug=True)
