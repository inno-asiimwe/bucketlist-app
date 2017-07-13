"""Module for the Bucketlist class """
class BucketList:
    """A class for creating and managing bucketlist objects"""

    bucketlist_id = 0

    def __init__(self, name, description):
        """class constructor"""
        self.bucketlist_id = str(BucketList.bucketlist_id + 1)
        self.name = name
        self.description = description
        self.activities = []

    def add_activity(self, activity):
        """method to add an activity to the bucketlist"""
        self.activities.append(activity)

    def remove_activity(self, activity_name):
        """method to remove an activity of a given name from the bucketlist"""
        activity = self.object_from_name(activity_name)
        if activity in self.activities:
            self.activities.remove(activity)
            return 'Success'
        return 'Activity does not exist'

    def object_from_name(self, name):
        """Returns an activity object"""
        for activity in self.activities:
            if activity.name == name:
                return activity



    