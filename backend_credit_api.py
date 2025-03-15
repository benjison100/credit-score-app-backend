
from flask import Flask, jsonify
import random

app = Flask(__name__)

# Sample loan offers
LOAN_OFFERS = [
    {"name": "Low-Interest Loan", "rate": 5.2},
    {"name": "Business Expansion Loan", "rate": 7.8},
    {"name": "Personal Loan", "rate": 10.5},
]

@app.route("/api/credit-score", methods=["GET"])
def get_credit_score():
    score = random.randint(300, 850)  # Simulate credit score
    offers = [offer for offer in LOAN_OFFERS if score > 500]  # Basic filtering
    return jsonify({"score": score, "loanOffers": offers})

if __name__ == "__main__":
    app.run(debug=True)
