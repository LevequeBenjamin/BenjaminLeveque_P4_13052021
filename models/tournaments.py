"""Define the tournaments."""


class Tournament:
    """Tournament class."""

    def __init__(self, name, location, dated):
        self.name = name
        self.location = location
        self.dated = dated
        self.number_of_rounds = 4
        self.list_rounds = []
        self.list_players = []
        self.time_control = None
        self.description = None
