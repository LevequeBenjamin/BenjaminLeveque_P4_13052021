# pylint: disable=too-many-arguments
# pylint: disable=too-many-instance-attributes
"""Define the tournaments."""


class Tournament:
    """Tournament class."""

    # - - - - - - - - - - - #
    # special methods       #
    # - - - - - - - - - - - #

    def __init__(
        self, name: str, location: str, dated: str, time_control: str, description: str
    ):
        """Inits Tournament

        Args:
            name (string): contains the name entered by the user,
            location (string): contains the location entered by the user,
            dated (string): contains the dated entered by the user,
            time_control (string): contains the time control entered by the user,
            description (string): contains the description entered by the user,
        """
        self.tournament_id = 0
        self.name = name
        self.location = location
        self.dated = dated
        self.current_round = 1
        self.rounds = []
        self.players = []
        self.time_control = time_control
        self.description = description
        self.current_tournament = ""
        self.current_players = []

    # - - - - - - - - - - - #
    # properties            #
    # - - - - - - - - - - - #

    @property
    def sort_score_players(self) -> list:
        """Sort the list from high score to low and high elo to low

        Returns:
            Tournament.players [list]: a sorted list
        """
        self.players.sort(
            key=lambda player: (player.score, player.elo),
            reverse=True,
        )
        return self.players

    # - - - - - - - - - - - #
    # methods               #
    # - - - - - - - - - - - #

    def serialize(self) -> dict:
        """Method used to serialize a tournament before saving
        it in the table TOURNAMENTS.

        Returns:
            a dictionary of Tournament:
                "current_round": self.current_round,
                "name": self.name,
                "location": self.location,
                "dated": self.dated,
                "rounds": self.serialize_rounds(),
                "players": self.serialize_players(),
                "time_control": self.time_control,
                "description": self.description,
                "current_tournament": self.current_tournament,
                "current_players": self.current_players,
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
            "current_tournament": self.current_tournament,
            "current_players": self.current_players,
        }

    def serialize_players(self) -> list:
        """Method used to serialize a list of Participant instance before saving
        it in the table TOURNAMENTS.

        Returns:
            players_serialized (list): contains a list of Particpant instances serialized
        """
        players_serialized = []
        for player in self.players:
            players_serialized.append(player.serialize())
        return players_serialized

    def serialize_rounds(self) -> list:
        """Method used to serialize a list of Round instance before saving
        it in the table TOURNAMENTS.

        Returns:
            rounds_serialized (list): contains a list of Round instances serialized
        """
        rounds_serialized = []
        for round_game in self.rounds:
            rounds_serialized.append(round_game.serialize())
        return rounds_serialized
