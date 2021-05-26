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

    # - - - - - - - - - - - #
    # properties            #
    # - - - - - - - - - - - #

    @property
    def get_id(self) -> int:
        """Return a tournament id.

        Returns:
            Tournament.tournament_id (int): contains the id of the tournament taken from the database.
        """
        return self.tournament_id

    @property
    def get_name(self) -> str:
        """Return the tournament name.

        Returns:
            Tournament.name (string): contains the name entered by the user.
        """
        return self.name

    @property
    def get_location(self) -> str:
        """Return the tournament location.

        Returns:
            Tournament.location (string): contains the location entered by the user.
        """
        return self.location

    @property
    def get_dated(self) -> str:
        """Return the tournament dated.

        Returns:
            Tournament.dated (string): contains the dated entered by the user.
        """
        return self.dated

    @property
    def get_time_control(self) -> str:
        """Return the tournament time control.

        Returns:
            Tournament.time_control (string): contains the time control entered by the user.
        """
        return self.time_control

    @property
    def get_list_players(self) -> list:
        """Return the tournament name.

        Returns:
            Tournament.players (Participant): contains a list of Participant intance,
        """
        return self.players

    @property
    def get_rounds(self) -> list:
        """Return the list of Round instance in this tournament.

        Returns:
            Tournament.rounds (list): contains a list of Round instances
        """
        return self.rounds

    @property
    def get_current_round(self) -> int:
        """Return the tournament current round.

        Returns:
            Tournament.current_round (string): contains the current
            round of tournament.
        """
        return self.current_round

    @property
    def sort_score_players(self) -> list:
        """Sort the list from high score to low and high elo to low

        Returns:
            Tournament.players [list]: a sorted list
        """
        sorted(
            self.players,
            key=lambda i: (self.get_score(i), self.get_elo(i)),
            reverse=True,
        )
        return self.players

    @property
    def get_current_tournament(self) -> str:
        """Returns Finished status if the tournament is over.

        Returns:
            Tournament.current_tournament (string): contains the
            status Finished if the tournament is over.
        """
        return self.current_tournament

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
        for round in self.rounds:
            rounds_serialized.append(round.serialize())
        return rounds_serialized

    def add_id(self, tournament_id: int) -> None:
        """Method used to add the tournament id.

        Args:
            tournament_id (int): contains the id of the tournament taken from the database.
        """
        self.tournament_id = tournament_id

    def append_list_players(self, player: object) -> None:
        """Method used to add a Participant instance in the players list.

        Args:
            player (Participant): a Participant instance.
        """
        self.players.append(player)

    def append_list_rounds(self, round: object) -> None:
        """Method used to add a Round instance in the rounds list.

        Args:
            round (Round): a Round instance.
        """
        self.rounds.append(round)

    def counter_round(self) -> None:
        """Allows you to add +1 to each new round"""
        self.current_round += 1

    def finished_tournament(self):
        """Allows you to define that the tournament is over"""
        self.current_tournament = "Tournoi terminé"

    @staticmethod
    def get_elo(player: object) -> int:
        """Return the player elo

        Args:
            player (Player): a Participant instance

        Returns:
            Participant.elo (int): contains the elo classement entered by the user.
        """
        return player.get_elo

    @staticmethod
    def get_score(player: object) -> float:
        """Return the player score

        Args:
            player (Player): a Participant instance

        Returns:
            Participant.score (float): contains the score entered by the user.
        """
        return player.get_score
