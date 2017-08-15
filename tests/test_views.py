"""Module contains tests for the views"""
import unittest
from app import app, url_for
from app.views import PLAN

class BucketlistViewTest(unittest.TestCase):
    """Class handles unit tests for the views"""

    def setUp(self):
        self.test_app = app.test_client(self)
        PLAN.create_user('Innocent', 'asiimwe', 'inno', '123', 'asiimwe@outlook.com')
    def test_index(self):
        """Test '/' """
        with app.app_context():
            response = self.test_app.get(url_for('index'))
            self.assertEqual(response.location, url_for('log_in'))
