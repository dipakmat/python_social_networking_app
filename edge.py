# edge.py
class Edge:
    """
    Represents a connection between two users in the social network.

    Attributes:
        user1 (User): The first user in the connection.
        user2 (User): The second user in the connection.
    """

    def __init__(self, user1, user2):
        """
        Initializes a new Edge.

        Args:
            user1 (User): The first user in the connection.
            user2 (User): The second user in the connection.
        """
        self.user1 = user1
        self.user2 = user2
