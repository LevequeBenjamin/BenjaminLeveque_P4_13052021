"""Define the rounds."""


class Round:
    """It is a class allowing to create a Round."""

    # - - - - - - - - - - - #
    # special methods       #
    # - - - - - - - - - - - #

    def __init__(self, players: list, name: str, created_at: str) -> None:
        """Inits Round.

        Args:
            players (Participant): contains a list of Participant intance,
            name (string): contains the name of the round,
            created_at (string): time retrieved from lib time,
        """
        self.list_matches = []
        self.players = players
        self.name = name
        self.created_at = created_at
        self.finished_at = None
        self.start = True

    # - - - - - - - - - - - #
    # properties            #
    # - - - - - - - - - - - #

    @property
    def sort_elo_players(self) -> list:
        """Sort the list from high elo to low

        Returns:
            Round.players [list]: a sorted list
        """
        self.players.sort(key=self.get_elo, reverse=True)
        return self.players

    @property
    def sort_score_players(self) -> list:
        """Sort the list from high score to low and high elo to low

        Returns:
            Round.players [list]: a sorted list
        """
        sorted(
            self.players,
            key=lambda i: (self.get_score(i), self.get_elo(i)),
            reverse=True,
        )
        return self.players

    @property
    def get_list_matches(self) -> list:
        """Return the matches list

        Returns:
            Round.matches [list]: contains the list of all matches.
        """
        return self.list_matches

    # - - - - - - - - - - - #
    # methods               #
    # - - - - - - - - - - - #

    def serialize(self) -> dict:
        """Method used to serialize a round before saving
        it in the table TOURNAMENTS.

        Returns:
            a dictionary of Round:
                "round": self.name,
                "created_at": self.created_at,
                "finished_at": self.finished_at,
                "round_in_progress": self.start,
                "list_matches": self.serialize_match(),
        """
        return {
            "round": self.name,
            "created_at": self.created_at,
            "finished_at": self.finished_at,
            "round_in_progress": self.start,
            "list_matches": self.serialize_match(),
        }

    def serialize_match(self) -> list:
        """Method used to serialize a list of Match instance before saving
        it in the table TOURNAMENTS.

        Returns:
            matches_serialized (list): contains a list of Match instances serialized
        """
        matches_serialized = []
        for match in self.list_matches:
            matches_serialized.append(match.serialize())
        return matches_serialized

    @staticmethod
    def get_elo(player: object) -> int:
        """Return the player elo

        Args:
            player (Player): a Participant instance

        Returns:
            Participant.elo (float): contains the elo classement entered by the user.
        """
        return player.get_elo

    @staticmethod
    def get_score(player: object) -> float:
        """Return the player score

        Args:
            player (Player): a Participant instance

        Returns:
            Participant.score (float): contains the elo classement entered by the user.
        """
        return player.get_score

    @staticmethod
    def generate_pair_first_round(players: list) -> list:
        """Method allows to generate pairs of players according
        to the Swiss tournament system.

        Args:
            players [list]: a list of Participant instance.
            Tournament.current_round (int): contains the current round.

        Returns:
            players_pair (list): return a list of Participant instance pairs
        """
        players_part_one = players[0:4]
        players_part_two = players[4:]
        players_pair = []
        j = 0
        for j in range(4):
            player_pair = [players_part_one[j], players_part_two[j]]
            players_pair.append(player_pair)
            players_part_one[j].append_list_opponents(players_part_two[j].get_id)
            players_part_two[j].append_list_opponents(players_part_one[j].get_id)
            j += 1
        return players_pair

    @staticmethod
    def generate_pair(players: list) -> list:
        """Method allows to generate pairs of players according
        to the Swiss tournament system.

        Args:
            players [list]: a list of Participant instance.
            Tournament.current_round (int): contains the current round.

        Returns:
            players_pair (list): return a list of Participant instance pairs
        """
        players_pair = []
        j = 0
        for j in range(4):
            x = 1
            if players[x].get_id not in players[0].get_opponents:
                player_pair = [players[0], players[x]]
                players[0].append_list_opponents(players[x].get_id)
                players[x].append_list_opponents(players[0].get_id)
                del players[x]
                del players[0]
                x += 1
            elif len(players) == 2:
                player_pair = [players[0], players[1]]
                players[0].append_list_opponents(players[1].get_id)
                players[1].append_list_opponents(players[0].get_id)
                del players[1]
                del players[0]
                x += 1
            else:
                player_pair = [players[0], players[x]]
                players[0].append_list_opponents(players[x].get_id)
                players[x].append_list_opponents(players[0].get_id)
                del players[x]
                del players[0]
                x += 1
            j += 1
            players_pair.append(player_pair)
        return players_pair

    def append_list_matches(self, match: object) -> None:
        """Method used to add a Match instance in the matches list.

        Args:
            match (Match): a Match instance
        """
        self.list_matches.append(match)

    def add_finished(self, finished_at: str) -> None:
        """Method used to define the end of the round.

        Args:
            finished_at (string): time retrieved from lib time,
        """
        self.finished_at = finished_at

    def add_start(self) -> None:
        """Method used to define the round is not started."""
        self.start = False
