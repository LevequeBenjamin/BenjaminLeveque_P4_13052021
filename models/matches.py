"""Define the matches."""


class Match: # pylint: disable=too-few-public-methods 
    """This is a class allowing to create a match."""

    # - - - - - - - - - - - #
    # special methods       #
    # - - - - - - - - - - - #

    def __init__(
        self,
        player_one: dict,
        player_two: dict,
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
        self.matches = (
            [player_one, score_player_one],
            [player_two, score_player_two],
        )

    # - - - - - - - - - - - #
    # methods               #
    # - - - - - - - - - - - #

    def serialize(self) -> dict:
        """Serialize matches

        Returns:
            dict: a dictionary of matches
        """
        return {"match": self.matches}
