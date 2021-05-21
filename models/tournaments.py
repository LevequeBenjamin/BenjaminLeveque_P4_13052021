"""Define the tournaments."""


class Tournament:
    """Tournament class."""

    def __init__(self, name, location, dated, time_control, description):
        self.id = None
        self.name = name
        self.location = location
        self.dated = dated
        self.current_round = 1
        self.rounds = []
        self.players = []
        self.time_control = time_control
        self.description = description

    @property
    def serialize(self):
        """Serielize Round

        Returns:
            dict: a dictionary of Round
        """
        return {
            "name": self.name,
            "location": self.location,
            "dated": self.dated,
            "rounds": self.rounds,
            "players": self.players,
            "time_control": self.time_control,
            "description": self.description,
        }

    @property
    def get_name(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.name

    @property
    def get_list_players(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.players

    @property
    def get_rounds(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.rounds

    def append_list_players(self, players):
        """[summary]

        Args:
            players ([type]): [description]
        """
        self.players.append(players)

    def append_list_rounds(self, rounds):
        """[summary]

        Args:
            rounds ([type]): [description]
        """
        self.rounds.append(rounds)
     
    @property
    def get_current_round(self):
        return self.current_round
    
    @property
    def counter_round(self):
        self.current_round += 1
