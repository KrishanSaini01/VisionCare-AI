from ai.gemini import generate_ai_response


def fallback_chat(question):

    question = question.lower()

    if "pneumonia" in question:
        return (
            "Pneumonia is a lung infection that causes inflammation "
            "of the air sacs. Symptoms include fever, cough, chest pain "
            "and difficulty breathing."
        )

    elif "normal" in question:
        return (
            "A NORMAL prediction means the AI model did not detect "
            "significant signs of pneumonia."
        )

    elif "medicine" in question:
        return (
            "Please take medicines only as prescribed by a qualified doctor."
        )

    elif "diet" in question:
        return (
            "Drink plenty of water, eat fruits, vegetables and protein-rich food."
        )

    elif "exercise" in question:
        return (
            "Light walking and breathing exercises are generally beneficial, "
            "but consult your doctor first."
        )

    return (
        "I'm sorry, I couldn't understand your question. "
        "Please consult a healthcare professional for medical advice."
    )


def ask_medical_ai(question):

    try:
        return generate_ai_response(question)

    except Exception:

        return fallback_chat(question)