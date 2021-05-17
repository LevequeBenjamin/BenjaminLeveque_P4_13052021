"""Define the rounds."""

from operator import itemgetter, attrgetter


class Round:
    """Round class."""

    def __init__(self, players):
        self.list_matches = []
        self.players = players

    def get_elo(self, players):
        return players.get("elo")

    @property 
    def sort_elo_players(self):
        """Docstrings."""
        self.players.sort(key=self.get_elo, reverse=True)
        return self.players

    def get_ladder(self, players):
        return players.get("ladder")

    @property
    def sort_ladder_players(self):
        """Docstrings."""
        self.players.sort(key=self.get_ladder)
        return self.players

    def get_score(self, players):
        return players.get("score")
    
    @property
    def sort_score_players(self):
        """Docstrings."""
        self.players.sort(key=self.get_score, reverse=True)
        return self.players

    @property
    def sort_rank_players(self):
        """Docstrings."""
        pass      

    @property
    def generate_pair(self):
        """Docstrings."""
        players_part_one = self.players[0:4]
        players_part_two = self.players[4:]
        players_pair = []
        j = 0
        while j in range(4):
            player_pair = [players_part_one[j], players_part_two[j]]    
            j += 1
            players_pair.append(player_pair)
        return players_pair
    
    def append_list_matches(self, match):
        self.players.append(match)
