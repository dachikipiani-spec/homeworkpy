class FootballTeam:
    def __init__(self, team_name, coach):
        self.team_name = team_name
        self.coach = coach
        self.players = []

    def add_player(self, name, position, number, age, nationality):
        player = {
            "name": name,
            "position": position,
            "number": number,
            "age": age,
            "nationality": nationality
        }
        self.players.append(player)

    def remove_player(self, number):
        for player in self.players:
            if player["number"] == number:
                self.players.remove(player)
                return
        print(f"Player with number {number} not found")

    def update_player(self, number, **kwargs):
        for player in self.players:
            if player["number"] == number:
                player.update(kwargs)
                return
        print(f"Player with number {number} not found")

    def show_team_info(self):
        print(f"Team: {self.team_name}")
        print(f"Coach: {self.coach}")
        print("Players:")
        for player in self.players:
            print(player)

    def show_player_info(self, number):
        for player in self.players:
            if player["number"] == number:
                print(player)
                return
        print(f"Player with number {number} not found")