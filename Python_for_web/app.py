from flask import Flask,render_template,request,redirect,url_for
import os

app = Flask(__name__)
@app.route("/")
def home():
    techs = ["Html","css","Flask","Python"]
    name = "30 days of Python Programming"
    return render_template("Home.html", techs=techs,name =name, title = "Home")

@app.route("/about")
def about():
    name = "30 days of Python Programmming"
    return render_template("About.html", name = name, title ="About us")

@app.route('/result')
def result():
    return render_template('result.html')

@app.route("/post", methods = ["POST","GET"])
def post():
    name= "Text Analyzer"
    if request.method == "GET":
        return render_template("post.html", name=name, title=name)
    if request.method == "POST":
        content = request.form["content"]
        print(content)
        return redirect(url_for("result"))
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(debug = True, host = "0.0.0.0", port = port)
    