"""Module contains unittest for the User class"""
import unittest
from app.classes.user import User

class TestUser(unittest.TestCase):
    """Tests for methods in the user"""

    def setUp(self):
        """Setting up a user to use for each test"""
        self.myuser = User('Innocent',
                           'Asiimwe',
                           'inno',
                           '123',
                           'asiimwe@outlook.com')

    def test_create_bucketlist_success(self):
        """Testing whether a bucketlist was successfully created,
        it should increase the length of self.bucketlists"""
        count_before = len(self.myuser.bucketlists)
        self.myuser.create_bucketlist('Before 50',
                                      'My goals to be attained before am 50 years old')
        count_after = len(self.myuser.bucketlists)
        self.assertEqual(count_after, count_before + 1,
                         msg='count_after should equal count_before + 1')

    def test_create_bucketlist_non_string_input(self):
        """Method should raise a type error for non string inputs"""
        self.assertRaises(TypeError,
                          self.myuser.create_bucketlist,
                          'Before 50', 50,
                          msg="Method only accept string inputs")

    def test_view_bucketlists_success(self):
        """View_bucketlists should return a list"""
        bucketslists = self.myuser.view_bucketlists()
        self.assertIsInstance(bucketslists, list)

    def test_update_bucketlist_success(self):
        """Tests whether the attributes of the bucketlist are updated"""
        self.myuser.create_bucketlist('Before 50', 'Things to do')
        self.myuser.update_bucketlist(self.myuser.bucketlists[0].bucketlist_id,
                                      'Before 50',
                                      'Things to do before 50')
        self.assertEqual(self.myuser.bucketlists[0].description, 'Things to do before 50')

    def test_update_bucketlist_invalid(self):
        """Non existant bucketlist should return 'Invalid' """
        self.myuser.create_bucketlist('Before 50', 'Things to do')
        update = self.myuser.update_bucketlist('2', 'Before 50', 'Things to do before 50')
        self.assertEqual(update, 'invalid')

    def test_update_activity_success(self):
        """Tests whether the attributes of the activity are updates"""
        self.myuser.create_bucketlist('Before 50', 'Things to do')
        self.myuser.create_activity('Before 50', 'Build', 'I should build house')
        self.myuser.update_activity(self.myuser.bucketlists[0].bucketlist_id,
                                    self.myuser.bucketlists[0].activities[0].activity_id,
                                    'Build a house',
                                    'I should build a house')
        self.assertEqual(self.myuser.bucketlists[0].activities[0].name, 'Build a house')

    def test_update_activity_invalid(self):
        """Non existant bucketlist should return 'invalid' """
        self.myuser.create_bucketlist('Before 50', 'Things to do')
        update = self.myuser.update_activity(self.myuser.bucketlists[0].bucketlist_id,
                                            '12',
                                            'Build a house',
                                            'I must build a house')
        self.assertEqual(update, 'invalid')



if __name__ == '__main__':
    unittest.main()
