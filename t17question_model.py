class Question:

    def __init__(self, question , answer):
        self.text = question
        self.answer = answer

new_q = Question("", "False")
print(new_q.text)