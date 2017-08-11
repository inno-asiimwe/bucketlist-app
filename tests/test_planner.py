"""Module contains unit tests for the Planner class"""
import unittest
from app.classes.planner import Planner

class TestPlanner(unittest.TestCase):
    """Class to handle tests for the planner class"""

    def setUp(self):
        """Setting up a user and Planner object for every test"""
        self.plan = Planner()
        self.plan.create_user('Jane', 'Jackson', 'jane', '123', 'j@j.com')
    def test_create_user_success(self):
        """Test a user is created successfully"""
        self.plan.create_user('Innocent', 'Asiimwe', 'inno', '1234', 'asiimwe@outlook.com')
        self.assertEqual(len(self.plan.users), 2,
                         msg="Length of the the users dictionary should be 2")

    def test_create_user_fail(self):
        """Test failure due to duplicate username"""
        user1 = self.plan.create_user('Innocent',
                                      'Asiimwe',
                                      'inno',
                                      '1234',
                                      'asiimwe@outlook.com')
        user2 = self.plan.create_user('Innocent',
                                      'Leone',
                                      'inno',
                                      '1234',
                                      'leone@outlook.com')
        self.assertEqual([user1, user2], ['Success', 'Fail'])

    def test_login_user_success(self):
        """Method updates the loged_in variable of the Planner class"""
        online_before = len(Planner.loged_in)
        self.plan.login_user('jane', '123')
        online_after = len(Planner.loged_in)
        self.assertEqual(online_after, online_before + 1)

    def test_update_user_success(self):
        """Test a user is successfully updated"""
        self.plan.update_user('jane', 'Jennifer', 'Basemera', '123', 'jane@outlook.com' )
        self.assertEqual([self.plan.users['jane'].firstname, 
                          self.plan.users['jane'].lastname ],
                          ['Jennifer', 'Basemera'])

    def test_update_nonexistant(self):
        """If the user does not exist method returns an error message"""
        update = self.plan.update_user('inno', 'Innocent', 'Asiimwe', '123', 'asiimwe@outlook.com')
        self.assertEqual(update, 'user not found')

if __name__ == '__main__':
    unittest.main()
