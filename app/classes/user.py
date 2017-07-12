from .bucketlist import BucketList
class User:
    """Creates the user object and has methods for creating and viewing bucketlists and activities"""

    def __init__(self, firstname, lastname, username,password, email):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password
        self.bucketlists = []

    def create_bucketlist(self, name, description):
        """method creates a new bucketlist for current user with the given name and description"""
        self.bucketlists.append(BucketList(name,description))
        

    def create_activity(self, bucketlist_name, activity_name, activity_status):
        """method creates a new activity with activity_name and activity_status in bucketlist of provided name"""
        pass 

    def view_bucketlists(self):
        """method returns all the bucketlists for the current user"""
        return self.bucketlists 

    def view_bucketlist_activities(self, bucketlist_name):
        """method returns a list of activities in a given bucket_list for the current user"""
        pass

    