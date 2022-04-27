class AnonymousSurvey:
    def __init__(self, question):
        self.question = question
        self.responses = []

    def storeResponse(self, response):
        self.responses.append(response)

    def showQuestion(self):
        print(self.question)

    def showResults(self):
        print("Results: ")
        for result in self.responses:
            print(f"\t-{result}")

