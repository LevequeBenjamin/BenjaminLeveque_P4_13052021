# pylint: disable=too-many-arguments
# pylint: disable=too-many-instance-attributes
"""Define the tournaments."""

# librairies
from typing import List, Dict

# models
from models.players import Participant
from models.rounds import Round


class Tournament:
    """Tournament class.

    Attributs:
        name (string): contains the name entered by the user,
        location (string): contains the location entered by the user,
        dated (string): contains the dated entered by the user,
        time_control (string): contains the time control entered by the user,
        description (string): contains the description entered by the user,
        number_players (int): contains the number of players entered by the user,
        number_rounds (int): contains the number or rounds entred by the user,
        tournament_id (int): contains the id of tournament,
        current_round (int): contains the current round,
        current_tournament (str): define when the tournament it's finished,

    Properties:
        serialize(self) -> Dict:
            Method used to serialize a tournament before saving
            it in the table TOURNAMENTS.
        serialize_players(self) -> List[Dict]:
            Method used to serialize a list of Participant instance before saving
            it in the table TOURNAMENTS.
        serialize_rounds(self) -> List[Dict]:
            Method used to serialize a list of Round instance before saving
            it in the table TOURNAMENTS.

    Methods:
        sort_elo_players(self) -> List[Participant]:
            Sort the list from high elo to low.
        sort_score_players(self) -> List[Participant]:
            Sort the list from high score to low and high elo to low.
        generate_pair_first_round(self) -> List[Participant]:
            Method allows to generate pairs of players according
            to the Swiss tournament system.
        generate_pair(self) -> List[Participant]:
            Method allows to generate pairs of players according
            to the Swiss tournament system.
    """

    # - - - - - - - - - - - #
    # special methods       #
    # - - - - - - - - - - - #

    def __init__(
        self,
        name: str,
        location: str,
        dated: str,
        time_control: str,
        description: str,
        number_players: int,
        number_rounds: int,
        tournament_id: int = 0,
        current_round: int = 1,
        current_tournament: str = None,
    ):
        """Inits Tournament

        Args:
            name (string): contains the name entered by the user,
            location (string): contains the location entered by the user,
            dated (string): contains the dated entered by the user,
            time_control (string): contains the time control entered by the user,
            description (string): contains the description entered by the user,
            number_players (int) : contains the number of players entered by the user.
            number_rounds (int) : contains the number or rounds entred by the user.
        """
        self.tournament_id = tournament_id
        self.name = name
        self.location = location
        self.dated = dated
        self.current_round = current_round
        self.rounds: List[Round] = []
        self.players: List[Participant] = []
        self.time_control = time_control
        self.description = description
        self.current_tournament = current_tournament
        self.current_players: List[Dict] = []
        self.number_players = number_players
        self.number_rounds = number_rounds

    # - - - - - - - - - - - #
    # properties            #
    # - - - - - - - - - - - #

    @property
    def serialize(self) -> Dict:
        """Method used to serialize a tournament before saving
        it in the table TOURNAMENTS.

        Returns:
            a dictionary of Tournament:
                "current_round": self.current_round,
                "name": self.name,
                "location": self.location,
                "dated": self.dated,
                "rounds": self.serialize_rounds(),
                "players": self.serialize_players(),
                "time_control": self.time_control,
                "description": self.description,
                "current_tournament": self.current_tournament,
                "current_players": self.current_players,
        """
        return {
            "current_round": self.current_round,
            "name": self.name,
            "location": self.location,
            "dated": self.dated,
            "rounds": self.serialize_rounds,
            "players": self.serialize_players,
            "time_control": self.time_control,
            "description": self.description,
            "current_tournament": self.current_tournament,
            "current_players": self.current_players,
            "number_players": self.number_players,
            "number_rounds": self.number_rounds,
        }

    @property
    def serialize_players(self) -> List[Dict]:
        """Method used to serialize a list of Participant instance before saving
        it in the table TOURNAMENTS.

        Returns:
            players_serialized (list): contains a list of Particpant instances serialized
        """
        players_serialized = []
        for player in self.players:
            players_serialized.append(player.serialize)
        return players_serialized

    @property
    def serialize_rounds(self) -> List[Dict]:
        """Method used to serialize a list of Round instance before saving
        it in the table TOURNAMENTS.

        Returns:
            rounds_serialized (list): contains a list of Round instances serialized
        """
        rounds_serialized = []
        for round_game in self.rounds:
            rounds_serialized.append(round_game.serialize)
        return rounds_serialized

    # - - - - - - - - - - - #
    # methods               #
    # - - - - - - - - - - - #

    def sort_elo_players(self) -> List[Participant]:
        """Sort the list from high elo to low.

        Returns:
            Round.players [list]: a sorted list
        """
        players_sorted = sorted(
            self.players, key=lambda player: player.elo, reverse=True
        )
        return players_sorted

    def sort_score_players(self) -> List[Participant]:
        """Sort the list from high score to low and high elo to low.

        Returns:
            Round.players [list]: a sorted list
        """
        players_sorted = sorted(
            self.players,
            key=lambda player: (player.score, player.elo),
            reverse=True,
        )
        return players_sorted

    def generate_pair_first_round(self) -> List[Participant]:
        """Method allows to generate pairs of players according
        to the Swiss tournament system.

        Args:
            players [list]: a list of Participant instance.
            Tournament.current_round (int): contains the current round.

        Returns:
            players_pair (list): return a list of Participant instance pairs
        """
        players = self.sort_elo_players()
        players_part_one = players[0 : int(self.number_players / 2)]
        players_part_two = players[int(self.number_players / 2) :]
        players_pair = []
        j = 0
        for j in range(int(self.number_players / 2)):
            player_pair = [players_part_one[j], players_part_two[j]]
            players_pair.append(player_pair)
            players_part_one[j].opponents.append(players_part_two[j].player_id)
            players_part_two[j].opponents.append(players_part_one[j].player_id)
            j += 1
        return players_pair

    def generate_pair(self) -> List[Participant]:
        """Method allows to generate pairs of players according
        to the Swiss tournament system.

        Args:
            players [list]: a list of Participant instance.
            Tournament.current_round (int): contains the current round.

        Returns:
            players_pair (list): return a list of Participant instance pairs
        """
        players = self.sort_score_players()
        players_pair = []
        try:
            while players:
                i = 1
                while (
                    i <= len(players)
                    and len(players) > 2
                    and players[i].player_id in players[0].opponents
                ):
                    i += 1
                player_pair = [players[0], players[i]]
                players[0].opponents.append(players[i].player_id)
                players[i].opponents.append(players[0].player_id)
                del players[i]
                del players[0]
                players_pair.append(player_pair)
        except IndexError:
            return None
        return players_pair
