"""Round views."""

from colorama import Fore


class RoundView:
    """Round view"""
   
    @property
    def prompt_set_score(self) -> int:
        """[summary]

        Returns:
            int: [description]
        """
        confirm = ""
        while confirm != "Y":
            score = input(Fore.LIGHTCYAN_EX +
                "entrez le score du joueur en caractère numerique: ")
            if score.isnumeric() == False or not score:
                print(Fore.LIGHTRED_EX + "Je n'ai pas compris ce que vous voulez dire, "
                      "veuillez entrer le score du joueur en caractère numerique svp.")
            else:
                while confirm != "Y" or "N":
                    confirm = input("Vous confirmez ? (Y/N) : ").upper()
                    if confirm == "Y":
                        return score
                    elif confirm == "N":
                        print("Veuillez entrez le score du joueur svp.")
                        break
                    else:
                        print(Fore.LIGHTRED_EX +
                            "Je n'ai pas compris ce que vous voulez dire.")

