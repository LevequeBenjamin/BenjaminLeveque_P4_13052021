"""Define the rounds."""

from typing import List, Dict
from models.matches import Match


class Round:
    """It is a class allowing to create a Round."""

    # - - - - - - - - - - - #
    # special methods       #
    # - - - - - - - - - - - #

    def __init__(
        self, name: str, created_at: str, finished_at: str = None, start: bool = True
    ) -> None:
        """Inits Round.

        Args:
            players (Participant): contains a list of Participant intance,
            name (string): contains the name of the round,
            created_at (string): time retrieved from lib time,
        """
        self.matches: List[Match] = []
        self.name = name
        self.created_at = created_at
        self.finished_at = finished_at
        self.start = start

    # - - - - - - - - - - - #
    # properties            #
    # - - - - - - - - - - - #

    @property
    def serialize(self) -> Dict:
        """Method used to serialize a round before saving
        it in the table TOURNAMENTS.

        Returns:
            a dictionary of Round:
                "round": self.name,
                "created_at": self.created_at,
                "finished_at": self.finished_at,
                "round_in_progress": self.start,
                "list_matches": self.serialize_match(),
        """
        return {
            "round": self.name,
            "created_at": self.created_at,
            "finished_at": self.finished_at,
            "round_in_progress": self.start,
            "list_matches": self.serialize_match,
        }

    @property
    def serialize_match(self) -> List[Dict]:
        """Method used to serialize a list of Match instance before saving
        it in the table TOURNAMENTS.

        Returns:
            matches_serialized (list): contains a list of Match instances serialized
        """
        matches_serialized = []
        for match in self.matches:
            matches_serialized.append(match.serialize)
        return matches_serialized

    # - - - - - - - - - - - #
    # methods               #
    # - - - - - - - - - - - #
