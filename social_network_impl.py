from user import User
from edge import Edge
from graph import Graph
from social_network import ISocialNetwork


class SocialNetwork(ISocialNetwork):
    """
    Implementation of a social network.

    Uses the User, Edge, and Graph classes to manage users and connections.
    """

    def __init__(self):
        """Initializes a new social network."""
        self.users = {}
        self.connections = Graph()

    def add_user(self, username, name):
        """
        Adds a user to the social network.

        Args:
            username (str): The username of the user.
            name (str): The name of the user.
        """
        new_user = User(username, name)
        self.users[username] = new_user

    def add_connection(self, user1, user2):
        """
        Adds a connection between two users in the social network.

        Args:
            user1 (str): The username of the first user.
            user2 (str): The username of the second user.
        """
        if user1 not in self.users or user2 not in self.users:
            raise ValueError("User not found in the social network.")

        self.connections.add_edge(user1, user2)
        self.connections.add_edge(user2, user1)
        self.users[user1].add_friend(self.users[user2])
        self.users[user2].add_friend(self.users[user1])

    def display_users(self):
        """Displays the users in the social network."""
        print("Users:")
        for username, user in self.users.items():
            print(f"{username} - {user.name}")

    def display_connections(self):
        """Displays the connections in the social network."""
        print("Connections:")
        self.connections.display_graph()
