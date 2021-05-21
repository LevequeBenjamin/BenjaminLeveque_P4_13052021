"""User views."""

from colorama import Fore
import logging
import sys

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class UserView:
    """User view"""

    @property
    def header(self):
        print(
            Fore.LIGHTCYAN_EX + "\n======================================"
            "======================"
        )
        print("                      CHESS TOURNAMENT                      ")
        print("============================================================ \n")

    @property
    def prompt_start_program(self):
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

    @property
    def menu(self):
        """Print main menu."""
        print(Fore.LIGHTWHITE_EX + "[1] Ajouter un nouveau joueur.")
        print("[2] Créer un tournoi.")
        print("[3] Importer un tournoi.")
        print("[0] Quitter Chess Tournament.\n")

    @property
    def exit_program(self):
        self.separator_yellow
        print(
            Fore.WHITE + "    Merci d'avoir utilisé Chess " "Tournament, à bientôt !!"
        )
        self.separator_yellow
        sys.exit()

    def separator_title(self, title):
        print(
            Fore.LIGHTYELLOW_EX + f"\n********************* {title} "
            "*********************\n"
        )

    @property
    def separator_yellow(self):
        print(
            Fore.LIGHTYELLOW_EX + "*********************************************"
            "***************\n"
        )

    @property
    def separator_white(self):
        print(
            Fore.LIGHTWHITE_EX + "*********************************************"
            "***************\n"
        )

    def user_print_msg(self, message):
        print(f"{message}")

    def user_print_green_msg(self, message):
        print(Fore.LIGHTGREEN_EX + f"{message}")

    def user_print_err(self, message):
        print(Fore.LIGHTRED_EX + f"{message}")

    @property
    def prompt_confirm(self):
        confirm = ""
        while confirm != "Y" or "N":
            confirm = input(Fore.LIGHTCYAN_EX + "Vous confirmez ? (Y/N) : ").upper()
            if confirm not in ["Y", "N"]:
                print(Fore.LIGHTRED_EX + "Je n'ai pas compris ce que vous voulez dire.")
            else: return confirm
