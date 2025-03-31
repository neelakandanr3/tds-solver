def get_answer(question: str, file):
    answers = {
        "Example Question 1": "Example Answer 1",
        "Example Question 2": "Example Answer 2",
    }
    return answers.get(question, "Question not found")
