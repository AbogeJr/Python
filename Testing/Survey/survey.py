from surveyClass import AnonymousSurvey

question = "Where do you live? Enter 'q' to quit."

my_survey = AnonymousSurvey(question)

my_survey.showQuestion()

while True:
    res = input("Location: ")
    if res == 'q':
        break
    my_survey.storeResponse(res)
print("\nhank you for your time.\nResults:")
my_survey.showResults()    