import unittest
from surveyClass import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    def test_store_single_response(self):
        question = "Where do you live? "
        survey = AnonymousSurvey(question)
        survey.storeResponse('Nairobi')
        self.assertIn('Nairobi', survey.responses)

    def test_multiple_response(self):
        question = "Where do you live? "
        survey = AnonymousSurvey(question)
        res = ['Nairobi', 'Nakuru', 'Kisumu']
        survey.storeResponse(res)
        self.assertIn(['Nairobi', 'Nakuru', 'Kisumu'], survey.responses)  

if __name__ == '__main__':
    unittest.main()        