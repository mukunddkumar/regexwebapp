# app.py

from flask import Flask, render_template, request
import re
from validate_email_address import validate_email

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/results", methods=["POST"])
def results():
    test_string = request.form.get("test_string")
    regex_pattern = request.form.get("regex_pattern")

    # Perform regex matching
    matches = re.findall(regex_pattern, test_string)

    return render_template("results.html", test_string=test_string, regex_pattern=regex_pattern, matches=matches)

@app.route("/validate_email", methods=["POST"])
def validate_email_route():
    email = request.form.get("email")

    # Additional check for a simple email format
    if "@" not in email or "." not in email:
        is_valid = False
    else:
        is_valid = validate_email(email)

    return render_template("email_validation.html", email=email, is_valid=is_valid)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

