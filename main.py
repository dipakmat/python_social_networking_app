from social_network_impl import SocialNetwork


if __name__ == "__main__":
    # Example Usage
    my_network = SocialNetwork()

    my_network.add_user("user1", "Alice")
    my_network.add_user("user2", "Bob")
    my_network.add_user("user3", "Charlie")

    my_network.add_connection("user1", "user2")
    my_network.add_connection("user2", "user3")

    my_network.display_users()
    my_network.display_connections()