"""Module contains unittests for the BucketList class"""
import unittest
from app.classes.bucketlist import BucketList
from app.classes.activity import Activity

class TestBucketList(unittest.TestCase):
    """Class contains tests methods in bucketlist class"""
    def setUp(self):
        self.mybucketlist = BucketList('Before 50',
                                       'Activities to accomplish before 50')
        self.myactivity = Activity("buy house", "I should buy a mansion")

    def test_add_activity_success(self):
        """Tests whether an activity was added to a bucketlist """
        self.mybucketlist.add_activity(self.myactivity)
        self.assertIn(self.myactivity, self.mybucketlist.activities,
                      msg="activity should be in list activities of the bucketlist object")

    def test_add_activity_string_input(self):
        """add_activity should raise type error with non activity objects"""
        self.assertRaises(TypeError, self.mybucketlist.add_activity,
                          'activity name',
                          msg="Input should activity object")

    def test_add_activity_integer_input(self):
        """add_activity should raise type error with non activity objects"""
        self.assertRaises(TypeError, self.mybucketlist.add_activity,
                          'activity name', msg="Input should activity object")

    def test_remove_activity_success(self):
        """Test whether activity is removed"""
        newactivity = Activity('Purchase car', 'I should buy a car by 20')
        self.mybucketlist.add_activity(newactivity)
        self.mybucketlist.remove_activity('Purchase car')
        self.assertNotIn(newactivity, self.mybucketlist.activities)

    def test_remove_activity_non_existant(self):
        """Test with an activity that does not exist"""
        status = self.mybucketlist.remove_activity('Purchase car')
        self.assertEqual(status, 'Activity does not exist')

    def test_remove_activity_non_string(self):
        """remove_activity should Raise a typeerror if passed a non string"""
        self.assertRaises(TypeError, self.mybucketlist.remove_activity,
                          57, msg="Activity name should be a string")
