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

    def check_already_played(self, lastname_player_one, lastname_player_two):
        for match in self.list_matches:
            try:
                if match[0]["last_name"] == lastname_player_one or match[0]["last_name"] == lastname_player_two and match[1]["last_name"] == lastname_player_one or match[1]["last_name"] == lastname_player_two:
                    return True
            except:
                return False

    def check_already_in_list(self, lastname_player_two):
        for match in self.list_matches:
            try:
                if match[0]["last_name"] == lastname_player_two or match[1]["last_name"] == lastname_player_two:
                    return True
            except:
                return False

    # def generate_pair(self, players):
    #     """[summary]

    #     Args:
    #         players ([type]): [description]

    #     Returns:
    #         [type]: [description]
    #     """
    #     players_part_one = players[0:4]
    #     players_part_two = players[4:]
    #     players_pair = []
    #     j = 0
    #     while j in range(4):
    #         player_pair = [players_part_one[j], players_part_two[j]]
    #         j += 1
    #         players_pair.append(player_pair)
    #     return players_pair

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
            if not self.check_already_played(players_part_one[j]["last_name"], players_part_two[0]["last_name"]) and not self.check_already_in_list(players_part_two[0]["last_name"]):
                print(f"{j}")
                print(f"{players_part_one[j]['last_name']}")
                print(f"{players_part_two[0]['last_name']}")
                player_pair = [players_part_one[j], players_part_two[0]]
            elif not self.check_already_played(players_part_one[j]["last_name"], players_part_two[1]["last_name"]) and not self.check_already_in_list(players_part_two[1]["last_name"]):
                print(f"{j}")
                print(f"{players_part_one[j]['last_name']}")
                print(f"{players_part_two[1]['last_name']}")
                player_pair = [players_part_one[j], players_part_two[1]]
            elif not self.check_already_played(players_part_one[j]["last_name"], players_part_two[2]["last_name"]) and not self.check_already_in_list(players_part_two[2]["last_name"]):
                print(f"{j}")
                print(f"{players_part_one[j]['last_name']}")
                print(f"{players_part_two[2]['last_name']}")
                player_pair = [players_part_one[j], players_part_two[2]]
            elif not self.check_already_played(players_part_one[j]["last_name"], players_part_two[3]["last_name"]) and not self.check_already_in_list(players_part_two[3]["last_name"]):
                print(f"{j}")
                print(f"{players_part_one[j]['last_name']}")
                print(f"{players_part_two[3]['last_name']}")
                player_pair = [players_part_one[j], players_part_two[3]]
            j += 1
            players_pair.append(player_pair)
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
