"""Define the rounds."""

import operator
import time


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
        self.finished_at = None
        self.start = True

    def serialize(self):
        """Serialize Round

        Returns:
            dict: a dictionary of Round
        """
        return {
            "round": self.name,
            "created_at": self.created_at,
            "finished_at": self.finished_at,
            "round_in_progress": self.start,
            "list_matches": self.serialize_match(),
        }

    def serialize_match(self):
        matches_serialized = []
        for match in self.list_matches:
            matches_serialized.append(match.serialize())
        return matches_serialized

    def get_elo(self, player):
        """[summary]

        Args:
            players ([type]): [description]

        Returns:
            [type]: [description]
        """
        return player.get_elo()

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
        return player.get_ladder()

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
        return player.get_score()

    def sort_score_players(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        players = sorted(self.players, key=lambda i: (self.get_score(i), self.get_elo(i)), reverse=True)
        return players

    def check_already_current_players(self, current_players, id):
        """[summary]

        Args:
            current_players ([type]): [description]
            lastname ([type]): [description]

        Returns:
            [type]: [description]
        """
        for player in current_players:
            if id == player.get_id():
                return True
        return False

    def check_already_played(self, tournament,
                             id_player_one, id_player_two
                             ):
        """[summary]

        Args:
            current_matches ([type]): [description]
            lastname_player_one ([type]): [description]
            lastname_player_two ([type]): [description]

        Returns:
            [type]: [description]
        """
        for round in tournament.serialize_rounds():
            for matches in round['list_matches']:
                if id_player_one in [
                    matches['match'][0][0]['id'],
                    matches['match'][1][0]['id'],
                ] and id_player_two in [
                    matches['match'][0][0]['id'],
                    matches['match'][1][0]['id'],
                ]:
                    return True
        return False
    
    def generate_pair(self, tournament, players, current_round):
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
        j = 0
        if current_round == 1:
            for j in range(4):
                player_pair = [players_part_one[j], players_part_two[j]]
                players_pair.append(player_pair)
                players_part_one[j].append_list_opponents(players_part_two[j].get_id())
                players_part_two[j].append_list_opponents(players_part_one[j].get_id())
                j += 1
        else:
            for j in range(4):
                x = 1
                if players[x].get_id() not in players[0].get_opponents():
                    player_pair = [players[0], players[x]]
                    players[0].append_list_opponents(players[x].get_id())
                    players[x].append_list_opponents(players[0].get_id())
                    del players[x]
                    del players[0]
                    x += 1
                elif len(players) == 2:
                    player_pair = [players[0], players[1]]
                    players[0].append_list_opponents(players[1].get_id())
                    players[1].append_list_opponents(players[0].get_id())
                    del players[1]
                    del players[0]
                    x += 1
                else:
                    player_pair = [players[0], players[x]]
                    players[0].append_list_opponents(players[x].get_id())
                    players[x].append_list_opponents(players[0].get_id())
                    del players[x]
                    del players[0]
                    x += 1
                j += 1
                players_pair.append(player_pair)
        return players_pair

    def append_list_matches(self, match):
        """[summary]

        Args:
            match ([type]): [description]
        """
        self.list_matches.append(match)

    def get_list_matches(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.list_matches

    def add_finished(self, finished_at):
        """[summary]

        Args:
            finished_at ([type]): [description]
        """
        self.finished_at = finished_at

    def add_start(self):
        """[summary]
        """
        self.start = False
