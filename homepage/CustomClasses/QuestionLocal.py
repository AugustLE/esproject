class QuestionLocal:

    def __init__(self, questionText, isOptions, id):

        self.questionText = questionText
        self.isOptions = isOptions
        self.options = []
        self.id = id


    def addOption(self, option):

        self.options.append(option)


    def getQuestionText(self):

        return self.questionText

    def getOptions(self):

        return self.options

    def setIsOptions(self, isOptions):

        self.isOptions = isOptions

    def getIsOptions(self):

        return self.isOptions

    def getId(self):

        return self.id