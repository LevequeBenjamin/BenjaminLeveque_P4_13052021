"""Define the tournaments."""


class Tournament:
    """Tournament class."""

    def __init__(self, name, location, dated, time_control, description):
        self.name = name
        self.location = location
        self.dated = dated
        self.number_of_rounds = 4
        self.rounds = []
        self.players = []
        self.time_control = time_control
        self.description = description

    @property
    def __str__(self) -> dict:
        return {"name": self.name, "location": self.location,
                "dated": self.dated, "rounds": self.rounds,
                "players": self.players, "time_control": self.time_control,
                "description": self.description}
    
    @property  
    def get_name(self):
        return self.name

    @property
    def get_list_players(self):
        return self.players
  
    def append_list_players(self, players):
        self.players.append(players)

    def append_list_rounds(self, rounds):
        self.rounds.append(rounds)