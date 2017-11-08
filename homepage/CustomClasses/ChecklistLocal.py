
class ChecklistLocal:

    def __init__(self, name, id, is_front, is_answered):

        self.name = name
        self.id = id
        self.questions = []
        self.is_front = is_front
        self.is_answered = is_answered


    def addQuestion(self, option):

        self.questions.append(option)

    def getQuestions(self):

        return self.questions

    def getName(self):

        return self.name

    def getId(self):

        return self.id

    def getIsFront(self):

        return self.is_front

    def isAnswered(self):
        return self.is_answered





