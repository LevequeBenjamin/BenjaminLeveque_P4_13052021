"""Define the tournaments."""


class Tournament:
    """Tournament class."""

    def __init__(self, name, location, dated, time_control, description):
        """[summary]

        Args:
            name ([type]): [description]
            location ([type]): [description]
            dated ([type]): [description]
            time_control ([type]): [description]
            description ([type]): [description]
        """
        self.id = 0
        self.name = name
        self.location = location
        self.dated = dated
        self.current_round = 1
        self.rounds = []
        self.players = []
        self.time_control = time_control
        self.description = description

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
            "rounds": self.serialize_rounds(),
            "players": self.serialize_players(),
            "time_control": self.time_control,
            "description": self.description,
        }

    def serialize_players(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        player_serialized = []
        for player in self.players:
            player_serialized.append(player.serialize())
        return player_serialized

    def serialize_rounds(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        round_serialized = []
        for round in self.rounds:
            round_serialized.append(round.serialize())
        return round_serialized

    def add_id(self, id):
        """[summary]

        Args:
            id ([type]): [description]
        """
        self.id = id

    def get_id(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.id

    def get_name(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.name
    
    def get_location(self):
        return self.location
    
    def get_dated(self):
        return self.dated

    def get_time_control(self):
        return self.time_control

    def get_list_players(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.players

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

    def get_current_round(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.current_round

    def counter_round(self):
        """[summary]
        """
        self.current_round += 1
