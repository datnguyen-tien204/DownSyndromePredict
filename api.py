from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the machine learning model
model = joblib.load("Naive_Bayes.sav")

@app.route("/", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        # Get the input data from the form
        data = []
        for i in range(1, 12):  # Assuming you have 11 input fields in the form
            data.append(float(request.form[f"input{i}"]))

        # Make the prediction using the loaded model
        prediction = model.predict([data])[0]

        # You can process the prediction further or return it directly to the user
        return f"Predicted output: {prediction}"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
