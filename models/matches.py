"""Define the matches."""


class Match:
    """Match class."""

    def __init__(self, player_one, player_two, score_player_one, score_player_two):
        self.player_one = player_one
        self.player_two = player_two
        self.score_player_one = score_player_one
        self.score_player_two = score_player_two
        self.matches = (
            [player_one, score_player_one],
            [player_two, score_player_two],
        )

    def __str__(self):
        pass

    @property
    def serialize(self):
        """Serialize matches

        Returns:
            dict: a dictionary of matches
        """
        return {"match": self.matches}
