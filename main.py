from flask import Flask,render_template,request
from model import restore_model
from forms import Form
from model import restore_model
import numpy as np
app = Flask(__name__)
app.secret_key = 'development key'
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect.html', methods=['GET', 'POST'])
def detect():
    form = Form(request.form)
    if request.method == 'POST' : #and form.validate():
        test_values = np.array([[form.pregnancies.data,form.glucose.data,form.bloodPressure.data,form.skinThickness.data,form.insulin.data,form.bmi.data,form.diabetesPedigreeFunction.data,form.age.data],], dtype=np.float32)
        result = restore_model(test_values)
        print("************")
        if(result):
            result = "Time to go Sugar Free"
        else:
            result = "Time for dessert"
    else:
        result = None
    iframe = 'details.html'

    return render_template('detect.html', form=form, result=result,iframe=iframe)

@app.route('/details.html')
def details():
    return render_template('details.html')

@app.route('/dashboard.html')
def dashboard():
    return render_template('dashboard.html')



if __name__ == '__main__':
   app.run(debug = True)
