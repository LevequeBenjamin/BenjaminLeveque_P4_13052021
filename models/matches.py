"""Define the matches."""

# librairies
from typing import Dict, List, Tuple


class Match:  # pylint: disable=too-few-public-methods
    """This is a class allowing to create a match.

    Attributs:
        player_one: Paricipant instance
        player_two: Participant instance
        score_player_one: float, player result
        score_player_two: float, player result
        matches: Tuple(List[Dict, float], List[Dict, float]) = (
            [player_one, score_player_one],
            [player_two, score_player_two],
        )
    Properties:
        serialize(self) -> Dict:
            Serialize matches.
    """

    # - - - - - - - - - - - #
    # special methods       #
    # - - - - - - - - - - - #

    def __init__(
        self,
        player_one: Dict,
        player_two: Dict,
        score_player_one: float,
        score_player_two: float,
    ) -> None:
        """Inits Match

        Args:
            player_one (dict): contains a reference to a Participant instance
            player_two (dict): contains a reference to a Participant instance
            score_player_one ([Float): contains the score of player one
            score_player_two (Float): contains the score of player one
        """
        self.player_one = player_one
        self.player_two = player_two
        self.score_player_one = score_player_one
        self.score_player_two = score_player_two
        self.matches: Tuple(List[Dict, float], List[Dict, float]) = (
            [player_one, score_player_one],
            [player_two, score_player_two],
        )

    # - - - - - - - - - - - #
    # properties            #
    # - - - - - - - - - - - #

    @property
    def serialize(self) -> Dict:
        """Serialize matches.

        Returns:
            dict: a dictionary of matches
        """
        return {"match": self.matches}
