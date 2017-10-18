class QuestionLocal:

    def __init__(self, questionText, isOptions):

        self.questionText = questionText
        self.isOptions = isOptions
        self.options = []


    def addOption(self, option):

        self.options.append(option)


    def getQuestionText(self):

        return self.questionText

    def getOptions(self):

        return self.options