"""Define the rounds."""

from operator import itemgetter, attrgetter


class Round:
    """Round class."""

    def __init__(self, players):
        self.list_matches = []
        self.players = players

    def sort_elo_players(self):
        """Docstrings."""
        elo = self.players.get("elo")
        players = self.players.sort(key=elo, reverse=True)
        return players

    def sort_ladder_players(self):
        """Docstrings."""
        ladder = self.players.get("ladder")
        players = self.players.sort(key=ladder)
        return players

    def sort_score_players(self):
        """Docstrings."""
        score = self.players.get("score")
        players = list.sort(key=score, reverse=True)
        return players

    def sort_rank_players(self):
        """Docstrings."""
        pass

    def generate_pair(self, list):
        """Docstrings."""
        pass

