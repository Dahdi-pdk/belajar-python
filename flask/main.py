from flask import Flask,url_for,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return "This is an about page."
if __name__ == "__main__":
    app.run(debug=True,host='127.0.0.1',port=5000, use_reloader=True, threaded=True, processes=1, passthrough_errors=True, )