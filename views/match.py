"""Match views."""


# views
from views.user import UserView


class MatchView(UserView):
    """Round view"""

    # - - - - - - - - - - - #
    # methods               #
    # - - - - - - - - - - - #

    @staticmethod
    def print_matches(tournament):
        """[summary]

        Args:
            tournament ([type]): [description]
        """
        for round_game in tournament.rounds:
            print(f"\n{'=' * 119}")
            print(f"{'-' * 20}".center(119))
            print(f"{round_game.name.center(119)}")
            print(f"{'-' * 20}".center(119))
            print(
                f"{'Nom'.center(20)} | "
                f"{'Prénom'.center(20)} | "
                f"{'Score'.center(25)} | "
                f"{'Nom'.center(20)} | "
                f"{'Prénom'.center(20)}"
                f"\n{'°' * 119}"
            )
            for match in round_game.serialize_match:
                print(
                    f"{match['match'][0][0]['last_name'].center(20)} | "
                    f"{match['match'][0][0]['first_name'].center(20)} | "
                    f"{str(match['match'][0][1]).center(11)} | "
                    f"{str(match['match'][1][1]).center(11)} | "
                    f"{match['match'][1][0]['last_name'].center(20)} | "
                    f"{match['match'][1][0]['first_name'].center(20)}"
                    f"\n{'-' * 119}"
                )
