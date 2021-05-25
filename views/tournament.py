"""Tournament views."""

# librairies
from views.user import UserView
from colorama import Fore
import logging

# logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class TournamentView:
    """User view"""

    def __init__(self):
        self.user_views = UserView()

    def prompt_tournament_name(self) -> str:
        """Prompt for get tournament name.

        Returns:
            str: name for class Tournament
        """
        confirm = ""
        while confirm != "Y":
            name = input(Fore.LIGHTCYAN_EX + "entrez le nom du tournoi : ").capitalize()
            if not name:
                print(
                    Fore.LIGHTRED_EX + "Je n'ai pas compris ce que vous voulez dire, "
                    "veuillez entrer un nom svp"
                )
            else:
                print(Fore.LIGHTGREEN_EX + f"Le nom du tournoi est: {name}")
                while confirm != "Y" or "N":
                    confirm = input(
                        Fore.LIGHTCYAN_EX + "Vous confirmez ? (Y/N) : "
                    ).upper()
                    if confirm == "Y":
                        return name
                    elif confirm == "N":
                        print("Veuillez entrez un nouveau nom svp.")
                        break
                    else:
                        print(
                            Fore.LIGHTRED_EX
                            + "Je n'ai pas compris ce que vous voulez dire."
                        )

    def prompt_tournament_location(self) -> str:
        """prompt for get tournament location

        Returns:
            str: location for class Tournament
        """
        confirm = ""
        while confirm != "Y":
            location = input(Fore.LIGHTCYAN_EX + "entrez l'adresse du tournoi : ")
            if not location:
                print(
                    Fore.LIGHTRED_EX + "Je n'ai pas compris ce que vous voulez dire, "
                    "veuillez entrer l'adresse du tournoi svp"
                )
            else:
                print(Fore.LIGHTGREEN_EX + f"Le tournoi se passe à: {location}")
                while confirm != "Y" or "N":
                    confirm = input(
                        Fore.LIGHTCYAN_EX + "Vous confirmez ? (Y/N) : "
                    ).upper()
                    if confirm == "Y":
                        return location
                    elif confirm == "N":
                        print("Veuillez entrez une nouvelle adresse svp.")
                        break
                    else:
                        print(
                            Fore.LIGHTRED_EX
                            + "Je n'ai pas compris ce que vous voulez dire."
                        )

    def prompt_tournament_dated(self) -> str:
        """prompt for get tournament dated

        Returns:
            str: dated for class Tournament
        """
        confirm = ""
        while confirm != "Y":
            dated = input(Fore.LIGHTCYAN_EX + "entrez la date du tournoi : ")
            if not dated:
                print(
                    Fore.LIGHTRED_EX + "Je n'ai pas compris ce que vous voulez dire, "
                    "veuillez entrer la date du tournoi svp"
                )
            else:
                print(Fore.LIGHTGREEN_EX + f"Le tournoi se passe le: {dated}")
                while confirm != "Y" or "N":
                    confirm = input(
                        Fore.LIGHTCYAN_EX + "Vous confirmez ? (Y/N) : "
                    ).upper()
                    if confirm == "Y":
                        return dated
                    elif confirm == "N":
                        print("Veuillez entrez une date svp.")
                        break
                    else:
                        print(
                            Fore.LIGHTRED_EX
                            + "Je n'ai pas compris ce que vous voulez dire."
                        )

    def choice_time_control(self):
        """[summary]"""
        print(Fore.LIGHTWHITE_EX + "[1] Bullet.")
        print("[2] Blitz.")
        print("[3] Coup rapide.")

    def perform_time_control(self, choice):
        """Performs according to the user choice.

        Args:
            user_choice (int): user choice

        Returns:

        """
        if choice == 1:
            return "Bullet"
        elif choice == 2:
            return "Blitz"
        elif choice == 3:
            return "Coup rapide"

    def prompt_tournament_time_control(self) -> str:
        """prompt for get tournament time control

        Returns:
            str: time control for class Tournament
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
                        elif confirm == "N":
                            choice = 0
                            break
                        else:
                            print(
                                Fore.LIGHTRED_EX
                                + "Je n'ai pas compris ce que vous voulez dire."
                            )
            except (ValueError, TypeError):
                print(Fore.LIGHTRED_EX + "Oops! Je n'ai pas compris votre choix.")

    def prompt_tournament_description(self) -> str:
        """prompt for get tournament description

        Returns:
            str: description for class Tournament
        """
        confirm = ""
        while confirm != "Y":
            description = input(
                Fore.LIGHTCYAN_EX + "entrez une description pour ce tournoi : "
            )
            if not description:
                print(
                    Fore.LIGHTRED_EX + "Je n'ai pas compris ce que vous voulez dire, "
                    "veuillez entrer une description pour ce tournoi svp"
                )
            else:
                print(Fore.LIGHTGREEN_EX + f"Description du tournoi : {description}")
                while confirm != "Y" or "N":
                    confirm = input(
                        Fore.LIGHTCYAN_EX + "Vous confirmez ? (Y/N) : "
                    ).upper()
                    if confirm == "Y":
                        return description
                    elif confirm == "N":
                        print("Veuillez entrez une description svp.")
                        break
                    else:
                        print(
                            Fore.LIGHTRED_EX
                            + "Je n'ai pas compris ce que vous voulez dire."
                        )

    def prompt_tournament_id(self) -> int:
        """[summary]

        Returns:
            int: [description]
        """
        confirm = ""
        while confirm != "Y":
            id = input(
                Fore.LIGHTCYAN_EX
                + "\nentrez l'id du tournoi que vous voulez importer : "
            )
            if not id.isnumeric() or not id:
                print(
                    Fore.LIGHTRED_EX + "Je n'ai pas compris ce que vous voulez dire, "
                    "veuillez entrer l'id du tournoi en caractère numerique svp."
                )
            else:
                print(Fore.LIGHTGREEN_EX + f"L'id du tournoi est: {id}")
                while confirm != "Y" or "N":
                    confirm = input(
                        Fore.LIGHTCYAN_EX + "Vous confirmez ? (Y/N) : "
                    ).upper()
                    if confirm == "Y":
                        return int(id)
                    elif confirm == "N":
                        print("Veuillez entrez l'id du tournoi svp.")
                        break
                    else:
                        print(
                            Fore.LIGHTRED_EX
                            + "Je n'ai pas compris ce que vous voulez dire."
                        )

    def menu(self, tournament):
        """Print tournament menu.

        Args:
            tournament ([type]): [description]
        """
        self.user_views.header()
        print(Fore.LIGHTWHITE_EX + f'{"* MENU TOURNAMENT*"}'.center(119))
        if tournament.get_current_round() < 5:
            if not tournament.get_list_players() or len(tournament.serialize_players()) < 8:
                print(Fore.LIGHTWHITE_EX + "[1] Ajouter 8 joueurs.")
                print("[0] Quitter le tournoi.\n")
            else:
                print(Fore.LIGHTWHITE_EX + f"[1] Démarrer le tour : {tournament.get_current_round()}.")
                print("[0] Quitter le tournoi.\n")
        else:
            print(Fore.LIGHTWHITE_EX + "[1] Afficher le classement.")
            print("[2] Afficher les matches.")
            print("[0] Quitter le tournoi.\n")
        print(Fore.CYAN + f'{"=" * 119}')

    def prompt_choice_menu_tournament(self):
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
            except Exception as err:
                logger.error("Oops! %s", err)
        return user_choice

    def menu_tournois(self):
        """[summary]
        """
        print(Fore.LIGHTWHITE_EX + f'{"* MENU TOURNAMENTS*"}'.center(119))
        print(Fore.LIGHTWHITE_EX + "[1] Importez un tournoi.")
        print("[2] Afficher les résultats d'un tournoi.")
        print("[0] Retour au menu principal.\n")
        print(Fore.CYAN + f'{"=" * 119}')

    def prompt_menu_tournaments(self):
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
            except Exception as err:
                logger.error("Oops! %s", err)
        return user_choice

    def print_tournois(self, tournois):
        print(f"{'ID'.center(10)} | "
              f"{'Nom'.center(25)} | "
              f"{'Lieu'.center(25)} | "
              f"{'Date'.center(20)} | "
              f"{'Time control'.center(25)}"
              f"\n{'°' * 119}")

        for tournoi in tournois:
            print(f"{str(tournoi.doc_id).center(10)} | "
                  f"{tournoi['name'].center(25)} | "
                  f"{tournoi['location'].center(25)} | "
                  f"{tournoi['dated'].center(20)} | "
                  f"{tournoi['time_control'].center(25)}"
                  f"\n{'-' * 119}")

    def print_one_tournament(self, tournoi):
        print(f"{'ID'.center(10)} | "
              f"{'Nom'.center(25)} | "
              f"{'Lieu'.center(25)} | "
              f"{'Date'.center(20)} | "
              f"{'Time control'.center(25)}"
              f"\n{'°' * 119}")

        print(f"{str(tournoi.doc_id).center(10)} | "
              f"{tournoi['name'].center(25)} | "
              f"{tournoi['location'].center(25)} | "
              f"{tournoi['dated'].center(20)} | "
              f"{tournoi['time_control'].center(25)}"
              f"\n{'-' * 119}")

    def print_current_tournament(self, tournoi):
        print(f"{'Ronde en cours'.center(20)} | "
              f"{'Nom'.center(22)} | "
              f"{'Lieu'.center(22)} | "
              f"{'Date'.center(22)} | "
              f"{'Time control'.center(22)}"
              f"\n{'°' * 119}")

        print(f"{str(tournoi.get_current_round()).center(20)} | "
              f"{tournoi.get_name().center(22)} | "
              f"{tournoi.get_location().center(22)} | "
              f"{tournoi.get_dated().center(22)} | "
              f"{tournoi.get_time_control().center(22)}"
              f"\n{'-' * 119}")

    def print_confirm_tournament(self, name, location, dated, time_control, description):
        print(f"{'Nom'.center(25)} | "
              f"{'Lieu'.center(35)} | "
              f"{'Date'.center(25)} | "
              f"{'Time control'.center(25)}"
              f"\n{'°' * 119}")

        print(f"{name.center(25)} | "
              f"{location.center(35)} | "
              f"{dated.center(25)} | "
              f"{time_control.center(25)}"
              f"\n{'-' * 119}")

        print(f"description : {description}"
              f"\n{'-' * 119}")

    def print_result_tournament(self, players):
        print(f"{'Classement'.center(15)} | "
              f"{'Nom'.center(30)} | "
              f"{'Prénom'.center(30)} | "
              f"{'Score'.center(15)} | "
              f"{'Elo'.center(15)}"
              f"\n{'°' * 119}")

        for player in players:
            print(f"{str(player.get_ladder()).center(15)} | "
                  f"{player.get_first_name().center(30)} | "
                  f"{player.get_last_name().center(30)} | "
                  f"{str(player.get_score()).center(15)} | "
                  f"{str(player.get_elo()).center(15)}"
                  f"\n{'-' * 119}")
