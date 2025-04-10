from flask import Flask, request, jsonify
import pickle
import os

app = Flask(__name__)

model = pickle.load(open(os.path.join("model", "classifier.pkl"), "rb"))

@app.route("/prediction", methods=["POST"])
def predict():
    data = request.get_json()
    Gender = 0 if data['Gender'] == "Male" else 1
    Married = 0 if data['Married'] == "Unmarried" else 1
    Credit_History = 0 if data['Credit_History'] == "Unclear Debts" else 1
    ApplicantIncome = data['ApplicantIncome']
    LoanAmount = data['LoanAmount']

    result = model.predict([[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]])
    return jsonify({"loan_approval_status": "Approved" if result[0] == 1 else "Rejected"})

if __name__ == "__main__":
    app.run(port=5000)
