import unittest
from app.classes.user import User

class TestUser(unittest.TestCase):
    """Tests for methods in the user"""

    def SetUp(self):
        self.myuser = User('Innocent', 'Asiimwe', 'inno', '123', 'asiimwe@outlook.com' )

    def test_create_bucketlist_success(self):
        """Testing whether a bucketlist was successfully created, it should increase the length of self.bucketlists"""
        count_before = len(myuser.bucketlists)
        self.myuser.create_bucketlist('Before 50', 'My goals to be attained before am 50 years old')
        count_after = len(self.myuser.bucketlists)
        self.assertEqual(count_after, count_before + 1, msg='count_after should equal count_before + 1')

    def test_create_bucketlist_name_exists(self):
        """Testing create_bucketlist with a name that already exists"""
        self.myuser.create_bucketlist('Before 50', 'Things I have to purchase before I am 50')
        self.assertEqual(self.myuser.create_bucketlist('Before 50', 'description'),"Name already exists", msg="Duplicate names are not allowed")

    def test_create_bucketlist_non_string_input(self):
        """Method should raise a type error for non string inputs"""
        self.assertRaises(TypeError,self.myuser.create_bucketlist, 'Before 50', 50, msg="Method only accept string inputs")

    def test_view_bucketlists_success(self):
        """"""
        bucketslists = self.myuser.view_bucketlists()
        self.assertIsInstance(bucketslists, list)

  


