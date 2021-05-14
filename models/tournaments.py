"""Define the tournaments."""


class Tournament:
    """Tournament class."""

    def __init__(self, name, location, dated, number_of_players, description):
        self.name = name
        self.location = location
        self.dated = dated
        self.number_of_rounds = 4
        self.number_of_players = number_of_players
        self.list_rounds = []
        self.list_players = []
        self.time_control = None
        self.description = description

    def __str__(self) -> dict:
        return {"name": self.name, "location": self.location,
                "dated": self.dated, "number_of_players": self.number_of_players,
                "description": self.description}
