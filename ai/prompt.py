def generate_prompt(disease, confidence):

    return f"""
You are an experienced medical AI assistant.

A CNN model analyzed a Chest X-ray.

Prediction:
Disease: {disease}
Confidence: {confidence}%

Provide the following:

1. Disease Explanation
2. Possible Symptoms
3. General Precautions
4. Healthy Diet Recommendations
5. When the patient should consult a doctor

Rules:
- Use simple English.
- Keep the response around 200-300 words.
- Do not make absolute medical claims.
- Mention that this is not a substitute for professional medical advice.
"""