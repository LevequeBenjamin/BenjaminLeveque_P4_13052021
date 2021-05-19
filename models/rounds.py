"""Define the rounds."""


class Round:
    """Round class."""

    def __init__(self, players, name, created_at):
        self.list_matches = []
        self.players = players
        self.name = name
        self.created_at = created_at

    @property
    def serialize(self):
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

    def check_already_played(self, players_pair, lastname_player_one, lastname_player_two):
        for match_one, match_two in players_pair:
            if lastname_player_one in [match_one["last_name"], match_two["last_name"]] and lastname_player_two in [match_one["last_name"], match_two["last_name"]]:
                return True
        return False

    def check_already_in_list(self, current_players, lastname):
        for player_one, player_two in current_players:
            if lastname in [player_one["last_name"], player_two['last_name']]:
                return True
        return False

    def check_already_played_two(self, lastname_player_one, lastname_player_two):
        for match_one, match_two in self.list_matches:
            if lastname_player_one in [match_one["last_name"], match_two["last_name"]] and lastname_player_two in [match_one["last_name"], match_two["last_name"]]:
                return True
        return False

    def generate_pair(self, players, i):
        """[summary]

        Args:
            players ([type]): [description]

        Returns:
            [type]: [description]
        """
        players_part_one = players[0:4]
        players_part_two = players[4:]
        players_pair = []
        current_players = []
        print(players_part_one)
        print(players_part_one)
        j = 0
        if i == 1:
            while j in range(4):
                if not self.check_already_played(players_pair, players_part_one[j]["last_name"],
                                                 players_part_two[0]["last_name"]) and not self.check_already_in_list(current_players, players_part_two[0]["last_name"]):
                    player_pair = [players_part_one[j], players_part_two[0]]
                elif not self.check_already_played(players_pair, players_part_one[j]["last_name"],
                                                   players_part_two[1]["last_name"]) and not self.check_already_in_list(current_players, players_part_two[1]["last_name"]):
                    player_pair = [players_part_one[j], players_part_two[1]]
                elif not self.check_already_played(players_pair, players_part_one[j]["last_name"],
                                                   players_part_two[2]["last_name"]) and not self.check_already_in_list(current_players, players_part_two[2]["last_name"]):
                    player_pair = [players_part_one[j], players_part_two[2]]
                else:
                    player_pair = [players_part_one[j], players_part_two[3]]

                j += 1
                current_players.append(player_pair)
                players_pair.append(player_pair)
        else:
            while j in range(4):
                if not self.check_already_played_two(players_part_one[j]["last_name"],
                                                     players_part_two[0]["last_name"]) and not self.check_already_in_list(current_players, players_part_two[0]["last_name"]):
                    player_pair = [players_part_one[j], players_part_two[0]]
                elif not self.check_already_played_two(players_part_one[j]["last_name"],
                                                       players_part_two[1]["last_name"]) and not self.check_already_in_list(current_players, players_part_two[1]["last_name"]):
                    player_pair = [players_part_one[j], players_part_two[1]]
                elif not self.check_already_played_two(players_part_one[j]["last_name"],
                                                       players_part_two[2]["last_name"]) and not self.check_already_in_list(current_players, players_part_two[2]["last_name"]):
                    player_pair = [players_part_one[j], players_part_two[2]]
                else:
                    player_pair = [players_part_one[j], players_part_two[3]]
                current_players.append(player_pair)
                j += 1
                players_pair.append(player_pair)
        del current_players[:]
        return players_pair

    def append_list_matches(self, match):
        """[summary]

        Args:
            match ([type]): [description]
        """
        self.list_matches.append(match)

    @property
    def get_list_matches(self):
        return self.list_matches
