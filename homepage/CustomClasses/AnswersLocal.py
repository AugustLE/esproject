class AnswersLocal:

    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.answers = []

    def addAnswer(self, answer):
        self.answers.append(answer)


    def getAnswers(self):
        return self.answers


    def getName(self):
        return self.name


    def getId(self):
        return self.id