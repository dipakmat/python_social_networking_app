from graph import Graph


class ISocialNetwork:
    """
    Interface for a social network.

    Defines methods that a social network should implement.
    """

    def add_user(self, username, name):
        """
        Adds a user to the social network.

        Args:
            username (str): The username of the user.
            name (str): The name of the user.
        """
        pass

    def add_connection(self, user1, user2):
        """
        Adds a connection between two users in the social network.

        Args:
            user1 (str): The username of the first user.
            user2 (str): The username of the second user.
        """
        pass

    def display_users(self):
        """Displays the users in the social network."""
        pass

    def display_connections(self):
        """Displays the connections in the social network."""
        pass
