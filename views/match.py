"""Match views."""

# librairies
from colorama import Fore

# views
from views.user import UserView

# utils
from utils.utils import isfloat


class MatchView(UserView):
    """Round view"""

    # - - - - - - - - - - - #
    # methods               #
    # - - - - - - - - - - - #
    
    @staticmethod
    def print_header_matches_array():
        """[summary]"""
        print(
            f"{'ID'.center(10)} | "
            f"{'Nom'.center(25)} | "
            f"{'Lieu'.center(25)} | "
            f"{'Date'.center(20)} | "
            f"{'Time control'.center(25)}"
            f"\n{'°' * 119}"
        )
        
    @staticmethod
    def print_matches(tournament_id, name, location, dated, time_control):
        """[summary]

        Args:
            tournament_id ([type]): [description]
            name ([type]): [description]
            location ([type]): [description]
            dated ([type]): [description]
            time_control ([type]): [description]
        """
        print(
            f"{str(tournament_id).center(10)} | "
            f"{name.center(25)} | "
            f"{location.center(25)} | "
            f"{dated.center(20)} | "
            f"{time_control.center(25)}"
            f"\n{'-' * 119}"
        )
