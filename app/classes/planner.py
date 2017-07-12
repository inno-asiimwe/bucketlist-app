from .user import User
class Planner:
    """The planner class contains methods to interact with all the other classes"""

    def __init__(self):
        self.users = {}

    def create_user(self, firstname, lastname, username, userpass, email):
        """A method to create a new user"""
        new_user = User(firstname, lastname, username, userpass, email)
        self.users.update({new_user.username:new_user})

    def delete_user(self, username):
        """A method to delete an existing user"""
        pass

    def login_user(self, username, userpass):
        """A method to login a user with username and password"""
        if username in self.users and self.users[username].password == userpass:
            return True
        else:
            return False

    def logout_user(self, username):
        """A method to logout a user with given username"""
        pass
    
