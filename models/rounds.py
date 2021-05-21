"""Define the rounds."""


class Round:
    """Round class."""

    def __init__(self, players, name, created_at):
        """[summary]

        Args:
            players ([type]): [description]
            name ([type]): [description]
            created_at ([type]): [description]
        """
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
        return {
            "round": self.name,
            "début tour": self.created_at,
            "liste match": self.list_matches,
        }

    def get_elo(self, player):
        """[summary]

        Args:
            players ([type]): [description]

        Returns:
            [type]: [description]
        """
        return player.get_elo

    @property
    def sort_elo_players(self):
        """Sort the list from high elo to low

        Returns:
            Round.players [list]: a sorted list
        """
        self.players.sort(key=self.get_elo, reverse=True)
        return self.players

    def get_ladder(self, player):
        """[summary]

        Args:
            players ([type]): [description]

        Returns:
            [type]: [description]
        """
        return player.get_ladder

    @property
    def sort_ladder_players(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        self.players.sort(key=self.get_ladder)
        return self.players

    def get_score(self, player):
        """[summary]

        Args:
            players ([type]): [description]

        Returns:
            [type]: [description]
        """
        return player.get_score

    @property
    def sort_score_players(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        self.players.sort(key=self.get_score, reverse=True)
        return self.players

    def check_already_current_players(self, current_players, lastname):
        """[summary]

        Args:
            current_players ([type]): [description]
            lastname ([type]): [description]

        Returns:
            [type]: [description]
        """
        for player in current_players:
            if lastname == player["last_name"]:
                return True
        return False

    def check_already_played(
        self, current_matches, lastname_player_one, lastname_player_two
    ):
        """[summary]

        Args:
            current_matches ([type]): [description]
            lastname_player_one ([type]): [description]
            lastname_player_two ([type]): [description]

        Returns:
            [type]: [description]
        """
        for matches in current_matches:
            for match_one, match_two in matches:
                if lastname_player_one in [
                    match_one["last_name"],
                    match_two["last_name"],
                ] and lastname_player_two in [
                    match_one["last_name"],
                    match_two["last_name"],
                ]:
                    return True
        return False

    def generate_pair(self, current_matches, players, current_round):
        """[summary]

        Args:
            current_matches ([type]): [description]
            players ([type]): [description]
            i ([type]): [description]

        Returns:
            [type]: [description]
        """
        players_part_one = players[0:4]
        players_part_two = players[4:]
        players_pair = []
        current_players = []
        j = 0
        if current_round == 1:
            while j in range(4):
                player_pair = [players_part_one[j], players_part_two[j]]

                j += 1
                players_pair.append(player_pair)
                current_players.append(player_pair[0])
                current_players.append(player_pair[1])
        else:
            while j in range(4):
                if not self.check_already_played(
                    current_matches,
                    players_part_one[j]["last_name"],
                    players_part_two[0]["last_name"],
                ) and not self.check_already_current_players(
                    current_players, players_part_two[0]["last_name"]
                ):
                    player_pair = [players_part_one[j], players_part_two[0]]
                elif not self.check_already_played(
                    current_matches,
                    players_part_one[j]["last_name"],
                    players_part_two[1]["last_name"],
                ) and not self.check_already_current_players(
                    current_players, players_part_two[1]["last_name"]
                ):
                    player_pair = [players_part_one[j], players_part_two[1]]
                elif not self.check_already_played(
                    current_matches,
                    players_part_one[j]["last_name"],
                    players_part_two[2]["last_name"],
                ) and not self.check_already_current_players(
                    current_players, players_part_two[2]["last_name"]
                ):
                    player_pair = [players_part_one[j], players_part_two[2]]
                else:
                    player_pair = [players_part_one[j], players_part_two[3]]
                j += 1
                players_pair.append(player_pair)
                current_players.append(player_pair[0])
                current_players.append(player_pair[1])
        del current_players[:]
        current_matches.append(players_pair)
        return players_pair

    def append_list_matches(self, match):
        """[summary]

        Args:
            match ([type]): [description]
        """
        self.list_matches.append(match)

    @property
    def get_list_matches(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.list_matches
