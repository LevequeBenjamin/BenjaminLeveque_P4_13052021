"""Define the matches."""


class Match:
    """Match class."""

    def __init__(self, player_one, player_two, score_players_one, score_players_two):
        self.player_one = player_one
        self.player_two = player_two
        self.score_players_one = score_players_one
        self.score_players_two = score_players_two
        self.tuple_match = ([player_one, score_players_one], [
                            player_two, score_players_two])

    @property
    def __str__(self):
        return {"match": self.tuple_match}

    def get_tuple_match(self):
        return self.tuple_match

    def save_game(self):
        """Docstrings."""
        pass

    def update_game(self):
        """Docstrings."""
        pass

    def delete_game(self):
        """Docstrings."""
        pass

    def winner(self):
        """Docstrings."""
        pass

    def loser(self):
        """Docstrings."""
        pass

    def draw(self):
        """Docstrings."""
        pass
