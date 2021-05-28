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
        self.matches = []
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
        players_sorted = sorted(
            self.players, key=lambda player: player.elo, reverse=True
        )
        return players_sorted

    @property
    def sort_score_players(self) -> list:
        """Sort the list from high score to low and high elo to low

        Returns:
            Round.players [list]: a sorted list
        """
        players_sorted = sorted(
            self.players,
            key=lambda player: (player.score, player.elo),
            reverse=True,
        )
        return players_sorted

    @property
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
            "list_matches": self.serialize_match,
        }

    @property
    def serialize_match(self) -> list:
        """Method used to serialize a list of Match instance before saving
        it in the table TOURNAMENTS.

        Returns:
            matches_serialized (list): contains a list of Match instances serialized
        """
        matches_serialized = []
        for match in self.matches:
            matches_serialized.append(match.serialize)
        return matches_serialized

    # - - - - - - - - - - - #
    # methods               #
    # - - - - - - - - - - - #

    @staticmethod
    def generate_pair_first_round(tournament: object, players: list) -> list:
        """Method allows to generate pairs of players according
        to the Swiss tournament system.

        Args:
            players [list]: a list of Participant instance.
            Tournament.current_round (int): contains the current round.

        Returns:
            players_pair (list): return a list of Participant instance pairs
        """
        players_part_one = players[0 : tournament.number_rounds]
        players_part_two = players[tournament.number_rounds :]
        players_pair = []
        j = 0
        for j in range(tournament.number_rounds):
            player_pair = [players_part_one[j], players_part_two[j]]
            players_pair.append(player_pair)
            players_part_one[j].opponents.append(players_part_two[j].player_id)
            players_part_two[j].opponents.append(players_part_one[j].player_id)
            j += 1
        return players_pair

    @staticmethod
    def generate_pair(tournament: object, players: list) -> list:
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
        for j in range(tournament.number_rounds):
            i = 1
            if players[i].player_id not in players[0].opponents:
                player_pair = [players[0], players[i]]
                players[0].opponents.append(players[i].player_id)
                players[i].opponents.append(players[0].player_id)
                del players[i]
                del players[0]
                i += 1
            elif len(players) == 2:
                player_pair = [players[0], players[1]]
                players[0].opponents.append(players[1].player_id)
                players[1].opponents.append(players[0].player_id)
                del players[1]
                del players[0]
                i += 1
            else:
                player_pair = [players[0], players[i]]
                players[0].opponents.append(players[i].player_id)
                players[i].opponents.append(players[0].player_id)
                del players[i]
                del players[0]
                i += 1
            j += 1
            players_pair.append(player_pair)
        return players_pair
