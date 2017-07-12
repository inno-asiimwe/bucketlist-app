import unittest
from app.classes.planner import Planner

class TestPlanner(unittest.TestCase):
    """Class to handle tests for the planner class"""

    def SetUp(self):
        self.plan = Planner()
    
    def test_create_user_success(self):
        """Test a user is created successfully"""
        self.plan.create_user('Innocent', 'Asiimwe', 'inno', '1234', 'asiimwe@outlook.com')
        self.assertEqual(len(self.plan.users),1, msg = "Length of the the users dictionary should be 1")

    def test_create_user_fail(self):
        """Test failure due to duplicate username"""
        user1 = self.plan.create_user('Innocent', 'Asiimwe', 'inno', '1234', 'asiimwe@outlook.com')
        user2 = self.plan.create_user('Innocent', 'Leone', 'inno', '1234', 'leone@outlook.com')
        self.assertEqual([user1, user2], ['Success','Fail'])

    




