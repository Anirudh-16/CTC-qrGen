from distutils.log import debug
from qrgen import qrgen
from flask import *

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/qrconvert',methods=['POST'])
def convert():
    global url
    url = request.form['url']
    return render_template("index.html")

@app.route('/download',methods=['POST','GET'])
def qr_download():
    filename=qrgen(url)
    
    return send_file(filename,as_attachment=True)

# @app.route('/qrconvert',methods=['POST','GET'])
# def convert():
#     global url
#     url = request.form['url']
#     filename=qrgen(url)

#     return send_file(filename,as_attachment=True)
#     # return render_template("index.html")

if __name__=="__main__":
    app.run(host='0.0.0.0',port='5000')