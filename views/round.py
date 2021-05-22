"""Round views."""

# librairies
from colorama import Fore
from utils.utils import isfloat
import logging

# logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)



class RoundView:
    """Round view"""

    @property
    def prompt_set_score(self) -> float:
        """Prompt for set player score.

        Returns:
            float: score for player (0.5, 1.0 or 2.0)
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
                while confirm != "Y" or "N":
                    confirm = input(
                        Fore.LIGHTCYAN_EX + "Vous confirmez ? (Y/N) : "
                    ).upper()
                    if confirm == "Y":
                        return float(score)
                    elif confirm == "N":
                        print("Veuillez entrez le score du joueur svp.")
                        break
                    else:
                        print(
                            Fore.LIGHTRED_EX
                            + "Je n'ai pas compris ce que vous voulez dire."
                        )

    @property
    def prompt_choice_menu_round(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        user_choice = 2
        while user_choice not in range(0, 1):
            try:
                user_choice = int(
                    input(Fore.LIGHTBLUE_EX + "Que voulez-vous faire ? : ")
                )
            except (ValueError, TypeError):
                print(Fore.LIGHTRED_EX + "Oops! Je n'ai pas compris votre choix.")
            except Exception as err:
                logger.error("Oops! %s", err)
        return user_choice
   
    def print_players_pair(self, players_pair):
        print("Paires de joueurs : ")
        for player_one, player_two in players_pair:
            print(f"{str(player_one)} VS {str(player_two)}")
