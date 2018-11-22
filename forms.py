# importing libraries
from flask_wtf import Form
from wtforms import IntegerField, SubmitField
from wtforms import validators, ValidationError
# create a form
class Form(Form):
   pregnancies = IntegerField("Number of pregnancies",[validators.Required("Please enter the number of times you were pregnet.")])
   glucose = IntegerField("Plasma glucose concentration in oral glucose tolerance test",[validators.Required("Please enter Plasma glucose concentration.")])
   bloodPressure = IntegerField("Diastolic blood pressure (mm Hg)",[validators.Required("Please enter Diastolic blood pressure in mm Hg.")])
   skinThickness = IntegerField("Triceps skin fold thickness (mm)",[validators.Required("Please enter Triceps skin fold thickness in mm.")])
   insulin = IntegerField("2-Hour serum insulin (mu U/ml)",[validators.Required("Please enter 2-Hour serum insulin in mu U/ml.")])
   bmi = IntegerField("Body mass index ",[validators.Required("Please enter BMI index.")])
   diabetesPedigreeFunction = IntegerField("Diabetes Pedigree Function ",[validators.Required("Please enter Diabetes Pedigree Function.")])
   age = IntegerField("Age ",[validators.Required("Please enter your age.")])
   submit = SubmitField("Send")
