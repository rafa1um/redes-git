class Question(object):

    def __init__(self, questionID, questionText, ans1, ans2, ans3, ans4, rightAns):
        self.questionID = questionID
        self.questionText = questionText
        self.ans1 = ans1
        self.ans2 = ans2
        self.ans3 = ans3
        self.ans4 = ans4
        self.rightAns = rightAns

    def get_questionID(self):
        return self.questionID

    def get_questionText(self):
        return self.questionText

    def get_ans1(self):
        return self.ans1

    def get_ans2(self):
        return self.ans2

    def get_ans3(self):
        return self.ans3

    def get_ans4(self):
        return self.ans4

    def get_rightAns(self):
        return self.rightAns
