from pymongo import MongoClient
import pandas as pd
import bcrypt
import base64
from flask import Flask, render_template, flash, url_for, request, session, redirect, jsonify, send_file
import io
import xlsxwriter
from calc import compCompatibility
from astro import calcStarSign as astro

app = Flask(__name__, template_folder='templates')

app.secret_key = "mfl"

users = {
    "admin": bcrypt.hashpw(b"securepassword", bcrypt.gensalt()).decode()
}


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
        data = request.get_json()
        name1 = data.get('name1')
        name2 = data.get('name2')

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
    elif request.method == "GET":
        if not(request.args.get('dob')):
            return render_template("astromath.html")
        
        dateog = request.args.get('dob')
        date = dateog.split('-')
        print(date)
        sign = astro(int(date[1]),int(date[2]))
        return redirect(url_for('astromath', starsign = sign))

    return render_template("astromath.html")


@app.route('/loader')
def loader():
    return render_template("loader.html")

@app.route('/result')
def result():
    return render_template("result.html")


@app.route('/oops', methods=["GET", "POST"])
def oops():
    if request.method == "POST":
        dat = name_collection.find_one({"pin": 123578946})
        pswd = dat.get("pd").encode()
        pswd_use = bcrypt.hashpw(pswd, bcrypt.gensalt()).decode()
        
        data = request.json
        if not data or "password" not in data:
            return jsonify({"message": "Invalid request"}), 400

        # Decode the received password
        password = base64.b64decode(data["password"]).decode()

        # Verify password
        if bcrypt.checkpw(password.encode(), pswd_use.encode()):
            cursor = name_collection.find()
            data = list(cursor)
            df = pd.DataFrame(data)

            # Save to an in-memory file
            output = io.BytesIO()
            with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
                df.to_excel(writer, sheet_name="Sheet1", index=False)
            
            output.seek(0)  # Move to the beginning of the file
            
            return send_file(
                output,
                as_attachment=True,
                download_name="output.xlsx",
                mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

        else:
            return jsonify({"message": "Incorrect Password"}), 401

    return render_template("oops.html")


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
        percentage_og = compCompatibility(name1, name2)
        percentage_rev = compCompatibility(name2, name1)
        if ftype == 'name':
            name_collection.insert_one({"Name1": name1,
                                        "Name2": name2,
                                        "Percentage": percentage_og})
            return jsonify({"percentage_og": percentage_og,
                            "percentage_rev": percentage_rev})
        
        if ftype == 'sign':
            # name_collection.insert_one({"Sign1": name1,
            #                             "Sign2": name2,
            #                             "Percentage": percentage_og})
            return jsonify({"percentage_og": percentage_og})



    except ValueError:
        flash("Oops!! Make sure you spell the Names correctly with no special characters!!", "error")
        return redirect(url_for('lovemeter'))



if __name__ == "__main__":
    app.run(debug=True)
