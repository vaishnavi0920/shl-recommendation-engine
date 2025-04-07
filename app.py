import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample SHL product catalog
data = [
    {
        "name": "Verify G+ (General Ability)",
        "type": "Cognitive",
        "roles": ["Analyst", "Engineer", "Developer"],
        "levels": ["Entry", "Mid"],
        "skills": ["Problem Solving", "Numerical Reasoning", "Logical Thinking"]
    },
    {
        "name": "OPQ (Occupational Personality Questionnaire)",
        "type": "Personality",
        "roles": ["All"],
        "levels": ["Entry", "Mid", "Senior", "Executive"],
        "skills": ["Leadership", "Teamwork", "Adaptability"]
    },
    {
        "name": "Customer Service SJT",
        "type": "Situational Judgment",
        "roles": ["Customer Service", "Support"],
        "levels": ["Entry", "Mid"],
        "skills": ["Customer Focus", "Decision Making"]
    },
    {
        "name": "Sales Potential Assessment",
        "type": "Behavioral",
        "roles": ["Sales", "Account Manager"],
        "levels": ["Entry", "Mid", "Senior"],
        "skills": ["Persuasion", "Drive", "Results Orientation"]
    }
]

@app.route("/recommend", methods=["POST"])
def recommend():
    input_data = request.json
    role = input_data.get("role")
    level = input_data.get("level")
    skills = input_data.get("skills", [])

    recommendations = []

    for product in data:
        role_match = role in product["roles"] or "All" in product["roles"]
        level_match = level in product["levels"]
        skill_match = any(skill in product["skills"] for skill in skills)

        if role_match and level_match and skill_match:
            recommendations.append({
                "name": product["name"],
                "type": product["type"],
                "matched_skills": list(set(product["skills"]).intersection(skills))
            })

    return jsonify(recommendations)

if __name__ == "__main__":
    app.run(debug=True)
