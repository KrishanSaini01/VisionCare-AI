from ai.gemini import generate_ai_report

response = generate_ai_report(
    disease="PNEUMONIA",
    confidence=40.54
)

print(response)