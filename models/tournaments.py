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
        """Serielize Tournament

        Returns:
            dict: a dictionary of Tournament
        """
        return {
            "current_round": self.current_round,
            "name": self.name,
            "location": self.location,
            "dated": self.dated,
            "rounds": self.serialize_rounds,
            "players": self.serialize_players,
            "time_control": self.time_control,
            "description": self.description,
        }
     
    @property
    def serialize_players(self):
        player_serialized = []
        for player in self.players:
            player_serialized.append(player.serialize)
        return player_serialized
    
    @property
    def serialize_rounds(self):
        round_serialized = []
        for round in self.rounds:
            round_serialized.append(round.serialize)
        return round_serialized
       
    def add_id(self, id):
        self.id = id 

    @property
    def get_id(self):
        return self.id

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

    def append_list_players(self, player):
        """[summary]

        Args:
            players ([type]): [description]
        """
        self.players.append(player)

    def append_list_rounds(self, round):
        """[summary]

        Args:
            rounds ([type]): [description]
        """
        self.rounds.append(round)
     
    @property
    def get_current_round(self):
        return self.current_round
    
    @property
    def counter_round(self):
        self.current_round += 1
