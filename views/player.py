"""Player views."""

# librairies
from typing import List
from colorama import Fore

# models
from models.players import Participant

# views
from views.abstract import AbstractView


class PlayerView(AbstractView):
    """Player view

    Static Methods:
        sub_players_menu() -> None:
            Show players menu.
        print_header_player_array() -> None:
            Print header of player array.
        print_player(player_id: int, last_name: str,
        first_name: str, birth_date: str, sex: str, elo: int,
        ) -> None:
            Display a array with information of player dict.

    Methods:
        prompt_player_sex(self) -> str:
            Prompt for get player sex.
    """

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
                confirm = self.prompt_confirm()
                if confirm == "Y":
                    return sex

    @staticmethod
    def sub_players_menu() -> None:
        """Show players menu."""
        print(Fore.LIGHTWHITE_EX + f'{"* MENU PLAYERS*"}'.center(119))
        print(Fore.LIGHTWHITE_EX + "[1] Ajouter un joueur.")
        print("[2] Modifier le classement Elo d'un joueur.")
        print("[3] Afficher par classement Elo.")
        print("[0] Retour au menu principal.\n")
        print(Fore.CYAN + f'{"=" * 119}')

    @staticmethod
    def print_header_player_array() -> None:
        """Print header of player array."""
        print(
            f"{'ID'.center(10)} | "
            f"{'Nom'.center(25)} | "
            f"{'Pr??nom'.center(25)} | "
            f"{'Date de naissance'.center(20)} | "
            f"{'Sexe'.center(10)} | "
            f"{'Elo'.center(10)}"
            f"\n{'??' * 119}"
        )

    # pylint: disable=too-many-arguments
    @staticmethod
    def print_player(
        player_id: int,
        last_name: str,
        first_name: str,
        birth_date: str,
        sex: str,
        elo: int,
    ) -> None:
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

    @staticmethod
    def print_players_tournament(players: List[Participant]) -> None:
        """[summary]

        Args:
            players ([type]): [description]
        """
        print(
            f"{'Classement'.center(15)} | "
            f"{'Nom'.center(30)} | "
            f"{'Pr??nom'.center(30)} | "
            f"{'Score'.center(15)} | "
            f"{'Elo'.center(15)}"
            f"\n{'??' * 119}"
        )

        for player in players:
            print(
                f"{str(player.ladder).center(15)} | "
                f"{player.first_name.center(30)} | "
                f"{player.last_name.center(30)} | "
                f"{str(player.score).center(15)} | "
                f"{str(player.elo).center(15)}"
                f"\n{'-' * 119}"
            )
