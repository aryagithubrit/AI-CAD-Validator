from flask import Flask, request, jsonify
from flask_cors import CORS

# Create app
app = Flask(__name__)
CORS(app)

# Validation logic
def validate_design(data):
    errors = []
    warnings = []
    suggestions = []

    thickness = data["thickness"]
    hole = data["hole_diameter"]
    width = data["width"]

    if thickness < 3:
        errors.append("Thickness too low (<3mm)")
        suggestions.append("Increase thickness to at least 4mm")

    if hole > thickness:
        warnings.append("Hole too large compared to thickness")
        suggestions.append("Reduce hole size or increase thickness")

    if thickness < 0.05 * width:
        warnings.append("Thickness too low for given width")

    return errors, warnings, suggestions


# Score logic
def calculate_score(data):
    score = 10

    if data["thickness"] < 3:
        score -= 3

    if data["hole_diameter"] > data["thickness"]:
        score -= 2

    return max(score, 0)


# API route
@app.route("/validate", methods=["POST"])
def validate():
    data = request.json

    errors, warnings, suggestions = validate_design(data)
    score = calculate_score(data)

    return jsonify({
        "errors": errors,
        "warnings": warnings,
        "suggestions": suggestions,
        "score": score
    })


# Run server
if __name__ == "__main__":
    app.run(debug=True)