from flask import Flask,render_template,request
from model import restore_model
from forms import Form
from model import restore_model
import numpy as np
app = Flask(__name__)
app.secret_key = 'development key'
@app.route('/', methods=['GET', 'POST'])
def home():
    form = Form(request.form)
    if request.method == 'POST' : #and form.validate():
        test_values = np.array([[form.pregnancies.data,form.glucose.data,form.bloodPressure.data,form.skinThickness.data,form.insulin.data,form.bmi.data,form.diabetesPedigreeFunction.data,form.age.data],], dtype=np.float32)
        result = restore_model(test_values)
    else:
        result = None
    return render_template('home.html', form=form, result=result)

if __name__ == '__main__':
   app.run(debug = True)
