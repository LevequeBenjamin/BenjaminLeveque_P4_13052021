"""User views."""

# librairies
import os
import sys
from colorama import Fore
import logging
import sys

# logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class UserView:
    """User view"""

    def header(self):
        """[summary]"""
        if sys.platform.startswith("linux"):
            os.system("clear")
        elif sys.platform.startswith("win32"):
            os.system("cls")
        elif sys.platform.startswith("darwin"):
            os.system("clear")
        print("\n")
        print(Fore.LIGHTYELLOW_EX + f"   @ @@ @", " ".center(98), " @ @@ @")
        print(f"   @@@@@@", " ".center(98), " @@@@@@")
        print(f"     @@", " ".center(102), " @@")
        print(f"    @@@@", " ".center(100), " @@@@")
        print(f"   @@@@@@", " ".center(98), " @@@@@@")
        print(f"  @@@@@@@@", " ".center(97), "@@@@@@@@")
        print(Fore.CYAN + f"*** -*- CHESS TOURNAMENT -*- ***".center(119))
        print("\n")
        print(f'{"=" * 119}')

    def prompt_start_program(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        user_choice = 6
        while user_choice not in range(0, 6):
            try:
                user_choice = int(
                    input(Fore.LIGHTBLUE_EX + "\nQue voulez-vous faire ? >> ")
                )
            except (ValueError, TypeError):
                print(Fore.LIGHTRED_EX + "Oops! Je n'ai pas compris votre choix.")
            except Exception as err:
                logger.error("Oops! %s", err)
        return user_choice

    def menu(self):
        """Print main menu."""
        self.header()
        print(Fore.LIGHTWHITE_EX + f'{"* MENU *"}'.center(119))
        print("\n" * 1)
        print("::[1] Ajouter un nouveau joueur")
        print("::[2] Créer un tournoi")
        print("::[3] Importer un tournoi")
        print("::[4] Liste des joueurs")
        print("::[5] Liste des tournois")
        print("::[0] Quitter -*-CHESS TOURNAMENT-*-\n")
        print(Fore.CYAN + f'{"=" * 119}')

    def title_h2(self, title):
        print(Fore.LIGHTWHITE_EX + f"{'*' * 60}".center(119))
        print(f"{title}".center(119))
        print(f"{'*' * 60}\n".center(122))

    def exit_program(self):
        """[summary]"""
        print(Fore.LIGHTYELLOW_EX + f'{"*" * 119}')
        print(f"\n" * 2)
        print(
            Fore.WHITE
            + "Merci d'avoir utilisé -*-CHESS TOURNAMENT-*-, à bientôt !!".center(119)
        )
        print("\n" * 2)
        print(Fore.LIGHTYELLOW_EX + f'{"*" * 119}')
        sys.exit()

    def separator_title(self, title):
        """[summary]

        Args:
            title ([type]): [description]
        """
        print(
            Fore.LIGHTYELLOW_EX + f"\n********************* {title} "
            "*********************\n"
        )

    def separator_yellow(self):
        """[summary]"""
        print(
            Fore.LIGHTYELLOW_EX + "*********************************************"
            "***************\n"
        )

    def separator_white(self):
        """[summary]"""
        print(
            Fore.LIGHTWHITE_EX + "*********************************************"
            "***************\n"
        )

    def user_print_msg(self, message):
        """[summary]

        Args:
            message ([type]): [description]
        """
        print(f"{message}")

    def user_print_green_msg(self, message):
        """[summary]

        Args:
            message ([type]): [description]
        """
        print(Fore.LIGHTGREEN_EX + f"{message}")

    def user_print_err(self, message):
        """[summary]

        Args:
            message ([type]): [description]
        """
        print(Fore.LIGHTRED_EX + f"{message}")

    def prompt_confirm(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        confirm = ""
        while confirm != "Y" or "N":
            confirm = input(Fore.LIGHTCYAN_EX + "Vous confirmez ? (Y/N) : ").upper()
            if confirm not in ["Y", "N"]:
                print(Fore.LIGHTRED_EX + "Je n'ai pas compris ce que vous voulez dire.")
            else:
                return confirm

    def prompt_return(self):
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
            else:
                return confirm

    def prompt_choice_menu(self, choice: int) -> int:
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
            except Exception as err:
                logger.error("Oops! %s", err)
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
                while confirm != "Y" or "N":
                    confirm = input(
                        Fore.LIGHTCYAN_EX + "Vous confirmez ? (Y/N) : "
                    ).upper()
                    if confirm == "Y":
                        return value
                    elif confirm == "N":
                        print(f"Veuillez entrez {argument_two} svp.")
                        break
                    else:
                        print(
                            Fore.LIGHTRED_EX
                            + "Je n'ai pas compris ce que vous voulez dire."
                        )

    def prompt_id(self, argument_one, argument_two) -> int:
        """Prompt for get tournament id.

        Returns:
            tournament_id (int): id to search for a tournament in the database.
        """
        confirm = ""
        while confirm != "Y":
            value = input(
                Fore.LIGHTCYAN_EX
                + f"\nentrez {argument_two} du {argument_one} que vous voulez importer : "
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
                while confirm != "Y" or "N":
                    confirm = input(
                        Fore.LIGHTCYAN_EX + "Vous confirmez ? (Y/N) : "
                    ).upper()
                    if confirm == "Y":
                        return int(value)
                    elif confirm == "N":
                        print(f"Veuillez entrez {argument_two} du {argument_one} svp.")
                        break
                    else:
                        print(
                            Fore.LIGHTRED_EX
                            + "Je n'ai pas compris ce que vous voulez dire."
                        )
