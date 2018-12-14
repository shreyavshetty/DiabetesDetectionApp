# DiabetesDetectionApp
### Discription
This is a ML oriented Web Application for detection of the diabetes based on the parameters that the user enters. It predicts whether it is benign or malignant by learning from the parameters. We have developed a deep neural network model to classify if the user has diabetes or not. The model is trained based on the PIMA Indian Diabetes dataset.
### Dataset
the PIMA Indian Diabetes dataset from  National Institute of Diabetes and Digestive and Kidney Diseases; Includes cost data (donated by Peter Turney). The attributes are as follows:
- Number of times pregnant 
- Plasma glucose concentration a 2 hours in an oral glucose tolerance test 
- Diastolic blood pressure (mm Hg) 
- Triceps skin fold thickness (mm) 
- 2-Hour serum insulin (mu U/ml) 
- Body mass index (weight in kg/(height in m)^2)
- Diabetes pedigree function 
- Age (years) 
- Class variable (0 or 1) 
### Technology Used
For the front end HTML5,CSS and bootstrap has been used. Flask based python is the backend. All interactions with the backend are made via RESTful API calls. A python ML model has been used to predict the disease stage. The weights of the trained model are saved and when a call is made to predict the model, inference is done based on the model weights. Iframes have been used to implement Ajax Patterns. 
### What does the application have?
**Homepage**
![alt text](https://github.com/shreyavshetty/DiabetesDetectionApp/blob/master/homepage.jpg "homepage")
**Dashboard**
![alt text](https://github.com/shreyavshetty/DiabetesDetectionApp/blob/master/form.jpg "form")
![alt text](https://github.com/shreyavshetty/DiabetesDetectionApp/blob/master/details.jpg "details")


