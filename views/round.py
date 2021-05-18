"""Round views."""

# librairies
from colorama import Fore
from utils.utils import isfloat


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
            score = input(Fore.LIGHTCYAN_EX +
                          "entrez le score du joueur en caractère numerique: ")
            if not isfloat(score) or score is None:
                print(Fore.LIGHTRED_EX + "Je n'ai pas compris ce que vous voulez dire, "
                      "veuillez entrer le score du joueur en caractère numerique svp.")
            else:
                while confirm != "Y" or "N":
                    confirm = input("Vous confirmez ? (Y/N) : ").upper()
                    if confirm == "Y":
                        return float(score)
                    elif confirm == "N":
                        print("Veuillez entrez le score du joueur svp.")
                        break
                    else:
                        print(Fore.LIGHTRED_EX +
                              "Je n'ai pas compris ce que vous voulez dire.")
