"""Tournament views."""

# librairies
from colorama import Fore

# models
from models.tournaments import Tournament

# views
from views.abstract import AbstractView


class TournamentView(AbstractView):
    """TounamentView view"""

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
                    confirm = self.prompt_confirm()
                    if confirm == "Y":
                        return self.perform_time_control(choice)
                    choice = 0
            except (ValueError, TypeError):
                print(Fore.LIGHTRED_EX + "Oops! Je n'ai pas compris votre choix.")

    def sub_tournament_menu(self, tournament: Tournament) -> None:
        """Show tournament menu.

        Args:
            tournament (Object): a Tournament instance.
        """
        self.header()
        print(Fore.LIGHTWHITE_EX + f'{"* MENU TOURNAMENT*"}'.center(119))
        if tournament.current_round < tournament.number_rounds + 1:
            if (
                not tournament.players
                or len(tournament.serialize_players) < tournament.number_players
            ):
                print(
                    Fore.LIGHTWHITE_EX
                    + f"[1] Ajouter {tournament.number_players} joueurs."
                )
                print("[0] Quitter le tournoi.\n")
            else:
                print(
                    Fore.LIGHTWHITE_EX
                    + f"[1] Démarrer le tour : {tournament.current_round}."
                )
                print("[2] Afficher la liste des participants.")
                print("[3] Afficher la liste des rondes.")
                print("[4] Afficher la liste des matches.")
                print("[0] Quitter le tournoi.\n")
        else:
            print(Fore.LIGHTWHITE_EX + "[1] Afficher le classement.")
            print("[2] Afficher la liste des participants.")
            print("[3] Afficher la liste des rondes.")
            print("[4] Afficher la liste des matches.")
            print("[0] Quitter le tournoi.\n")
        print(Fore.CYAN + f'{"=" * 119}')

    @staticmethod
    def menu_tournaments():
        """[summary]"""
        print(Fore.LIGHTWHITE_EX + f'{"* MENU TOURNAMENTS*"}'.center(119))
        print("[1] Importez un tournoi.")
        print("[0] Retour au menu principal.\n")
        print(Fore.CYAN + f'{"=" * 119}')

    @staticmethod
    def print_current_tournament(tournament: Tournament):
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
        if tournament.current_round == tournament.number_rounds + 1:
            print(
                f"{tournament.current_tournament.center(20)} | "
                f"{tournament.name.center(22)} | "
                f"{tournament.location.center(22)} | "
                f"{tournament.dated.center(22)} | "
                f"{tournament.time_control.center(22)}"
                f"\n{'-' * 119}"
            )
        else:
            print(
                f"{str(tournament.current_round).center(20)} | "
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
