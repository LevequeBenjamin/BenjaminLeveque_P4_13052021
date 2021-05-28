"""Player views."""

# librairies
import logging
from colorama import Fore

# views
from views.user import UserView

# logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class PlayerView:
    """Player view"""

    # - - - - - - - - - - - #
    # special methods       #
    # - - - - - - - - - - - #

    def __init__(self):
        """Inits TournamentView"""
        self.user_views = UserView()

    # - - - - - - - - - - - #
    # methods               #
    # - - - - - - - - - - - #

    def prompt_player_sex(self) -> str:
        """Prompt for get player sex.

        Returns:
            sex (str): sex for create player instance.
        """
        confirm = ""
        while confirm != "Y":
            sex = input(
                Fore.LIGHTCYAN_EX
                + "Veuillez entrer (M) pour masculin ou (F) pour feminin : "
            ).upper()
            if not sex or sex not in ["M", "F"]:
                print(
                    Fore.LIGHTRED_EX + "Je n'ai pas compris ce que vous voulez dire, "
                    "Veuillez entrer une commande valide svp."
                )
            else:
                print(Fore.LIGHTGREEN_EX + f"Le sexe du joueur est : {sex}")
                confirm = self.user_views.prompt_confirm()
                if confirm == "Y":
                    return sex

    def prompt_player_elo(self) -> int:
        """Prompt for get player elo.

        Returns:
            elo (int): elo for create Player instance.
        """
        confirm = ""
        while confirm != "Y":
            elo = input(
                Fore.LIGHTCYAN_EX
                + "entrez le classement Elo du joueur en caractère numerique: "
            )
            if not elo.isnumeric() or not elo:
                print(
                    Fore.LIGHTRED_EX + "Je n'ai pas compris ce que vous voulez dire, "
                    "veuillez entrer le classement Elo du joueur en caractère numerique svp."
                )
            else:
                print(Fore.LIGHTGREEN_EX + f"Le classement elo du joueur est: {elo}")
                confirm = self.user_views.prompt_confirm()
                if confirm == "Y":
                    return int(elo)

    @staticmethod
    def menu() -> None:
        """Show players menu."""
        print(Fore.LIGHTWHITE_EX + f'{"* MENU PLAYERS*"}'.center(119))
        print(Fore.LIGHTWHITE_EX + "[1] Ajouter un joueur.")
        print("[2] Modifier le classement Elo d'un joueur.")
        print("[0] Retour au menu principal.\n")
        print(Fore.CYAN + f'{"=" * 119}')

    @staticmethod
    def print_header_player_array():
        """[summary]"""
        print(
            f"{'ID'.center(10)} | "
            f"{'Nom'.center(25)} | "
            f"{'Prénom'.center(25)} | "
            f"{'Date de naissance'.center(20)} | "
            f"{'Sexe'.center(10)} | "
            f"{'Elo'.center(10)}"
            f"\n{'°' * 119}"
        )

    # pylint: disable=too-many-arguments
    @staticmethod
    def print_player(player_id, last_name, first_name, birth_date, sex, elo) -> None:
        """Display a array with information of player dict.

        Args:
            player (dict): a dict of player.
        """
        print(
            f"{str(player_id).center(10)} | "
            f"{last_name.center(25)} | "
            f"{first_name.center(25)} | "
            f"{birth_date.center(20)} | "
            f"{sex.center(10)} | "
            f"{str(elo).center(10)}"
            f"\n{'-' * 119}"
        )
