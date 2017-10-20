
class ChecklistLocal:

    def __init__(self, name, id):

        self.name = name
        self.id = id
        self.questions = []


    def addQuestion(self, option):

        self.questions.append(option)

    def getQuestions(self):

        return self.questions

    def getName(self):

        return self.name

    def getId(self):

        return self.id





