import flask 
from flask import render_template , request

app = flask.Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/halaman_kedua', methods=['GET','POST'])
def halaman2():
    if request.method == 'POST':
        usia = request.form['tahun_lahir']
        o = ['huhuhuh']
        print(type(o))
        return render_template('halaman2.html',h = 'usia kamu adalah', k = exec(usia))
    return render_template('halaman2.html',k=None)

# untuk run project *pastikan berada paling bawah
if __name__ == "__main__":
    app.run(host="0.0.0.0" ,port=5000)


# class op:
#     def __init__(self,k):
#         self.k = "klklk"
        
#     def ui(self):
#         return "klklkl"
# print(op.ui(__name__))
# print(app)