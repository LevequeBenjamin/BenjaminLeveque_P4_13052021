"""Define the matches."""


class Match:
    """Match class."""

    def __init__(self, player_one, player_two, score_players_one, score_players_two):
        self.player_one = player_one
        self.player_two = player_two
        self.score_players_one = score_players_one
        self.score_players_two = score_players_two
        self.matches = ([player_one, score_players_one], [
                            player_two, score_players_two])

    @property
    def __str__(self):
        """Serialize matches

        Returns:
            dict: a dictionary of matches
        """
        return {"match": self.matches}
