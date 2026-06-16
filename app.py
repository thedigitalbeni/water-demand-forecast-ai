from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
        
@app.route("/")
def home():

    return render_template("index.html")


@app.route("/main")
def main():

    return render_template("main.html")


@app.route("/aboutus")
def aboutus():

    return render_template("about_us.html")
# @app.route("/structure")
# def structure():

#     return render_template("structure.html")


# @app.route("/periodic_stable")
# def periodic_table():

#     return render_template("periodic_table.html")


@app.route('/result', methods =["GET", "POST"])
def my_form_post():
    
    year = int(request.args["year"])
    month = int(request.args["month"])
    day = int(request.args["day"])

    return render_template("result.html",
                           predicted=model.predict([[year,month,day]])[0])
 


if "__main__" == __name__:
    app.run(host="0.0.0.0", debug=True)
