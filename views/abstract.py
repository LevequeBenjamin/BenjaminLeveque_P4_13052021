"""User views."""

# librairies
import os
import sys
from abc import ABC
from colorama import Fore


class AbstractView(ABC):
    """User view"""

    @staticmethod
    def header():
        """[summary]"""
        if sys.platform.startswith("linux"):
            os.system("clear")
        elif sys.platform.startswith("win32"):
            os.system("cls")
        elif sys.platform.startswith("darwin"):
            os.system("clear")
        print("\n")
        print(Fore.LIGHTYELLOW_EX + "   @ @@ @", " ".center(98), " @ @@ @")
        print("   @@@@@@", " ".center(98), " @@@@@@")
        print("     @@", " ".center(102), " @@")
        print("    @@@@", " ".center(100), " @@@@")
        print("   @@@@@@", " ".center(98), " @@@@@@")
        print("  @@@@@@@@", " ".center(97), "@@@@@@@@")
        print(Fore.CYAN + "*** -*- CHESS TOURNAMENT -*- ***".center(119))
        print("\n")
        print("=" * 119)

    def main_menu(self):
        """Print main menu."""
        self.header()
        print(Fore.LIGHTWHITE_EX + "* MENU *".center(119))
        print("\n" * 1)
        print("::[1] Ajouter un nouveau joueur")
        print("::[2] Créer un tournoi")
        print("::[3] Importer un tournoi")
        print("::[4] Liste des joueurs")
        print("::[5] Liste des tournois")
        print("::[0] Quitter -*-CHESS TOURNAMENT-*-\n")
        print(Fore.CYAN + "=" * 119)

    @staticmethod
    def title_h2(title):
        """[summary]

        Args:
            title ([type]): [description]
        """
        print(Fore.LIGHTWHITE_EX + f'{"*" * 60}'.center(119))
        print(f"{title}".center(119))
        print(f'{"*" * 60}'.center(119), "\n")

    @staticmethod
    def exit_program():
        """[summary]"""
        print(Fore.LIGHTYELLOW_EX + "*" * 119)
        print("\n" * 2)
        print(
            Fore.WHITE
            + "Merci d'avoir utilisé -*-CHESS TOURNAMENT-*-, à bientôt !!".center(119)
        )
        print("\n" * 2)
        print(Fore.LIGHTYELLOW_EX + "*" * 119)

    @staticmethod
    def user_print_msg(message):
        """[summary]

        Args:
            message ([type]): [description]
        """
        print(f"{message}")

    @staticmethod
    def prompt_confirm():
        """[summary]

        Returns:
            [type]: [description]
        """
        confirm = ""
        while confirm not in ["Y", "N"]:
            confirm = input(Fore.LIGHTCYAN_EX + "Vous confirmez ? (Y/N) : ").upper()
            if confirm not in ["Y", "N"]:
                print(Fore.LIGHTRED_EX + "Je n'ai pas compris ce que vous voulez dire.")
        return confirm

    @staticmethod
    def prompt_return():
        """[summary]

        Returns:
            [type]: [description]
        """
        confirm = ""
        while confirm != "Y":
            confirm = input(
                Fore.LIGHTCYAN_EX + "\n::[Y] pour retourner au menu >> "
            ).upper()
            if confirm not in ["Y", "N"]:
                print(Fore.LIGHTRED_EX + "Je n'ai pas compris ce que vous voulez dire.")
        return confirm

    @staticmethod
    def prompt_choice_menu(choice: int) -> int:
        """[summary]

        Returns:
            [type]: [description]
        """
        user_choice = choice
        while user_choice not in range(0, choice):
            try:
                user_choice = int(
                    input(Fore.LIGHTBLUE_EX + "Que voulez-vous faire ? : ")
                )
            except (ValueError, TypeError):
                print(Fore.LIGHTRED_EX + "Oops! Je n'ai pas compris votre choix.")
        return user_choice

    def prompt_string(self, argument_one, argument_two) -> str:
        """Prompt for get tournament name.

        Returns:
            name (str): name for create Tournament instance.
        """
        confirm = ""
        while confirm != "Y":
            value = input(
                Fore.LIGHTCYAN_EX + f"entrez {argument_two} du {argument_one} : "
            ).capitalize()
            if not value:
                print(
                    Fore.LIGHTRED_EX + "Je n'ai pas compris ce que vous voulez dire, "
                    f"veuillez entrer {argument_two} svp"
                )
            else:
                print(
                    Fore.LIGHTGREEN_EX
                    + f"{argument_two} du {argument_one} est: {value}"
                )
                confirm = self.prompt_confirm()
                if confirm == "Y":
                    return value

    def prompt_integer(self, argument_one, argument_two) -> int:
        """Prompt for get tournament id.

        Returns:
            tournament_id (int): id to search for a tournament in the database.
        """
        confirm = ""
        while confirm != "Y":
            value = input(
                Fore.LIGHTCYAN_EX
                + f"\nentrez {argument_two} du {argument_one} : "
            )
            if not value.isnumeric() or not value:
                print(
                    Fore.LIGHTRED_EX + "Je n'ai pas compris ce que vous voulez dire, "
                    f"veuillez entrer {argument_two} du {argument_one} en caractère numerique svp."
                )
            else:
                print(
                    Fore.LIGHTGREEN_EX
                    + f"{argument_two} du {argument_one} est: {value}"
                )
                confirm = self.prompt_confirm()
                if confirm == "Y":
                    return int(value)
