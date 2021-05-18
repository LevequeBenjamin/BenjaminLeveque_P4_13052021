"""Define the rounds."""


class Round:
    """Round class."""

    def __init__(self, players, name, created_at):
        self.list_matches = []
        self.players = players
        self.name = name
        self.created_at = created_at

    def __str__(self):
        """Serialize Round

        Returns:
            dict: a dictionary of Round
        """
        return {"round": self.name, "début tour": self.created_at, "liste match": self.list_matches}

    def get_elo(self, players):
        """[summary]

        Args:
            players ([type]): [description]

        Returns:
            [type]: [description]
        """
        return players.get("elo")

    @property
    def sort_elo_players(self):
        """Sort the list from high elo to low

        Returns:
            Round.players [list]: a sorted list
        """
        self.players.sort(key=self.get_elo, reverse=True)
        return self.players

    def get_ladder(self, players):
        """[summary]

        Args:
            players ([type]): [description]

        Returns:
            [type]: [description]
        """
        return players.get("ladder")

    @property
    def sort_ladder_players(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        self.players.sort(key=self.get_ladder)
        return self.players

    def get_score(self, players):
        """[summary]

        Args:
            players ([type]): [description]

        Returns:
            [type]: [description]
        """
        return players.get("score")

    @property
    def sort_score_players(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        self.players.sort(key=self.get_score, reverse=True)
        return self.players

    @property
    def sort_rank_players(self):
        """Docstrings."""
        pass

    def generate_pair(self, players):
        """[summary]

        Args:
            players ([type]): [description]

        Returns:
            [type]: [description]
        """
        players_part_one = players[0:4]
        players_part_two = players[4:]
        players_pair = []
        j = 0
        while j in range(4):
            player_pair = [players_part_one[j], players_part_two[j]]
            j += 1
            players_pair.append(player_pair)
        return players_pair

    def append_list_matches(self, match):
        """[summary]

        Args:
            match ([type]): [description]
        """
        self.list_matches.append(match)
