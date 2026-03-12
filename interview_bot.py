questions = [
"Tell me about yourself",
"Why do you want to join this company?",
"What are your strengths?",
"What is your experience with Python?"
]

def get_next_question(index):

    if index < len(questions):
        return questions[index]

    return "Thank you. Our HR team will contact you soon."