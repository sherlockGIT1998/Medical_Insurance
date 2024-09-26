from flask import Flask,render_template,request,jsonify

from utils import MedicalInsurance

app = Flask(__name__)

@app.route('/')

def hello_flask():
    print('Medical Insurance Prediction System')
    
    return render_template('index.html')

@app.route('/predict_cahrges',methods=['POST','GET'])
def get_insurance_charges():
    if request.method == 'GET':
        print('GET MEthod')
        
        # data = request.form
        # age = eval(data[age])
        # sex = data[age]
        # bmi = eval(data[bmi])
        # children = eval(data[children])
        # smoker = data[smoker]
        # region = data[region]
        
        age = eval(request.args.get('age'))
        sex = request.args.get('sex')
        bmi = eval(request.args.get('bmi'))
        children = eval(request.args.get('children'))
        smoker = request.args.get('smoker')
        region = request.args.get('region')
        
        med_ins = MedicalInsurance(age,sex,bmi,children,smoker,region)
        
        charges = med_ins.get_predicted_charges()
        
        return render_template('index.html',prediction=charges)
        
        # return f'Medical Charges : Rs round{charges,2} /-.'
    
if __name__ == '__main__':
    
    app.run()