"""Round views."""

# librairies
from colorama import Fore

# models
from models.players import Participant
from models.tournaments import Tournament

# views
from views.abstract import AbstractView

# utils
from utils.utils import isfloat


class RoundView(AbstractView):
    """Round view"""

    # - - - - - - - - - - - #
    # methods               #
    # - - - - - - - - - - - #

    def prompt_set_score(self) -> float:
        """Prompt for get player score.

        Returns:
            score (float): score for player
        """
        confirm = ""
        while confirm != "Y":
            score = input(
                Fore.LIGHTCYAN_EX + "entrez le score du joueur en caractère numerique: "
            )
            if not isfloat(score) or score is None:
                print(
                    Fore.LIGHTRED_EX + "Je n'ai pas compris ce que vous voulez dire, "
                    "veuillez entrer le score du joueur en caractère numerique svp."
                )
            else:
                confirm = self.prompt_confirm()
                if confirm == "Y":
                    return float(score)

    @staticmethod
    def sub_round_menu() -> None:
        """Show rounds menu."""
        print(Fore.LIGHTWHITE_EX + f'{"* MENU RONDE *"}'.center(119))
        print("\n" * 1)
        print(Fore.LIGHTWHITE_EX + "\n[1] Inscrire les résultats.")
        print("[0] Annuler et revenir au menu tournoi.\n")
        print(Fore.CYAN + f'{"=" * 119}')

    @staticmethod
    def print_header_players_pair_array():
        """[summary]"""
        print(
            Fore.LIGHTBLUE_EX + f"{'Nom'.center(24)} | "
            f"{'Prénom'.center(24)} | "
            f"{'VS'.center(10)} | "
            f"{'Nom'.center(24)} | "
            f"{'Prenom'.center(24)}"
            f"\n{'°' * 119}"
        )

    @staticmethod
    def print_players_pair(player_one: Participant, player_two: Participant) -> None:
        """Display a array with information of player one et two.

        Args:
            player_one (object): a Participant instance.
            player_two (object): a Participant instance.
        """
        print(
            Fore.LIGHTWHITE_EX + f"{player_one.last_name.center(24)} | "
            f"{player_one.first_name.center(24)}"
            + Fore.LIGHTYELLOW_EX
            + f" | {'*'.center(10)} | "
            + Fore.LIGHTWHITE_EX
            + f"{player_two.last_name.center(24)} | "
            f"{player_two.first_name.center(24)}"
            f"\n{'-' * 119}"
        )

    @staticmethod
    def print_header_rounds_array():
        """[summary]"""
        print(
            f"{'Nom'.center(25)} | "
            f"{'Début de ronde'.center(35)} | "
            f"{'Fin de ronde'.center(35)}"
            f"\n{'°' * 100}"
        )

    @staticmethod
    def print_rounds(tournament: Tournament):
        """[summary]

        Args:
            tournament_id ([type]): [description]
            name ([type]): [description]
            location ([type]): [description]
            dated ([type]): [description]
            time_control ([type]): [description]
        """
        for round_game in tournament.rounds:
            print(
                f"{round_game.name.center(25)} | "
                f"{round_game.created_at.center(35)} | "
                f"{round_game.finished_at.center(35)}"
                f"\n{'-' * 100}"
            )
            
    @staticmethod
    def print_matches(tournament: Tournament):
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
