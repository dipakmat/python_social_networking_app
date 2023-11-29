class User:
    """
    Represents a user in the social network.

    Attributes:
        username (str): The username of the user.
        name (str): The name of the user.
        friends (list): A list of User objects representing friends.
    """

    def __init__(self, username, name):
        """
        Initializes a new User.

        Args:
            username (str): The username of the user.
            name (str): The name of the user.
        """
        self.username = username
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        """
        Adds a friend to the user's friend list.

        Args:
            friend (User): The User object to be added as a friend.
        """
        self.friends.append(friend)

