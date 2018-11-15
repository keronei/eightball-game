import unittest
from eightball import predictor,answers_count

class TestFortune(unittest.TestCase):
    
    def test_idx_error_in_answers_array(self):
        config_file = open('answers.config','r')
        expected = config_file.read()
        config_file.close()
        self.assertTrue(expected != None,'Config answers need not be null')
    
    def test_if_predictor_content_is_null(self):
        self.assertTrue(predictor() != None,'Predictor() must return a prediction')
        
    def test_answers_count(self):
        self.assertEqual(answers_count() , 20,'Lenght of answers must be equal to number of line in config file')
        
                 

if __name__ == '__main__':
    unittest.main()