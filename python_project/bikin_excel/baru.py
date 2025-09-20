from flask import Flask,request,render_template,jsonify
from openpyxl import load_workbook
app = Flask(__name__)

# variabel kolom 
nomor = []
nama = []
alamat = []
#memuat / loading workbook
lembar = load_workbook('ini.xlsx')
kolom = lembar['Sheet']

#bagian rute website
@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        InputNomor = int(request.form['nomor'])
        InputNama  = request.form['nama']
        InputAlamat=request.form['alamat']
        nomor.append(InputNomor)
        nama.append(InputNama)
        alamat.append(InputAlamat)
        print(nomor,'\n',nama,'\n',alamat)
        return render_template('index.html',nomor=nomor,nama=nama,alamat=alamat)
    return render_template('/index.html',nomor=None,nama=None,alamat=None)

@app.route('/kompile',methods=["GET"])
def kompile():
    o=True
    while o:
        for i in range(max(nomor)):
            baris = i + 1
            noBarisA = f'A{baris}'
            noBarisB = f'B{baris}'
            noBarisC = f'C{baris}'
            kolom[noBarisA] = baris
            kolom[noBarisB] = nama[i]
            kolom[noBarisC]= alamat[i]
        else:
            o=False
    lembar.save('ini.xlsx')
    print('berhasil')
    return jsonify({'message':'hallo dahdi'})
    
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=9000)


# i = 0
# while (i < 10):
#     print(i)





# lembar.save('ini.xlsx')
# print('berhasil')