from flask import Flask,render_template,request
#from flask import render_template
app = Flask(__name__)


tampung = []

@app.route('/', methods=['GET','POST'])
def main():
   
    if request.method == "POST":
        input = str(request.form['input'])
        tampung.append(input)
        print(tampung)
        return render_template('index.html',hg = tampung)
    
    return render_template('index.html',hg =None)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9000)