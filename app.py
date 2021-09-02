from flask import Flask, render_template,request
import pickle
from flask_cors import CORS,cross_origin


app = Flask(__name__)

model = pickle.load(open('challenge.pickle','rb'))


@app.route('/',methods = ['GET','POST'])
@cross_origin()
def Home():
    return render_template('index.html')

@app.route("/predict",methods=["POST"])
@cross_origin()
def predict():
    if request.method == "POST":
        pt = float(request.form['pt'])
        rt = int(request.form['RT'])
        Torque = float(request.form['Torque'])
        tool = int(request.form['TW'])
        twf = int(request.form['TWF'])
        hdf = int(request.form['HDF'])
        pwf = int(request.form['PWF'])
        osf = int(request.form['OSF'])
        rnf = int(request.form['RNF'])

        result = model.predict([[pt,rt,Torque,tool,twf,hdf,pwf,osf,rnf]])[0]
        return render_template('result.html',result = result)
    else:
        return render_template('index.html')

@app.route('/profile',methods=["POST","GET"])
@cross_origin()
def report():
    return render_template('report.html')

if __name__=="__main__":
    app.run(debug=True)
    