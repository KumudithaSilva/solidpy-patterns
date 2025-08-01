class Player:
    def __init__(self, name, position, number):
        # Initialize the name, position, and number properties
        self.name = name
        self.position = position
        self.number = number


class Team:
    def __init__(self, name):
        # Initialize the name property and an empty players list
        self.name = name
        self.players = []

    def add_player(self, player):
        # Add a Player instance to the team's players list
        self.players.append(player)

    def get_player_info(self, number):
        # Return the player's name, position, and jersey number as a formatted string
        # or "Player not found." if no player with the given jersey number is found.
        for player in self.players:
            if player.number == number:
                return f"{player.name} ({player.position}) - {player.number}"
        return "Player not found."


player1 = Player("Rock", "James", "AU_1212")
player2 = Player("Niko", "Anderson", "AU_1717")
player3 = Player("Philip", "Madison", "AU_1515")

team1 = Team("Team AU")
team1.add_player(player1)
team1.add_player(player2)

print(team1.get_player_info("AU_1717"))
print(team1.get_player_info("AU_1212"))
print(team1.get_player_info("AU_9275"))
