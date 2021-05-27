"""Tournament views."""

# librairies
import logging
from colorama import Fore

# views
from views.user import UserView

# logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class TournamentView:
    """TounamentView view"""

    # - - - - - - - - - - - #
    # special methods       #
    # - - - - - - - - - - - #

    def __init__(self):
        """Inits TournamentView"""
        self.user_views = UserView()

    # - - - - - - - - - - - #
    # methods               #
    # - - - - - - - - - - - #

    @staticmethod
    def choice_time_control() -> None:
        """Show time control choice."""
        print(Fore.LIGHTWHITE_EX + "[1] Bullet.")
        print("[2] Blitz.")
        print("[3] Coup rapide.")

    @staticmethod
    def perform_time_control(choice: int) -> str:
        """Performs according to the user choice.

        Args:
            user_choice (int): user choice

        Returns:
            'Bullet' if choice == 1.
            'Blitz' if choice == 2.
            'Coup rapide' if choice == 3.
        """
        if choice == 1:
            return "Bullet"
        if choice == 2:
            return "Blitz"
        if choice == 3:
            return "Coup rapide"
        return None

    def prompt_tournament_time_control(self) -> str:
        """Prompt for get tournament time control.

        Returns:
            time_control (str): time control for create Tournament instance.
        """
        self.choice_time_control()
        choice = 0
        confirm = ""
        while choice not in range(1, 4):
            try:
                choice = int(
                    input(
                        Fore.LIGHTCYAN_EX
                        + "Veuillez choisir parmis les 3 time control : "
                    )
                )
                if choice not in range(1, 4):
                    print(Fore.LIGHTRED_EX + "Oops! Je n'ai pas compris votre choix.")
                elif choice in range(1, 4):
                    while confirm != "Y":
                        confirm = input(
                            Fore.LIGHTCYAN_EX + "Vous confirmez ? (Y/N) : "
                        ).upper()
                        if confirm == "Y":
                            return self.perform_time_control(choice)
                        if confirm == "N":
                            choice = 0
                            break
                        print(
                            Fore.LIGHTRED_EX
                            + "Je n'ai pas compris ce que vous voulez dire."
                        )
            except (ValueError, TypeError):
                print(Fore.LIGHTRED_EX + "Oops! Je n'ai pas compris votre choix.")

    def menu(self, tournament: object) -> None:
        """Show tournament menu.

        Args:
            tournament (Object): a Tournament instance.
        """
        self.user_views.header()
        print(Fore.LIGHTWHITE_EX + f'{"* MENU TOURNAMENT*"}'.center(119))
        if tournament.current_round < 5:
            if not tournament.players or len(tournament.serialize_players()) < 8:
                print(Fore.LIGHTWHITE_EX + "[1] Ajouter 8 joueurs.")
                print("[0] Quitter le tournoi.\n")
            else:
                print(
                    Fore.LIGHTWHITE_EX
                    + f"[1] Démarrer le tour : {tournament.current_round}."
                )
                print("[0] Quitter le tournoi.\n")
        else:
            print(Fore.LIGHTWHITE_EX + "[1] Afficher le classement.")
            print("[2] Afficher les matches.")
            print("[0] Quitter le tournoi.\n")
        print(Fore.CYAN + f'{"=" * 119}')

    @staticmethod
    def prompt_choice_menu_tournament():
        """[summary]

        Returns:
            [type]: [description]
        """
        user_choice = 4
        while user_choice not in range(0, 4):
            try:
                user_choice = int(
                    input(Fore.LIGHTBLUE_EX + "Que voulez-vous faire ? : ")
                )
            except (ValueError, TypeError):
                print(Fore.LIGHTRED_EX + "Oops! Je n'ai pas compris votre choix.")
        return user_choice

    @staticmethod
    def menu_tournois():
        """[summary]"""
        print(Fore.LIGHTWHITE_EX + f'{"* MENU TOURNAMENTS*"}'.center(119))
        print("[1] Importez un tournoi.")
        print("[0] Retour au menu principal.\n")
        print(Fore.CYAN + f'{"=" * 119}')

    @staticmethod
    def prompt_menu_tournaments():
        """[summary]

        Returns:
            [type]: [description]
        """
        user_choice = 3
        while user_choice not in range(0, 3):
            try:
                user_choice = int(
                    input(Fore.LIGHTBLUE_EX + "\nQue voulez-vous faire ? >> ")
                )
            except (ValueError, TypeError):
                print(Fore.LIGHTRED_EX + "Oops! Je n'ai pas compris votre choix.")
        return user_choice

    @staticmethod
    def print_current_tournament(tournament):
        """[summary]

        Args:
            tournament ([type]): [description]
        """
        print(
            f"{'Ronde en cours'.center(20)} | "
            f"{'Nom'.center(22)} | "
            f"{'Lieu'.center(22)} | "
            f"{'Date'.center(22)} | "
            f"{'Time control'.center(22)}"
            f"\n{'°' * 119}"
        )
        if tournament.current_round == 5:
            print(
                f"{str(tournament.current_round).center(20)} | "
                f"{tournament.name.center(22)} | "
                f"{tournament.location.center(22)} | "
                f"{tournament.dated.center(22)} | "
                f"{tournament.time_control.center(22)}"
                f"\n{'-' * 119}"
            )
        else:
            print(
                f"{tournament.current_tournament.center(20)} | "
                f"{tournament.name.center(22)} | "
                f"{tournament.location.center(22)} | "
                f"{tournament.dated.center(22)} | "
                f"{tournament.time_control.center(22)}"
                f"\n{'-' * 119}"
            )

    @staticmethod
    def print_confirm_tournament(name, location, dated, time_control, description):
        """[summary]

        Args:
            name ([type]): [description]
            location ([type]): [description]
            dated ([type]): [description]
            time_control ([type]): [description]
            description ([type]): [description]
        """
        print(
            f"{'Nom'.center(25)} | "
            f"{'Lieu'.center(35)} | "
            f"{'Date'.center(25)} | "
            f"{'Time control'.center(25)}"
            f"\n{'°' * 119}"
        )

        print(
            f"{name.center(25)} | "
            f"{location.center(35)} | "
            f"{dated.center(25)} | "
            f"{time_control.center(25)}"
            f"\n{'-' * 119}"
        )

        print(f"description : {description}" f"\n{'-' * 119}")

    @staticmethod
    def print_result_tournament(players):
        """[summary]

        Args:
            players ([type]): [description]
        """
        print(
            f"{'Classement'.center(15)} | "
            f"{'Nom'.center(30)} | "
            f"{'Prénom'.center(30)} | "
            f"{'Score'.center(15)} | "
            f"{'Elo'.center(15)}"
            f"\n{'°' * 119}"
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

    @staticmethod
    def print_header_tournament_array():
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
    def print_tournament(tournament_id, name, location, dated, time_control):
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
