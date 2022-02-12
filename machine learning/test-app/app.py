# Importing the libraries
import pickle
from flask import Flask, render_template, request
import numpy as np

# Global Variables
app = Flask(__name__)
loaded_model = pickle.load(open('model.pkl', 'rb'))

# Routes
@app.route("/", methods=["GET"])
def home():
    return render_template("form.html")


@app.route("/prediction", methods=["POST"])
def prediction():
    bmi = request.form["bmi"]
    age = request.form["age"]
    glucose = request.form["glucose"]

    prediction = loaded_model.predict([[glucose, bmi, age]])[0]
    probability = loaded_model.predict_proba([[glucose, bmi, age]])
    probability = str(np.round(probability.max() * 100, 2)) + "%"
    
    if prediction == 0:
        prediction = "Not Diabetic " + probability 
    else:
        prediction = "Diabetic " + probability

    return render_template("form.html", output=prediction)

# Main function
if __name__ == '__main__':
    app.run(debug=True)