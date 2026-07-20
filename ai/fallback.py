def fallback_report(disease, confidence):

    disease = disease.upper()

    if disease == "PNEUMONIA":

        return f"""
Disease Detected : PNEUMONIA

Confidence Score : {confidence}%

About Pneumonia
Pneumonia is a lung infection that causes inflammation of the air sacs.
It may lead to cough, fever, chest pain and difficulty breathing.

Possible Symptoms
• Fever
• Cough
• Chest Pain
• Shortness of Breath
• Fatigue

Precautions
• Drink plenty of fluids.
• Take adequate rest.
• Avoid smoking.
• Follow your doctor's advice.
• Seek medical attention if symptoms worsen.

This AI prediction is not a medical diagnosis.
Please consult a qualified healthcare professional.
"""

    else:

        return f"""
Disease Detected : NORMAL

Confidence Score : {confidence}%

No signs of Pneumonia were detected.

Recommendations
• Continue maintaining a healthy lifestyle.
• Exercise regularly.
• Eat nutritious food.
• Avoid smoking.
• Schedule regular health checkups.

This AI prediction is not a medical diagnosis.
Please consult a qualified healthcare professional.
"""