class BucketList:
    """A class for creating and managing bucketlist objects"""

    bucketlist_id = 0

    def __init__(self,name, description):
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
        pass

        

    