
from typing import List
from models.disease_model import predict_disease

def parse_prescription_text(text: str):
    lines = text.strip().split('\n')
    medicines = []
    for line in lines:
        if any(char.isdigit() for char in line):
            parts = line.split()
            if len(parts) >= 2:
                medicines.append({
                    "name": parts[0],
                    "dosage": parts[1],
                    "frequency": parts[2] if len(parts) > 2 else "Once daily",
                    "timing": parts[3] if len(parts) > 3 else "Not specified"
                })
    return medicines

def recommend_dosage(meds: List[dict], age: int = 30):
    results = []
    for med in meds:
        if age < 12:
            results.append(f"{med['name']}: Half dosage for children")
        elif age > 60:
            results.append(f"{med['name']}: Consider reduced dosage for elderly")
        else:
            results.append(f"{med['name']}: Normal dosage as prescribed")
    return "\n".join(results)

def suggest_nutrition(meds: List[dict]):
    advice = []
    for med in meds:
        name = med['name'].lower()
        if 'paracetamol' in name:
            advice.append("Drink plenty of water; avoid alcohol.")
        elif 'antibiotic' in name:
            advice.append("Eat probiotic-rich foods like yogurt.")
        else:
            advice.append("Eat balanced meals with fruits and vegetables.")
    return "\n".join(advice)

def analyze_prescription_text(text: str):
    medicines = parse_prescription_text(text)
    age_check = recommend_dosage(medicines)
    disease = predict_disease(text)
    diet = suggest_nutrition(medicines)
    workout = "Light walking or yoga unless advised otherwise."

    return {
        "medicines": medicines,
        "age_limit_check": age_check,
        "predicted_disease": disease,
        "diet": diet,
        "workout": workout
    }
