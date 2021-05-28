"""Round views."""

# librairies
from colorama import Fore

# views
from views.user import UserView

# utils
from utils.utils import isfloat


class RoundView(UserView):
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
    def menu() -> None:
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
    def print_players_pair(player_one: object, player_two: object) -> None:
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
