"""The Planner class handles all methods partaining to the user object """
from .user import User
class Planner:
    """The planner class contains methods to interact with all the other classes"""

    loged_in = []

    def __init__(self):
        self.users = {}

    def create_user(self, firstname, lastname, username, userpass, email):
        """A method to create a new user"""
        if self.user_exists(username):
            return 'Fail'
        new_user = User(firstname, lastname, username, userpass, email)
        self.users.update({new_user.username:new_user})
        return 'Success'

    def delete_user(self, username):
        """A method to delete an existing user"""
        if username not in self.users:
            return 'user not found'
        del self.users[username]

    def login_user(self, username, userpass):
        """A method to login a user with username and password"""
        if self.user_exists(username) and self.users[username].password == userpass:
            Planner.loged_in.append(self.users[username].username)
            return True
        return False

    def logout_user(self, username):
        """A method to logout a user with given username"""
        while username in Planner.loged_in:
            Planner.loged_in.remove(username)
    def user_exists(self, username):
        """method checks if the user already exists basing on username"""
        return username in self.users
    def update_user(self, username, new_firstname, new_lastname, new_password, new_email):
        """A method to update the profile of a user, returns update user or 'user not found"""
        if username not in self.users:
            return 'user not found'
        self.users[username].firstname = new_firstname
        self.users[username].lastname = new_lastname
        self.users[username].password = new_password
        self.users[username].email = new_email
        return self.users[username]
    def get_name_from_id(self, bucketlist_id):
        """Methods takes a bucketlist id and returns its name"""
        found = False
        for user in self.users:
            for bucketlist in self.users[user].bucketlists:
                if bucketlist.bucketlist_id == bucketlist_id:
                    found = True
                    return bucketlist.name
                found = False
        if  not found:
            return False
