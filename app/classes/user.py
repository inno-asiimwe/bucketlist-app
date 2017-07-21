"""Module for the User Class"""
from .bucketlist import BucketList
from .activity import Activity

class User:
    """Creates the user object and has methods for creating and
        viewingbucketlists and activities"""
    def __init__(self, firstname, lastname, username, password, email):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password
        self.email = email
        self.bucketlists = []

    def create_bucketlist(self, name, description):
        """method creates a new bucketlist for current user with the given name and description"""
        self.bucketlists.append(BucketList(name, description))
    def create_activity(self, bucketlist_name, activity_name, description):
        """method creates a new activity with activity_name and
           description in bucketlist of provided name"""
        new_activity = Activity(activity_name, description)
        for bucketlist in self.bucketlists:
            if bucketlist.name == bucketlist_name:
                found = True
                bucketlist.add_activity(new_activity)
        if not found:
            bucketlist = self.create_bucketlist(bucketlist_name, '')
            bucketlist.add_activity(new_activity)

    def view_bucketlists(self):
        """method returns all the bucketlists for the current user"""
        return self.bucketlists
    def view_bucketlist_activities(self, bucketlist_name):
        """method returns a list of activities in a given bucket_list for the current user"""
        for bucketlist in self.bucketlists:
            if bucketlist.name == bucketlist_name:
                return bucketlist.activities
    def delete_bucketlist(self, bucketlist_name):
        """Method deletes a bucketlist"""
        if isinstance(bucketlist_name, str):
            bucketlist = self.get_object_from_name(bucketlist_name, self.bucketlists)
            self.bucketlists.remove(bucketlist)
        raise TypeError('Given Name not a string')

    def update_bucketlist(self, bucketlist_id, new_name, new_description):
        """Method updates the attributes of the bucketlist"""
        for bucketlist in self.bucketlists:
            if bucketlist.bucketlist_id == bucketlist_id:
                bucketlist.name = new_name
                bucketlist.description = new_description

    def delete_activity(self, bucketlist_id, activity_id):
        """Method deletes activity from bucketlist """
        for bucketlist in self.bucketlists:
            if bucketlist.bucketlist_id == bucketlist_id:
                bucketlist.remove_activity(activity_id)

    def get_object_from_name(self, item_name, container):
        """searches a list of objects by name returns the object if name found """
        for item in container:
            if item.name == item_name:
                return item
