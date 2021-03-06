import unittest

from mock import patch

from api import Wikipedia, ParseError
from definitions import Definitions

class WikiDefTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # def test_article_success(self):
    #     article = Definitions.article("Robot")        
    #     self.assertIn("mechanical", article)

    # def test_missing_article_failure(self):
    #     missing_article_title = "!!!!!-NonExistentArticle"
    #     self.assertRaises(ParseError, Definitions.article, missing_article_title)

    # patch with a decorator
    # @patch.object(Wikipedia, 'article')
    @patch('definitions.Wikipedia.article')
    def test_article_success_decorator_mocked(self, mock_method):
        article = Definitions.article("Robot")        
        mock_method.assert_called_once_with("Robot")

    # patch with a context manager
    def test_article_success_context_manager_mocked(self):
        with patch.object(Wikipedia, 'article') as mock_method:
            article = Definitions.article("Robot")        
            mock_method.assert_called_once_with("Robot")

    # have the mocked object return mocked data
    @patch('definitions.Wikipedia.article')
    def test_article_contents_mocked(self, mock_method):
        mock_method.return_value = "A robot is mechanical"
        article = Definitions.article("Robot")
        self.assertIn("mechanical", article)



